from company_data import RemotePolicy
from helpers import scrape

name = 'Cohere'
business = 'NLP'


def remote_policy():
    '''Their careers page describes them as remote-first'''
    url = 'https://cohere.ai/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://jobs.lever.co/cohere/'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Cohere-EI_IE1779417.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Cohere-Engineering-Reviews-EI_IE1779417.0,6_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://jobs.lever.co/cohere/a400534c-8dd8-4535-9550-918ff180fd7a'
    tech = 'go'
    return tech, url


def salary():
    '''No information at present'''
    url = 'https://www.glassdoor.co.uk/Salary/Cohere-Salaries-E6413613.htm'
    return "unknown", url
