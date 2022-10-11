from company_data import RemotePolicy
from helpers import scrape

name = 'Zapier'
business = 'Automation'


def remote_policy():
    '''Blog post about their fully-remote origins'''
    url = 'https://zapier.com/blog/why-work-remotely/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global and regional remote jobs'''
    url = 'https://aiven.io/careers/job'
    return 'global', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Zapier-Engineering-Reviews-EI_IE1196705.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Zapier-EI_IE1196705.11,17.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of tech from stackshare.io'''
    url = 'https://stackshare.io/zapier/zapier'
    tech = 'python, javascript, django, postgres, redis, aws lambda'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.com/Salary/Zapier-Software-Engineer-Salaries-E1196705_D_KO7,24.htm'
    return scrape.glassdoor_salary(url), url
