import atexit
import os
import random
import shutil
import tempfile
import time
from functools import wraps
from pathlib import Path

import undetected_chromedriver as uc


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
        # Only check the title for challenge indicators.
        # Checking source for markers like "challenge-platform" causes false
        # positives because normal pages include Cloudflare scripts with that
        # string in their URL.
        title_markers = (
            "just a moment",
            "checking your browser",
        )
        # These only indicate a challenge when the page body is mostly a
        # Cloudflare challenge form, not when they appear in inline scripts
        # on a normal page. Detect them via a dedicated challenge element.
        source_markers = (
            "cf-challenge-running",
            "cf-browser-verification",
            'id="cf-turnstile"',
        )
        if any(marker in title for marker in title_markers) or any(
            marker in source for marker in source_markers
        ):
            input("Cloudflare check detected. Please solve it in the browser, then press Enter...")
            time.sleep(2)
        else:
            break


def browser(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, driver=browser._driver, **kwargs)
            print(f"[{func.__name__}] returned: {result!r}")
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
