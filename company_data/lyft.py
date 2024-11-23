from company_data import RemotePolicy
from helpers import scrape

name = 'Lyft'
business = 'ride-hailing'


def remote_policy():
    '''A blog post which says they are a fully flexible workspace'''
    url = 'https://www.lyft.com/blog/posts/lyft-announces-fully-flexible-workplace'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.lyft.com/careers#openings'
    return 'Europe, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Lyft-EI_IE700614.11,15.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Lyft-Engineering-Reviews-EI_IE700614.0,4_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Lyft-Software-Engineer-Salaries-E700614_D_KO5,22.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/lyft/lyft'
    tech = 'java, swift, c++, php, go, js, python, flask, redis, mongodb, docker, aws'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/lyft'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
