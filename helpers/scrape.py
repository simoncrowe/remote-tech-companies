import re

import requests

from helpers import add


@add.random_user_agent
def glassdoor_rating(company_profile_url, user_agent):
    headers = {'User-Agent': user_agent}
    response = requests.get(company_profile_url, headers=headers)
    body = response.content.decode()
    result = re.search(r'ratingValue.*([0-4]\.[0-9]+)"', body)
    return result.group(1)


@add.random_user_agent
def glassdoor_salary_range(salary_info_url, user_agent):
    headers = {'User-Agent': user_agent}
    response = requests.get(salary_info_url, headers=headers)
    body = response.content.decode()
    result = re.search(r'[£\$][0-9,]+\s-\s[\$£][0-9\,]+', body)
    return result.group(0)
