from company_data import RemotePolicy
from helpers import scrape

name = 'Anaconda'
business = 'Data Science'


def remote_policy():
    '''Their career page, which lists remote jobs'''
    url = 'https://www.anaconda.com/careers'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.anaconda.com/careers#jobs'
    return 'US, Canada, Germany, UK', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Anaconda-Engineering-Reviews-EI_IE983617.0,8_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Anaconda-EI_IE983617.11,19.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Tech taken from Senior Full Stack Software Engineer job spec'''
    url = 'https://boards.greenhouse.io/anaconda/jobs/4260312'
    tech = 'python, js, mongodb, docker, k8s, fastapi'
    return tech, url


def salary():
    '''Median Software Engineer salary'''
    url = 'https://www.levels.fyi/companies/anaconda/salaries/software-engineer'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/continuum-analytics'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
