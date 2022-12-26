from company_data import RemotePolicy
from helpers import scrape

name = 'TestGorilla'
business = 'Pre-hire Tests'


def remote_policy():
    '''Their careers page describes their team as global'''
    url = 'https://www.testgorilla.com/careers/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://www.testgorilla.com/careers/#jobs'
    return 'global', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-TestGorilla-EI_IE5216975.11,22.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/TestGorilla-Engineering-Reviews-EI_IE5216975.0,11_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/testgorilla/tech-stack'
    tech = 'js, angular, python, django, redis, k8s, ansible, terraform, aws'
    return tech, url
