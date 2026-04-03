import re

from helpers import inject
from helpers.cloudflare import wait_for_cloudflare


@inject.webdriver
def glassdoor_rating(company_profile_url, driver):
    driver.get(company_profile_url)
    wait_for_cloudflare(driver)
    print(f'Scraping rating from {company_profile_url}')
    body = driver.page_source
    if result := re.search(r'<p class="rating-headline-average_rating__\w+">([0-5](?:\.[0-9])?)</p>', body):
        return result.group(1)
    if result := re.search(r'"ratingValue"\s*:\s*"([0-5](?:\.[0-9])?)"', body):
        return result.group(1)
    if result := re.search(r'overallRating\\?":?\s*([0-5](?:\.[0-9]+)?)', body):
        return result.group(1)
    return 'unknown'


@inject.webdriver
def glassdoor_engineering_rating(company_profile_url, driver):
    driver.get(company_profile_url)
    wait_for_cloudflare(driver)

    print(f'Scraping engineering rating from {company_profile_url}')
    body = driver.page_source
    if re.search(r'<p.*>There are no reviews matching your search', body):
        return 'unknown'

    if result := re.search(r'<p class="rating-headline-average_rating__\w+">([0-5]\.[0-9])</p>', body):
        return result.group(1)
    if result := re.search(r'RatingHeadline_rating__\w+"[^>]*>([0-5]\.[0-9])</p>', body):
        return result.group(1)
    if result := re.search(r'EmployerAggregateRating.*?"ratingValue":\s*"([0-5]\.[0-9])"', body, re.DOTALL):
        return result.group(1)
    return 'unknown'


@inject.webdriver
def glassdoor_salary(salary_info_url, driver):
    driver.get(salary_info_url)
    wait_for_cloudflare(driver)
    print(f'Scraping salary from {salary_info_url}')
    body = driver.page_source

    # Try embedded JSON salary range (Next.js RSC payload)
    range_result = re.search(
        r'"salaryEstimateRangeLow":(\d+).*?"salaryEstimateRangeHigh":(\d+)',
        body,
    )
    if range_result:
        low = int(range_result.group(1))
        high = int(range_result.group(2))
        currency = ""
        currency_match = re.search(r'"symbol":"([^"]+)"', body)
        if currency_match:
            symbol = currency_match.group(1)
            for char in symbol:
                if char in "£$€":
                    currency = char
                    break
        salary = f"{currency}{low:,} - {currency}{high:,}"
        print(f'Found salary: {salary}')
        return salary

    # Try meta description (e.g. "Average salaries for ... : £73,500.")
    meta_result = re.search(
        r'Average salaries for .+?:\s*([£$€][\d,]+)', body
    )
    if meta_result:
        salary = meta_result.group(1)
        print(f'Found salary: {salary}')
        return salary

    if re.search(r"unable to confidently predict", body):
        print("No salary estimate listed")
        return "unknown"

    raise RuntimeError("Unable to match against page")


@inject.webdriver
def levels_salary(salary_info_url, driver):
    print(f'Scraping salary from {salary_info_url}')
    driver.get(salary_info_url)
    body = driver.page_source
    # Try salary range display (current format)
    range_match = re.search(
        r'commonRangeStart">([$£€][0-9.]+K).*?commonRangeEnd">([$£€][0-9.]+K)',
        body,
        re.DOTALL,
    )
    if range_match:
        return f"{range_match.group(1)} - {range_match.group(2)}"

    # Try older prose formats
    result = re.search(r'The median Software Engineer compensation package at \w+ totals ([£$€][0-9.]+K) per year', body)
    if not result:
        result = re.search(r'The median total compensation package for a[\w\s]+ at [\w\s]+ is\s+([$£€][0-9]+,[0-9]+).', body)
    if not result:
        result = re.search(r'The median Software Engineer compensation in [\w\s]+ package at \w+ totals ([$£€][0-9.]+K) per year', body)

    if result:
        return result.group(1)

    if re.search(r'We only need.*[0-9]+.*submission.*to unlock', body, re.DOTALL):
        print('Not enough data to get salary right now')
        return 'unknown'

    raise RuntimeError("Unable to match against levels.fyi page")


@inject.webdriver
def crunchbase_funding(company_profile_url, driver):

    print(f'Scraping funding info from {company_profile_url}')
    driver.get(company_profile_url)
    body = driver.page_source

    amount_result = re.search(r'text\":\".+ has raised (\$[0-9A-Z.]+)\.\"', body)
    amount = amount_result.group(1) if amount_result is not None else None

    round_result = re.search(r'text\":\".* closed its last funding round on .* from a ([\w\ ]+) round.\"', body)
    latest_round = round_result.group(1) if round_result else None

    if amount and latest_round:
        return f"{amount} ({latest_round})"

    return amount or latest_round
