from company_data import RemotePolicy
from helpers import scrape

name = 'Lokalise'
business = 'Language Localisation'


def remote_policy():
    '''Their careers page describes them as 100% remote'''
    url = 'https://lokalise.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://lokalise.com/careers'
    return 'europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Lokalise-EI_IE3398432.11,19.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Lokalise-Engineering-Reviews-EI_IE3398432.0,8_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/localize/localize-stack'
    tech = 'js, mongodb, redis, aws'
    return tech, url


salary = 'unknown'
