from company_data import RemotePolicy
from helpers import scrape

name = 'HubSpot'
business = 'CRM'


def remote_policy():
    '''A blog post discussing their hybrid remote policy'''
    url = 'https://www.hubspot.com/careers-blog/future-of-work-hybrid'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.hubspot.com/careers/jobs'
    return 'APAC, Europe, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/HubSpot-Reviews-E227605.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/HubSpot-Engineering-Reviews-EI_IE227605.0,7_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.co.uk/Salary/HubSpot-Software-Engineer-Salaries-E227605_D_KO8,25.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/hubspot/hubspot'
    tech = 'js, java, swift, mysql, kafka, nginx, k8s'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/hubspot'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
