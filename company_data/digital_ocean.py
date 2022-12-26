from company_data import RemotePolicy
from helpers import scrape

name = 'DigitalOcean'
business = 'Cloud'


def remote_policy():
    '''Their careers page which describes them as remote-first'''
    url = 'https://www.digitalocean.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.digitalocean.com/careers#anchor--current-openings'
    return 'Europe, Americas, APAC', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-DigitalOcean-EI_IE823482.11,23.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/DigitalOcean-Engineering-Reviews-EI_IE823482.0,12_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/digitalocean/digitalocean'
    tech = 'go, ruby, rails, redis, mysql, nginx, k8s'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/AbstractOps-Software-Engineer-Salaries-E6885566_D_KO12,29.htm'
    return scrape.glassdoor_salary(url), url
