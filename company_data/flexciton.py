from company_data import RemotePolicy
from helpers import scrape

name = 'Flexciton'
business = 'Semiconductors'


def remote_policy():
    '''Their jobs page, which lists hybrid and fully remote jobs'''
    url = 'https://careers.flexciton.com/en/jobs'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://careers.flexciton.com/en/jobs'
    return 'England?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Flexciton-EI_IE1901293.11,20.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Flexciton-Engineering-Reviews-EI_IE1901293.0,9_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://careers.flexciton.com/jobs/2182354-staff-software-engineer-python'
    tech = 'js, angular, python, flask, sqlalchemy, rabbitmq, postgres, k8s, azure'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Flexciton-Senior-Software-Engineer-Salaries-E1901293_D_KO10,34.htm'
    return scrape.glassdoor_salary(url), url
