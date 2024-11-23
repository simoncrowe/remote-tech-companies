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
    url = 'https://zapier.com/jobs#job-openings'
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
    tech = 'python, js, django, postgres, redis, aws lambda'
    return tech, url


def salary():
    '''Senior Data Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Zapier-Senior-Data-Engineer-Salaries-E1196705_D_KO7,27.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/zapier'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
