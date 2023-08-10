import random
import re
import time

import requests

from helpers import add


@add.random_user_agent
def glassdoor_rating(company_profile_url, user_agent):
    headers = {'User-Agent': user_agent}
    print(f'Scraping rating from {company_profile_url}')
    response = requests.get(company_profile_url, headers=headers)
    body = response.content.decode()
    if result := re.search(r'title="([0-5]\.[0-9]+)"', body):
        ave_rating = result.group(1)
        print(f'Found rating: {ave_rating}')
        return ave_rating
    if result := re.search(r'overallRating":([0-5]\.[0-9]+)', body):
        ave_rating = result.group(1)
        print(f'Found rating: {ave_rating}')
        return ave_rating
    return 'unknown'


@add.random_user_agent
def glassdoor_engineering_rating(company_profile_url, user_agent):
    headers = {'User-Agent': user_agent}
    print(f'Scraping rating from {company_profile_url}')
    response = requests.get(company_profile_url, headers=headers)
    body = response.content.decode()
    if re.search(r'<p.*>There are no reviews matching your search', body):
        return 'unknown'

    result = re.search(r'title="([0-5]\.[0-9])"', body)
    try:
        ave_rating = result.group(1)
    except AttributeError:
        return 'unknown'
    print(f'Found rating: {ave_rating}')
    return ave_rating


@add.random_user_agent
def glassdoor_salary(salary_info_url, user_agent):
    headers = {'User-Agent': user_agent}
    print(f'Scraping salary from {salary_info_url}')
    response = requests.get(salary_info_url, headers=headers)
    body = response.content.decode()
    print(body)
    result = re.search(r'[£\$€][0-9,]+\s*-\s*[£\$€][0-9\,]+', body)
    if result:
        salary = result.group(0)
    else:
        # Try for single salary record
        result = re.search(
            r'total pay for a .* at .* is ([£\$€][0-9,]+) per year. This number',
            body
        )
        salary = result.group(1)

    print(f'Found salary: {salary}')
    salary_range = [amount.strip() for amount in salary.split("-")]
    return " - ".join(salary_range)


@add.random_user_agent
def levels_salary(salary_info_url, user_agent):
    headers = {'User-Agent': user_agent}
    print(f'Scraping salary from {salary_info_url}')
    response = requests.get(salary_info_url, headers=headers)
    body = response.content.decode()
    result = re.search(r'The median Software Engineer compensation package at \w+ totals (\$[0-9]+K) per year', body)
    if not result:
        result = re.search(r'The median total compensation package for a[\w\s]+ at [\w\s]+ is\s+([$£][0-9]+,[0-9]+).', body)
    try:
        salary = result.group(1)
        print(f'Found salary: {salary}')
        return salary
    except AttributeError:
        if re.search(r'We only need.*[0-9]+.*submission.*to unlock salary data',  body):
            print('Not enough data to get salary right now')
            return 'unknown'
        else:
            raise


@add.random_user_agent
def crunchbase_funding(company_profile_url, user_agent):
    headers = {'User-Agent': user_agent}
    sleep_duration = 240 + (random.random() * 60)
    print(f"Waiting {sleep_duration:.2f} seconds")
    time.sleep(sleep_duration)

    print(f'Scraping funding info from {company_profile_url}')
    response = requests.get(company_profile_url, headers=headers)
    body = response.content.decode()

    amount_result = re.search(r'text\":\".+ has raised (\$[0-9A-Z.]+)\.\"', body)
    amount = amount_result.group(1) if amount_result is not None else None

    round_result = re.search(r'text\":\".* closed its last funding round on .* from a ([\w\ ]+) round.\"', body)
    latest_round = round_result.group(1) if round_result else None

    if amount and latest_round:
        return f"{amount} ({latest_round})"

    return amount or latest_round
