from company_data import RemotePolicy
from helpers import scrape

name = 'InVision'
business = 'Visual Collaboration'


def remote_policy():
    '''Their careers page, which describes them as remote-first'''
    url = 'https://www.invisionapp.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://www.invisionapp.com/careers'
    return 'global', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/InVision-Engineering-Reviews-EI_IE912781.0,8_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-InVision-EI_IE912781.11,19.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of tech from stackshare.io'''
    url = 'https://stackshare.io/invisionapp/invisionapp'
    tech = 'js, react, angular, postgres, kafka, k8s, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/InVision-Senior-Software-Engineer-Salaries-E912781_D_KO9,33.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/invision'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
