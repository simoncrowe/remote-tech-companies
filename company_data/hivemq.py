from company_data import RemotePolicy
from helpers import scrape

name = 'HiveMQ'
business = 'Message Broker'


def remote_policy():
    '''A job spec that describes them as a global, remote-first company'''
    url = 'https://www.hivemq.com/jobs/?gh_jid=4086583101'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.hivemq.com/jobs/'
    return 'Europe, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-HiveMQ-EI_IE2931156.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/HiveMQ-Engineering-Reviews-EI_IE2931156.0,6_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on github profile'''
    url = 'https://github.com/hivemq'
    tech = 'java, shell, js, ruby, c'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.levels.fyi/companies/hive/salaries/software-engineer'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/hivemq'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
