from company_data import RemotePolicy
from helpers import scrape

name = 'Six Feet Up'
business = 'Software Consultancy'


def remote_policy():
    '''Their careers page, which describes them as 100% virtual'''
    url = 'https://sixfeetup.com/company/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://sixfeetup.com/company/careers#open-positions'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.com/Overview/Working-at-Six-Feet-Up-EI_IE1466623.11,22.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.com/Reviews/Six-Feet-Up-Engineering-Reviews-EI_IE1466623.0,11_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Tech Lead job spec'''
    url = 'https://sixfeetup.com/company/tech-lead-and-system-architect'
    tech = 'python, docker'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.levels.fyi/companies/six-feet-up/salaries/software-engineer'
    return scrape.levels_salary(url), url
