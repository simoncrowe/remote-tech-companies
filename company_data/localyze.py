from company_data import RemotePolicy
from helpers import scrape

name = 'Localyze'
business = 'Remote HR'


def remote_policy():
    '''A blog post describing their remote culture'''
    url = 'https://www.localyze.com/post/work-and-location-policy-at-localyze'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.localyze.com/careers'
    return 'Europe, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Localyze-EI_IE5377470.11,19.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Localyze-Engineering-Reviews-EI_IE5377470.0,8_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


tech_stack = 'unknown'


salary = 'unknown'


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/localyze'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
