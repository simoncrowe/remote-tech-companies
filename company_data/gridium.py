from company_data import RemotePolicy
from helpers import scrape

name = 'Gridium'
business = 'Building Decarbonisation'


def remote_policy():
    '''Their careers page, which says they are a 'distributed team' '''
    url = 'https://gridium.com/about/working-at-gridium/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://gridium.com/about/working-at-gridium/'
    return 'USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Gridium-Reviews-E695849.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Gridium-Engineering-Reviews-EI_IE695849.0,7_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/gridium/tech-stack'
    tech = 'python, js, php, postgres, nginx, aws'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/gridium'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
