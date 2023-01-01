from company_data import RemotePolicy
from helpers import scrape

name = 'AWeber'
business = 'Email Marketing'


def remote_policy():
    '''Their careers page, which says they are 100% remote'''
    url = 'https://www.aweber.com/careers.htm'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.aweber.com/careers.htm#careers'
    return 'USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-AWeber-EI_IE722170.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/AWeber-Engineering-Reviews-EI_IE722170.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech mentioned on Backend Software Engineer job spec'''
    url = 'https://www.aweber.com/careers-application.htm?gh_jid=4331044'
    tech = 'python, tornado, docker, k8s'
    return tech, url


def salary():
    '''Software Engineer'''
    url = 'https://www.levels.fyi/companies/aweber/salaries/software-engineer'
    return scrape.levels_salary(url), url
