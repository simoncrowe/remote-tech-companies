from company_data import RemotePolicy
from helpers import scrape

name = 'QuestDB'
business = 'Time-Series Database'


def remote_policy():
    '''Their careers page, which says they are 100% remote'''
    url = 'https://questdb.io/careers/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for possibly global remote jobs'''
    url = 'https://questdb.io/careers'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/QuestDB-Reviews-E3571431.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/QuestDB-Engineering-Reviews-EI_IE3571431.0,7_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/QuestDB-Software-Engineer-Salaries-E3571431_D_KO8,25.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech their Github profile'''
    url = 'https://github.com/orgs/questdb/repositories?q=&type=all&language=&sort=stargazers'
    tech = 'java, typescript, python, c++, go'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/questdb'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
