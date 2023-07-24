from company_data import RemotePolicy
from helpers import scrape

name = 'Redoc'
business = 'Healthcare Data'


def remote_policy():
    '''A blog post that mentions that employs can work from anywhere in the US'''
    url = 'https://www.redoxengine.com/blog/people-everywhere/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.redoxengine.com/company/careers/current-openings/'
    return 'USA', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Redox-Inc-Engineering-Reviews-EI_IE1266986.0,9_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Redox-Inc-EI_IE1266986.11,20.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of tech from stackshare.io'''
    url = 'https://stackshare.io/redox-engine/redox-engine'
    tech = 'python, js, redis, postgres, kafka, k8s, aws'
    return tech, url


def salary():
    '''Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/Redox-Inc-Software-Engineer-Salaries-E1266986_D_KO10,27.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/redox'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
