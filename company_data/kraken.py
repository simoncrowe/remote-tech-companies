from company_data import RemotePolicy
from helpers import scrape

name = 'Kraken'
business = 'Crypto Exchange'


def remote_policy():
    '''A blog post extolling the virtues of their remote culture'''
    url = 'https://blog.kraken.com/post/8360/kraken-leads-the-work-from-home-movement/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global and regional remote jobs'''
    url = 'https://jobs.lever.co/kraken?department=Engineering'
    return 'global', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Kraken-Digital-Asset-Exchange-Engineering-Reviews-EI_IE938667.0,29_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Kraken-Digital-Asset-Exchange-EI_IE938667.11,40.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of tech from himalayas.app'''
    url = 'https://himalayas.app/companies/kraken/tech-stack'
    tech = 'js, python, sql, k8s, gcp'
    return tech, url


def salary():
    '''Median Software Engineer salary'''
    url = 'https://www.levels.fyi/companies/kraken/salaries/software-engineer'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/kraken'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
