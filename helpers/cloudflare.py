import time


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
