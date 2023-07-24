from company_data import RemotePolicy
from helpers import scrape

name = 'Pento'
business = 'Payroll'


def remote_policy():
    '''A blog post that describes the company as remote-first'''
    url = 'https://humaans.io/blog/how-pento-uses-humaans-to-scale-a-great-remote-first-employee-experience/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://jobs.lever.co/pento'
    return 'EMEA', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Pento-Engineering-Reviews-EI_IE6534062.0,5_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Pento-EI_IE6534062.11,16.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Selection of tech from stackshare.io'''
    url = 'https://stackshare.io/pento/pento'
    tech = 'go, js, postgres, nginx, docker, k8s'
    return tech, url


def salary():
    '''No data (2022-10-22)'''
    url = 'https://www.google.com/search?q=pento+software+engineer+salary&oq=pento+software+engineer+salary'
    return 'unknown', url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/pento'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
