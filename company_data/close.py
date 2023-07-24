from company_data import RemotePolicy
from helpers import scrape

name = 'Close'
business = 'CRM'


def remote_policy():
    '''BLog post about their remote culture'''
    url = 'https://blog.close.com/remote-team-culture/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''https://www.close.com/careers'''
    url = 'https://www.close.com/careers'
    return 'Americas, EMEA', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Close-Engineering-Reviews-EI_IE1155591.0,5_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Close-EI_IE1155591.11,16.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of tech from stackshare.io'''
    url = 'https://stackshare.io/close-crm/close'
    tech = 'python, flask, js, react, lua, postgres, redis, aws, k8s'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/Close-Senior-Software-Engineer-Salaries-E1155591_D_KO6,30.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/close'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
