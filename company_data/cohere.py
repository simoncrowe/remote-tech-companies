from company_data import RemotePolicy
from helpers import scrape

name = 'Cohere'
business = 'NLP'


def remote_policy():
    '''Their careers page describes them as remote-first'''
    url = 'https://cohere.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://jobs.ashbyhq.com/cohere'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Cohere-EI_IE6413613.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Cohere-Reviews-E6413613.htm?filter.jobFunction=1007'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://jobs.ashbyhq.com/cohere/4dd749aa-a675-4430-98fb-6701c8e14ab6?employmentType=FullTime&locationId=9327eaae-1f4e-493c-9bab-4024d7afa54c&workplaceType=Remote'
    tech = 'python, go, kubernetes'
    return tech, url


def salary():
    '''Median Software Engineer salary'''
    url = 'https://www.levels.fyi/en-gb/companies/cohere/salaries/software-engineer?country=43'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/cohere-82b8'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
