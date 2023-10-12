from company_data import RemotePolicy
from helpers import scrape

name = 'TheoremOne'
business = 'Software Consultancy'


def remote_policy():
    '''Their careers page, which describes them as remote-first'''
    url = 'https://www.theoremone.co/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://jobs.lever.co/theoremonellc'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-TheoremOne-EI_IE960344.11,21.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/TheoremOne-Engineering-Reviews-EI_IE960344.0,10_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed in job descriptions'''
    url = 'https://jobs.lever.co/theoremonellc'
    tech = 'c#, ruby, js, react'
    return tech, url


def salary():
    '''Software Engineer Salaries'''
    url = 'https://www.levels.fyi/companies/theoremone/salaries/software-engineer'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/theorem-co'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
