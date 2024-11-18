import re

from helpers import add


@add.chromedriver
def glassdoor_rating(company_profile_url, driver):
    driver.get(company_profile_url)
    print(f'Scraping rating from {company_profile_url}')
    body = driver.page_source
    if result := re.search(r'<p class="rating-headline-average_rating__\w+">([0-5]\.[0-9])</p>', body):
        ave_rating = result.group(1)
        print(f'Found rating: {ave_rating}')
        return ave_rating
    if result := re.search(r'overallRating":([0-5]\.[0-9]+)', body):
        ave_rating = result.group(1)
        print(f'Found rating: {ave_rating}')
        return ave_rating
    return 'unknown'


@add.chromedriver
def glassdoor_engineering_rating(company_profile_url, driver):
    driver.get(company_profile_url)
    body = driver.page_source

    print(f'Scraping engineering rating from {company_profile_url}')
    body = driver.page_source
    if re.search(r'<p.*>There are no reviews matching your search', body):
        return 'unknown'

    result = re.search(r'<p class="rating-headline-average_rating__\w+">([0-5]\.[0-9])</p>', body)
    try:
        ave_rating = result.group(1)
    except AttributeError:
        return 'unknown'
    print(f'Found rating: {ave_rating}')
    return ave_rating


@add.chromedriver
def glassdoor_salary(salary_info_url, driver):
    driver.get(salary_info_url)
    print(f'Scraping salary from {salary_info_url}')
    body = driver.page_source

    salary = None
    result = re.search(r'is (\w*[£$€][0-9,K]+\s*[–-]\s*\w*[£$€][0-9,K]+) per year', body)
    if result:
        salary = result.group(0)
        # Try for single salary record
    else:
        result = re.search(
            r'total pay for a .* at .* is ([£\$€][0-9,]+) per year. This number',
            body
        )
        if result:
            salary = result.group(1)

    if salary:
        print(f'Found salary: {salary}')
        salary_range = [amount.strip() for amount in salary.split("-")]
        return " - ".join(salary_range)
    else:
        result = re.search(r"unable to confidently predict", body)
        if result:
            print("No salary estimate listed")
            return "unknown"
        else:
            raise RuntimeError("Unable to match against page")


@add.chromedriver
def levels_salary(salary_info_url, driver):
    print(f'Scraping salary from {salary_info_url}')
    driver.get(salary_info_url)
    body = driver.page_source
    result = re.search(r'The median Software Engineer compensation package at \w+ totals ([£$€][0-9.]+K) per year', body)
    if not result:
        result = re.search(r'The median total compensation package for a[\w\s]+ at [\w\s]+ is\s+([$£€][0-9]+,[0-9]+).', body)
    if not result:
        result = re.search(r'The median Software Engineer compensation in [\w\s]+ package at \w+ totals ([$£€][0-9.]+K) per year', body)

    try:
        salary = result.group(1)
        print(f'Found salary: {salary}')
        return salary
    except AttributeError:
        if re.search(r'We only need.*[0-9]+.*submission.*to unlock',  body):
            print('Not enough data to get salary right now')
            return 'unknown'
        else:
            raise


@add.chromedriver
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
