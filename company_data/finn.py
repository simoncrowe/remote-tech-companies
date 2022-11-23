from company_data import RemotePolicy
from helpers import scrape

name = 'FINN'
business = 'Car Rental'


def remote_policy():
    '''Their jobs page, which lists some remote openings'''
    url = 'https://www.finn.auto/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.finn.auto/careers'
    return 'USA, EMEA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-FINN-EI_IE3098544.11,15.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/FINN-Engineering-Reviews-EI_IE3098544.0,4_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/finn/tech-stack'
    tech = 'python, fo, js, typescript, google bigquery, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/FINN-Senior-Software-Engineer-Salaries-E3098544_D_KO5,29.htm'
    return scrape.glassdoor_salary(url), url
