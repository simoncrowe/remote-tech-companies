from company_data import RemotePolicy
from helpers import scrape

name = 'Airbyte'
business = 'Data Integration'


def remote_policy():
    '''Their careers page, which says they are Fully Remote'''
    url = 'https://airbyte.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://boards.greenhouse.io/airbyte'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Airbyte-CA-Reviews-E7651014.htm'
    return scrape.glassdoor_rating(url), url


def salary():
    '''Software Engineer based in USA'''
    url = 'https://www.levels.fyi/companies/airbyte/salaries/software-engineer'
    return scrape.levels_salary(url), url


def tech_stack():
    '''Selected tech from the Technical Stack section of their documentation'''
    url = 'https://docs.airbyte.com/understanding-airbyte/tech-stack/'
    tech = 'java, python, nodejs, typescript, react, postgres'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/airbyte'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
