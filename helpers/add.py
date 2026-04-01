import os
import random
import time
from functools import wraps
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0.1 Safari/605.1.15'
    'Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0'
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15'
    'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'
    'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
]


def random_user_agent(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_agent = random.choice(USER_AGENTS)
        return func(*args, user_agent=user_agent, **kwargs)
    return wrapper


def _find_firefox_profile():
    """Find the default Firefox profile directory."""
    home = Path.home()
    candidates = [
        home / ".mozilla" / "firefox",
        home / ".config" / "mozilla" / "firefox",
        home / ".var" / "app" / "org.mozilla.firefox" / ".mozilla" / "firefox",  # Flatpak
        home / "snap" / "firefox" / "common" / ".mozilla" / "firefox",  # Snap
        home / "Library" / "Application Support" / "Firefox",  # macOS
    ]
    profiles_dir = next((p for p in candidates if p.exists()), None)
    if profiles_dir is None:
        return None
    ini_path = profiles_dir / "profiles.ini"
    if ini_path.exists():
        default_profile = None
        current_path = None
        current_is_relative = True
        for line in ini_path.read_text().splitlines():
            line = line.strip()
            if line.startswith("["):
                if current_path and default_profile:
                    break
                current_path = None
                current_is_relative = True
                default_profile = False
            elif line.startswith("Path="):
                current_path = line.split("=", 1)[1]
            elif line.startswith("IsRelative="):
                current_is_relative = line.split("=", 1)[1] == "1"
            elif line in ("Default=1", "Default=true"):
                default_profile = True
        if current_path:
            if current_is_relative:
                return str(profiles_dir / current_path)
            return current_path
    # Fallback: pick the first *.default-release profile
    for entry in profiles_dir.iterdir():
        if entry.is_dir() and entry.name.endswith(".default-release"):
            return str(entry)
    return None


def browser(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, driver=browser._driver, **kwargs)
            sleep_duration = 30 + (random.random() * 30)
            print(f"Waiting {sleep_duration: .2f} seconds")
            time.sleep(sleep_duration)
        except Exception as e:
            print(str(e))
            print("Sleeping for an hour to allow debug...")
            time.sleep(60*60)
            browser._driver.quit()
            raise

        return result
    return wrapper


_options = FirefoxOptions()
_profile_path = os.environ.get("FIREFOX_PROFILE") or _find_firefox_profile()
if _profile_path:
    print(f"Using Firefox profile: {_profile_path}")
    _options.add_argument("-profile")
    _options.add_argument(_profile_path)
else:
    print("Warning: No Firefox profile found. Glassdoor auth cookies will not be available.")
browser._driver = webdriver.Firefox(options=_options)
