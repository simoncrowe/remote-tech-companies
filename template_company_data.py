from company_data import RemotePolicy
from helpers import scrape

name = ''
business = ''


def remote_policy():
    '''Their careers page, which says they support a hybrid working model'''
    url = ''
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = ''
    return 'APAC, EMEA, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = ''
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = ''
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = ''
    tech = ''
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = ''
    return scrape.glassdoor_salary(url), url
