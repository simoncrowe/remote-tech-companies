from company_data import RemotePolicy
from helpers import scrape

name = 'Adeva'
business = 'Remote HR'


def remote_policy():
    '''Their careers page, which says they're fully remote'''
    url = 'https://adevait.com/careers/job-openings'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://adevait.com/careers/job-openings'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Adeva-Reviews-E1401684.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Adeva-Engineering-Reviews-EI_IE1401684.0,5_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/adeva/tech-stack'
    tech = 'kotlin, scala, swift, php, typescript, symfony, postgres, aws, gcp'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/adeva'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
