import re

import requests

from helpers import add


@add.random_user_agent
def glassdoor_rating(company_profile_url, user_agent):
    headers = {'User-Agent': user_agent}
    print(f'Scraping rating from {company_profile_url}')
    response = requests.get(company_profile_url, headers=headers)
    body = response.content.decode()
    result = re.search(r'ratingValue.*([0-5]\.[0-9]+)"', body)
    ave_rating = result.group(1)
    print(f'Found rating: {ave_rating}')
    return ave_rating


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
        if 'salaries are hidden until we collect enough submissions' in body:
            print('Not enough data to get salary right now')
            return 'unknown'
        else:
            raise
