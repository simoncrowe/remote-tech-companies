from company_data import RemotePolicy
from helpers import scrape

name = 'Zerion'
business = 'Crypto Wallet'


def remote_policy():
    '''A job spec, which describes the engineering team as fully remote'''
    url = 'https://jobs.lever.co/zerion/6a66e7d7-440f-4fba-94f9-566cb4b7757e'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional and seemingly global remote jobs'''
    url = 'https://jobs.lever.co/zerion'
    return 'CIS, global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.com/Overview/Working-at-Zerion-Software-EI_IE271496.11,26.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Zerion-Engineering-Reviews-EI_IE3325248.0,6_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/Zerion-Software-Software-Engineer-Salaries-E271496_DAO.htm?filter.jobTitleExact=Software+Engineer%28%29'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/zerion'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
