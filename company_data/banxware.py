from company_data import RemotePolicy
from helpers import scrape

name = 'Banxware'
business = 'Fintech'


def remote_policy():
    '''Job spec citing possibility of fully remote work'''
    url = 'https://join.com/companies/banxware/6626410-senior-backend-engineer-f-m-d'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://join.com/companies/banxware'
    return 'Europe?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Banxware-EI_IE5293622.11,19.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Banxware-Engineering-Reviews-EI_IE5293622.0,8_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Senior Software Engineer job spec'''
    url = 'https://join.com/companies/banxware/6626410-senior-backend-engineer-f-m-d'
    tech = 'ruby, k8s, aws'
    return tech, url


salary = 'unknown'


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/banxware'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
