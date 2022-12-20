from company_data import RemotePolicy
from helpers import scrape

name = 'Cleo'
business = 'Personal Finances'


def remote_policy():
    '''A job spec that encourages some office time for remote workers'''
    url = 'https://boards.greenhouse.io/cleoai/jobs/6481990002'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://web.meetcleo.com/careers'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Cleo-United-Kingdom-EI_IE2204277.11,30.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Cleo-(United-Kingdom)-Engineering-Reviews-EI_IE2204277.0,21_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selection of tech from himalayas.app'''
    url = 'https://himalayas.app/companies/cleo/tech-stack'
    tech = 'ruby, js, rails, react'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Cleo-United-Kingdom-Senior-Software-Engineer-Salaries-E2204277_D_KO20,44.htm'
    return scrape.glassdoor_salary(url), url
