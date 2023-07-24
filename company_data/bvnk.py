from company_data import RemotePolicy
from helpers import scrape

name = 'BVNK'
business = 'Crypto'


def remote_policy():
    '''Their careers page, which mentions remote and office-based work'''
    url = 'https://bvnk.com/life-at-bvnk'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://boards.eu.greenhouse.io/bvnk'
    return 'EMEA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-BVNK-EI_IE7236562.11,15.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/BVNK-Engineering-Reviews-EI_IE7236562.0,4_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://boards.eu.greenhouse.io/bvnk/jobs/4028998101'
    tech = 'java'
    return tech, url


salary = 'unknown'


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/bvnk'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
