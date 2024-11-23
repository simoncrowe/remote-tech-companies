from company_data import RemotePolicy
from helpers import scrape

name = 'YouGov'
business = 'Market Research'


def remote_policy():
    '''A job spec that describes the role as 100% remote'''
    url = 'https://www.smartrecruiters.com/YouGov1/743999854006581?trid=aa693c38-1e61-49d8-ad06-09c4623c7dcb'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://jobs.yougov.com/jobs'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-YouGov-EI_IE518089.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/YouGov-Engineering-Reviews-EI_IE518089.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech in software engineer job titles'''
    url = 'https://jobs.yougov.com/jobs'
    tech = 'python, javascript'
    return tech, url


def salary():
    '''Software Engineer based in Europe'''
    url = 'https://www.glassdoor.co.uk/Salary/YouGov-Senior-Python-Engineer-Salaries-E518089_D_KO7,29.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/yougov'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
