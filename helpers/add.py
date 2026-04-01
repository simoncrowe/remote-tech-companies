import atexit
import os
import random
import shutil
import tempfile
import time
from functools import wraps
from pathlib import Path

import undetected_chromedriver as uc

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


def _find_chrome_profile():
    """Find the default Chrome/Chromium user data directory."""
    home = Path.home()
    candidates = [
        home / ".config" / "chromium",
        home / ".config" / "google-chrome",
        home / ".var" / "app" / "com.google.Chrome" / "config" / "google-chrome",  # Flatpak
        home / "snap" / "chromium" / "common" / "chromium",  # Snap
        home / "Library" / "Application Support" / "Google" / "Chrome",  # macOS
    ]
    return next((str(p) for p in candidates if p.exists()), None)


def wait_for_cloudflare(driver):
    """Detect Cloudflare challenge pages and prompt the user to solve them."""
    time.sleep(3)
    while True:
        title = driver.title.lower()
        source = driver.page_source.lower()
        cloudflare_markers = (
            "just a moment",
            "cf-challenge",
            "cf-turnstile",
            "challenge-platform",
            "challenge-running",
            "cf-browser-verification",
            "checking your browser",
            "cf_chl_opt",
        )
        if any(marker in title or marker in source for marker in cloudflare_markers):
            input("Cloudflare check detected. Please solve it in the browser, then press Enter...")
            time.sleep(2)
        else:
            break


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


_options = uc.ChromeOptions()
_profile_path = os.environ.get("CHROME_PROFILE") or _find_chrome_profile()
_temp_profile = None
if _profile_path:
    _temp_profile = tempfile.mkdtemp(prefix="uc_profile_")
    shutil.copytree(
        _profile_path, _temp_profile, dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("SingletonLock", "SingletonSocket", "SingletonCookie"),
    )
    print(f"Using Chrome profile (copied to {_temp_profile})")
    _options.add_argument(f"--user-data-dir={_temp_profile}")
else:
    print("Warning: No Chrome profile found. Glassdoor auth cookies will not be available.")
_chrome_version = None
try:
    import subprocess
    _chrome_out = subprocess.check_output(
        [uc.find_chrome_executable(), "--version"], text=True
    )
    import re as _re
    _version_match = _re.search(r"(\d+)\.\d+\.\d+\.\d+", _chrome_out)
    _chrome_version = int(_version_match.group(1))
    print(f"Detected Chrome version: {_chrome_version}")
except Exception:
    pass
browser._driver = uc.Chrome(options=_options, version_main=_chrome_version)

if _temp_profile:
    atexit.register(shutil.rmtree, _temp_profile, ignore_errors=True)
