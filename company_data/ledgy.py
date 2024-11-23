from company_data import RemotePolicy
from helpers import scrape

name = 'Ledgy'
business = 'Fintech (Equity)'


def remote_policy():
    '''Their careers page, which mentions flexible and remote work'''
    url = 'https://ledgy.com/uk/careers/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://ledgy.com/uk/careers/'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Ledgy-EI_IE2406828.11,16.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Ledgy-Engineering-Reviews-EI_IE2406828.0,5_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://ledgy.com/uk/careers/4000985101'
    tech = 'js, typescript, mongodb, gcp'
    return tech, url


def salary():
    '''Salary range on old Senior Software Engineer job spec'''
    url = 'https://cord.co/u/ledgy/jobs/21087-senior-software-engineer-at-ledgy?%2Fjobs%2F10379-devops-lead-='
    return '£80,000 - £105,000', url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/ledgy'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
