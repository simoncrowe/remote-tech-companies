from company_data import RemotePolicy
from helpers import scrape

name = 'FINN'
business = 'Car Rental'


def remote_policy():
    '''Their jobs page, which lists some remote openings'''
    url = 'https://www.finn.auto/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.finn.auto/careers'
    return 'USA, EMEA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-FINN-EI_IE3098544.11,15.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/FINN-Engineering-Reviews-EI_IE3098544.0,4_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech from Tech Lead job spec'''
    url = 'https://jobs.lever.co/finn.auto/7549b914-e410-445a-be83-b3e14d8d85ab'
    tech = 'js, typescript, python, go, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/FINN-Senior-Software-Engineer-Salaries-E3098544_D_KO5,29.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/finn'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
