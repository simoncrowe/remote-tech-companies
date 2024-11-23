from company_data import RemotePolicy
from helpers import scrape

name = 'Affirm'
business = 'Fintech'


def remote_policy():
    '''Their careers page, which describes them as remote-first'''
    url = 'https://www.affirm.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.affirm.com/careers'
    return 'Europe, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Affirm-EI_IE823564.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Affirm-Engineering-Reviews-EI_IE823564.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/affirm/affirm'
    tech = 'js, lua, ruby, kotlin, swift, java, python, flask, airflow, nginx, redis, mysql, docker, aws'
    return tech, url


def salary():
    '''Software Engineer II based in USA'''
    url = 'https://www.levels.fyi/companies/affirm/salaries/software-engineer/levels/l5'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/affirm'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
