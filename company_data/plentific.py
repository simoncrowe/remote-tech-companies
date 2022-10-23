from company_data import RemotePolicy
from helpers import scrape

name = 'Plentific'
business = 'Property'


def remote_policy():
    '''A job spec that states that job CAN BE fully remote in the UK'''
    url = 'https://apply.workable.com/plentific/j/5738E00A6D/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.plentific.com/en-gb/careers#careers'
    return 'Europe, Turkey', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Plentific-Engineering-Reviews-EI_IE966007.0,9_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Plentific-EI_IE966007.11,20.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Tech listed on various software engineering job specs'''
    url = 'https://www.plentific.com/en-gb/careers#careers'
    tech = 'python, js, c#, django, react'
    return tech, url


def salary():
    '''Salary range for the Software Engineer title, based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Plentific-Software-Engineer-Salaries-E966007_D_KO10,27.htm'
    return scrape.glassdoor_salary(url), url
