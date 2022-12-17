from company_data import RemotePolicy
from helpers import scrape

name = 'Hofy'
business = 'Remote HR'


def remote_policy():
    '''Their careers page, which lists office-based and remote jobs'''
    url = 'https://www.hofy.com/careers'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.hofy.com/careers'
    return 'GMT +/-3hrs', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Hofy-EI_IE5411167.11,15.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Hofy-Engineering-Reviews-EI_IE5411167.0,4_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/hofy/tech-stack'
    tech = 'js, typescript, react, go, nginx, aws'
    return tech, url


def salary():
    '''Old Senior Software Engineer job spec'''
    url = 'https://cord.co/u/hofy/jobs/14295-senior-software-engineer'
    return '£75,000 - £95,000', url
