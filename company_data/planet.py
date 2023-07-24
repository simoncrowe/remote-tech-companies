from company_data import RemotePolicy
from helpers import scrape

name = 'Planet'
business = 'Satellite Imaging'


def remote_policy():
    '''Article about their remote hiring'''
    url = 'https://www.planet.com/pulse/making-space-for-everyone-how-planet-is-building-a-global-workforce/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.planet.com/company/careers/'
    return 'APAC, Americas, EMEA', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Planet-Engineering-Reviews-EI_IE827495.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Planet-EI_IE827495.11,17.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of the tech listed on himalayas.app'''
    url = 'https://himalayas.app/companies/planet/tech-stack'
    tech = 'js, python, go, c++, c, postgres, mysql, nginx,  ansible, terraform, k8s'
    return tech, url


def salary():
    '''L4 Software Engineer in USA'''
    url = 'https://www.levels.fyi/companies/planet/salaries/software-engineer'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/planet'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
