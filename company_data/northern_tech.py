from company_data import RemotePolicy
from helpers import scrape

name = 'Northern Tech'
business = 'IoT'


def remote_policy():
    '''Their careers page, which lists many jobs with remote options'''
    url = 'https://northern.tech/careers'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://northern.tech/careers'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Northern-tech-Reviews-E3109156.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Northern.tech-Engineering-Reviews-EI_IE3109156.0,13_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech mentioned on software engineer job spec'''
    url = 'https://northern.tech/careers/open-positions/frontend-developer-backend-experience'
    tech = 'go, python, mongodb'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/northern-tech'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
