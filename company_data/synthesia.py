from company_data import RemotePolicy
from helpers import scrape

name = 'Synthesia'
business = 'Generative AI'


def remote_policy():
    '''Their careers page, which describes them as remote-friendly'''
    url = 'https://www.synthesia.io/careers'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.synthesia.io/careers#jobs'
    return 'Europe, USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Synthesia-EI_IE4421112.11,20.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Synthesia-Engineering-Reviews-EI_IE4421112.0,9_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://boards.eu.greenhouse.io/synthesia/jobs/4094596101?gh_jid=4094596101'
    tech = 'python, typescript, c++, flask, react, redux, docker, aws'
    return tech, url


def salary():
    '''Senior Software Engineer salary range based on job spec'''
    url = 'https://boards.eu.greenhouse.io/synthesia/jobs/4094596101?gh_jid=4094596101'
    return '€70-110k', url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/synthesia'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
