from company_data import RemotePolicy
from helpers import scrape

name = 'Monzo'
business = 'Banking'


def remote_policy():
    '''Their careers page, which says they support distributed work'''
    url = 'https://monzo.com/careers#benefits'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://monzo.com/careers'
    return 'uk, ireland, spain', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Monzo-Bank-EI_IE1557148.11,21.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Monzo-Bank-Reviews-E1557148.htm?filter.jobFunction=1007'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.co.uk/Salary/Monzo-Bank-Senior-Software-Engineer-Salaries-E1557148_D_KO11,35.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/monzo/tech-stack'
    tech = 'js, go, k8s, react, kafka, cassandra, gcp'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/monzo'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
