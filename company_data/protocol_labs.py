from company_data import RemotePolicy
from helpers import scrape

name = 'Protocol Labs'
business = 'P2P Software'


def remote_policy():
    '''A blog post describing their remote culture'''
    url = 'https://protocol.ai/blog/how-we-work-at-protocol-labs/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://boards.greenhouse.io/protocollabs'
    return 'global', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Protocol-Labs-Engineering-Reviews-EI_IE3245538.0,13_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Protocol-Labs-EI_IE3245538.11,24.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Top from their github profile'''
    url = 'https://github.com/protocol'
    tech = 'js, go, typescript, jupyter notebook, shell'
    return tech, url


def salary():
    '''Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/Protocol-Labs-Senior-Software-Engineer-Salaries-E3245538_D_KO14,38.htm'
    return scrape.glassdoor_salary(url), url
