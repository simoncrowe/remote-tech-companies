from company_data import RemotePolicy
from helpers import scrape

name = 'Prisma'
business = 'Data Access'


def remote_policy():
    '''Their career page, which mentions working from anywhere'''
    url = 'https://www.prisma.io/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.prisma.io/careers'
    return 'global (GMT -6 to GMT +3)', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Prisma-Data-EI_IE2431237.11,22.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Prisma-Data-Engineering-Reviews-EI_IE2431237.0,11_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from himalayas.io'''
    url = 'https://himalayas.app/companies/prisma/tech-stack'
    tech = 'js, typescript, rust, next.js, react, aws'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/prisma'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
