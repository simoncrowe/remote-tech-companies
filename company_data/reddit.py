from company_data import RemotePolicy
from helpers import scrape

name = 'Reddit'
business = 'Social Media'


def remote_policy():
    '''Job listings with some remote options'''
    url = 'https://boards.greenhouse.io/reddit'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://boards.greenhouse.io/reddit'
    return 'Americas, APAC, EMEA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Reddit-EI_IE796358.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Reddit-Engineering-Reviews-EI_IE796358.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/reddit/reddit'
    tech = 'python, js, flask, postgres, redis, nginx, aws'
    return tech, url


def salary():
    '''Software Engineer III based in USA'''
    url = 'https://www.levels.fyi/companies/reddit/salaries/software-engineer/levels/ic3'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/reddit'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
