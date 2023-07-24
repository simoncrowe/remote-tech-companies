from company_data import RemotePolicy
from helpers import scrape

name = 'Pennylane'
business = 'Accounting'


def remote_policy():
    '''Their careers page, which describes them as remote-friendly'''
    url = 'https://www.pennylane.com/fr/careers/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.pennylane.com/fr/careers/#nos-offres'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Pennylane-France-EI_IE4171708.11,27.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Pennylane-(France)-Engineering-Reviews-EI_IE4171708.0,18_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://jobs.lever.co/pennylane/a493366a-16f8-4418-8bf3-dd1f7641685c'
    tech = 'ruby, rails, typescript, react, jest, aws'
    return tech, url


def salary():
    '''Software Engineer based in France'''
    url = 'https://www.glassdoor.com/Salary/Pennylane-France-Software-Engineer-Paris-Salaries-EJI_IE4171708.0,16_KO17,34_IL.35,40_IM1080.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/pennylane'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
