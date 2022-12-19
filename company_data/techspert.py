from company_data import RemotePolicy
from helpers import scrape

name = 'Techspert'
business = 'Expert Consultation'


def remote_policy():
    '''Their careers page, which says all their roles have significant scope to work from home'''
    url = 'https://careers.techspert.com/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://careers.techspert.com/'
    return 'England', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Techspert-io-EI_IE3050042.11,23.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Techspert.io-Engineering-Reviews-EI_IE3050042.0,12_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Research Engineer job spec'''
    url = 'https://careers.techspert.com/o/research-engineer'
    tech = 'python, numpy, pandas, scipy'
    return tech, url


def salary():
    '''Software Developer job based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Techspert-io-Software-Developer-Salaries-E3050042_D_KO13,31.htm'
    return scrape.glassdoor_salary(url), url
