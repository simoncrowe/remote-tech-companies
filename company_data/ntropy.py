from company_data import RemotePolicy
from helpers import scrape

name = 'Ntropy'
business = 'Financial Data'


def remote_policy():
    '''Their careers page which describes their team as global'''
    url = 'https://ntropy.com/company/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://ntropy.com/company/careers'
    return 'global (GMT-7 to GMT+1)', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.com/Overview/Working-at-Ntropy-EI_IE5382890.11,17.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://jobs.lever.co/ntropy-network/5a587b64-7f97-4d75-be47-acf6394ed936'
    tech = 'python, rust, pytorch, k8s, aws, gcp'
    return tech, url


def salary():
    '''Salary on Software Engineer job spec'''
    url = 'https://jobs.lever.co/ntropy-network/5a587b64-7f97-4d75-be47-acf6394ed936'
    return '$120k', url
