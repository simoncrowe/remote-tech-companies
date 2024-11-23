from company_data import RemotePolicy
from helpers import scrape

name = 'Okta'
business = 'IAM'


def remote_policy():
    '''Their careers page, which says lists some remote roles'''
    url = 'https://www.okta.com/uk/company/careers/?department=All&location=All'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.okta.com/uk/company/careers/?department=All&location=All'
    return 'Europe, Americas, APAC', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Okta-Reviews-E444756.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Okta-Engineering-Reviews-EI_IE444756.0,4_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Staff Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Okta-Staff-Engineer-Salaries-E444756_D_KO5,19.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/okta/okta'
    tech = 'js, java, c#, ruby, redis, mysql, nginx, docker, aws'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/okta'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
