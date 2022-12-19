from company_data import RemotePolicy
from helpers import scrape

name = 'Ravio'
business = 'Compensation Data'


def remote_policy():
    '''A job spec that cites the possibility of working remotely in the UK'''
    url = 'https://jobs.ashbyhq.com/Ravio/983f199f-e21e-49a2-be44-4082dfb92333'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://jobs.ashbyhq.com/Ravio'
    return 'England', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Ravio-EI_IE7330915.11,16.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Jobs/Ravio-Engineering-Jobs-EI_IE7330915.0,5_DEPT1007.htm?filter.countryId=null'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://jobs.ashbyhq.com/Ravio/983f199f-e21e-49a2-be44-4082dfb92333'
    tech = 'js, nodejs, postgres'
    return tech, url


salary = 'unknown'
