from company_data import RemotePolicy
from helpers import scrape

name = 'Giant Digital'
business = 'Digital Agency'


def remote_policy():
    '''Their careers page, which says they are a 'fully remote team' '''
    url = 'https://www.giantdigital.co.uk/careers/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.giantdigital.co.uk/careers/'
    return 'UK', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Giant-Digital-Reviews-E2261728.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Giant-Digital-Engineering-Reviews-EI_IE2261728.0,13_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Giant-Digital-Software-Engineer-Salaries-E2261728_D_KO14,31.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Tech listed on their careers page'''
    url = 'https://www.giantdigital.co.uk/careers/'
    tech = 'python, django, aws'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/giant-digital'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
