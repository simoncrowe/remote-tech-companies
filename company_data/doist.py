from company_data import RemotePolicy
from helpers import scrape

name = 'Doist'
business = 'Productivity'


def remote_policy():
    '''Their careers page, which says "Doisters can work from anywhere in the world"'''
    url = 'https://doist.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://doist.com/careers'
    return 'global', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Doist-Reviews-E1102553.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Doist-Engineering-Reviews-EI_IE1102553.0,5_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.levels.fyi/companies/doist/salaries/software-engineer'
    return scrape.levels_salary(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/doist/tech-stack'
    tech = 'python, java, php, kotlin, js, react, aws'
    return tech, url
