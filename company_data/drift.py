from company_data import RemotePolicy
from helpers import scrape

name = 'Drift'
business = 'Marketing'


def remote_policy():
    '''Their careers page, which says remote is the primary experience for all employees'''
    url = 'https://www.drift.com/about/careers'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.drift.com/about/careers/#openings'
    return 'APAC, EMEA, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Drift-Reviews-E1145026.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Drift-Engineering-Reviews-EI_IE1145026.0,5_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/drift-developer/driftt'
    tech = 'java, js, objective-c,i react, pug, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.levels.fyi/companies/drift/salaries/software-engineer'
    return scrape.levels_salary(url), url
