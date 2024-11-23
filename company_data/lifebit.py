from company_data import RemotePolicy
from helpers import scrape

name = 'Lifebit'
business = 'Medtech'


def remote_policy():
    '''Their careers page, which claims employees are able to work fully remote from anywhere'''
    url = 'https://www.lifebit.ai/careers/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://apply.workable.com/lifebit-biotech-ltd/'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Lifebit-EI_IE3969764.11,18.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Lifebit-Engineering-Reviews-EI_IE3969764.0,7_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://apply.workable.com/lifebit-biotech-ltd/j/A1D7FFCC7A/'
    tech = 'js, typescript, python, react, redux, mongodb, k8s, terraform, aws'
    return tech, url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Lifebit-Software-Engineer-Salaries-E3969764_D_KO8,25.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/lifebit'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
