from company_data import RemotePolicy
from helpers import scrape

name = 'Audiense'
business = 'Data Mining'


def remote_policy():
    '''Their careers page, which suggests that they offer 'the freedom to work from any location' '''
    url = 'https://www.audiense.com/jobs/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.audiense.com/jobs/careers'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Audiense-Reviews-E1367395.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Audiense-Engineering-Reviews-EI_IE1367395.0,8_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Salary Range from Software Engineer job spec'''
    url = 'https://www.audiense.com/jobs/product-developer'
    return '40K-60K€', url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://www.audiense.com/jobs/product-developer'
    tech = 'node.js, react, mongodb, mysql, rabbitmq, redis, docker, aws'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/audiense'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
