from company_data import RemotePolicy
from helpers import scrape

name = 'Qualio'
business = 'Quality Management'


def remote_policy():
    '''Their careers page, which describes them as 100% remote'''
    url = 'https://www.qualio.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.qualio.com/careers#open-roles'
    return 'EMEA, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Qualio-EI_IE2414909.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Qualio-Engineering-Reviews-EI_IE2414909.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Full Stack Developer job spec'''
    url = 'https://www.qualio.com/careers/job?gh_jid=5254313003'
    tech = 'python, js, docker, aws'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/qualio'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
