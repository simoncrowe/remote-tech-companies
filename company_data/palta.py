from company_data import RemotePolicy
from helpers import scrape

name = 'Palta'
business = 'Health'


def remote_policy():
    '''Listings for some remote jobs'''
    url = 'https://palta.com/jobs'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for remote jobs'''
    url = 'https://palta.com/jobs'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Palta-EI_IE6042331.11,16.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Palta-Engineering-Reviews-EI_IE6042331.0,5_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on their careers page'''
    url = 'https://palta.com/careers'
    tech = 'python, scala, kotlin, swift, terraform, aws'
    return tech, url


def salary():
    '''No information at present'''
    url = 'https://www.glassdoor.co.uk/Salary/Palta-Salaries-E6042331.htm'
    return 'unknown', url
