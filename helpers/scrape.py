import re

import requests

from helpers import add


@add.random_user_agent
def glassdoor_rating(company_profile_url, user_agent):
    headers = {'User-Agent': user_agent}
    print(f'Scraping rating from {company_profile_url}')
    response = requests.get(company_profile_url, headers=headers)
    body = response.content.decode()
    result = re.search(r'ratingValue.*([0-4]\.[0-9]+)"', body)
    ave_rating = result.group(1)
    print(f'Found rating: {ave_rating}')
    return ave_rating


@add.random_user_agent
def glassdoor_engineering_rating(company_profile_url, user_agent):
    headers = {'User-Agent': user_agent}
    print(f'Scraping rating from {company_profile_url}')
    response = requests.get(company_profile_url, headers=headers)
    body = response.content.decode()
    result = re.search(r'title="([0-5]\.[0-9])"', body)
    ave_rating = result.group(1)
    print(f'Found rating: {ave_rating}')
    return ave_rating


@add.random_user_agent
def glassdoor_salary_range(salary_info_url, user_agent):
    headers = {'User-Agent': user_agent}
    print(f'Scraping salary from {salary_info_url}')
    response = requests.get(salary_info_url, headers=headers)
    body = response.content.decode()
    result = re.search(r'[£\$][0-9,]+\s-\s[\$£][0-9\,]+', body)
    salary_range = result.group(0)
    print(f'Found salary range: {salary_range}')
    return salary_range


@add.random_user_agent
def levels_salary(salary_info_url, user_agent):
    headers = {'User-Agent': user_agent}
    print(f'Scraping salary from {salary_info_url}')
    response = requests.get(salary_info_url, headers=headers)
    body = response.content.decode()
    result = re.search(r'The median Software Engineer compensation package at \w+ totals (\$[0-9]+K) per year', body)
    salary = result.group(1)
    print(f'Found salary: {salary}')
    return salary
