from company_data import RemotePolicy
from helpers import scrape

name = 'castLabs'
business = 'Video Streaming'


def remote_policy():
    '''Their careers page, which mentions remote work possibilities'''
    url = 'https://castlabs.com/careers/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for some regional remote jobs'''
    url = 'https://boards.eu.greenhouse.io/castlabs'
    return 'Americas, Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.com/Overview/Working-at-castLabs-EI_IE1005921.11,19.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.com/Reviews/castLabs-Engineering-Reviews-EI_IE1005921.0,8_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Developer job spec'''
    url = 'https://boards.eu.greenhouse.io/castlabs/jobs/4101284101'
    tech = 'js, python, django, aws'
    return tech, url
