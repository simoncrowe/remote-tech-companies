from company_data import RemotePolicy
from helpers import scrape

name = 'Elastic'
business = 'Search & Observability'


def remote_policy():
    '''Their careers page, which says they support hybrid and remote'''
    url = 'https://www.elastic.co/careers'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://jobs.elastic.co/jobs/department/engineering?size=n_20_n'
    return 'global', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Elastic-EI_IE751551.11,18.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Elastic-Reviews-E751551.htm?filter.jobFunction=1007'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in the UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Elastic-Senior-Software-Engineer-Salaries-E751551_D_KO8,32.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Top languages from Elastic's Github org profile'''
    url = 'https://github.com/elastic'
    tech = 'go, js, python, java'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/elasticsearch'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
