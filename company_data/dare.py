from company_data import RemotePolicy
from helpers import scrape

name = 'Dare'
business = 'Energy Trading'


def remote_policy():
    '''Their careers page, which lists some fully remote jobs'''
    url = 'https://careers.dare.global/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://careers.dare.global/jobs'
    return 'UK, Germany', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Dare-International-EI_IE6357593.11,29.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Dare-International-Engineering-Reviews-EI_IE6357593.0,18_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech mentioned on Senior Software Engineer job spec'''
    url = 'https://careers.dare.global/jobs/1484999-senior-software-engineer'
    tech = 'python, go'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/dare'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
