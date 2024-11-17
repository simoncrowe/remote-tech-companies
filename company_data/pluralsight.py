from company_data import RemotePolicy
from helpers import scrape

name = 'Pluralsight'
business = 'EdTech'


def remote_policy():
    '''Their careers page, which says they're remote-friendly'''
    url = 'https://www.pluralsight.com/careers'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://pluralsight.wd1.myworkdayjobs.com/en-US/Careers/'
    return 'USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Pluralsight-EI_IE672636.11,22.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Pluralsight-Engineering-Reviews-EI_IE672636.0,11_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/pluralsight/pluralsight'
    tech = 'c#, node.js, typescript, ruby, js, react, rails, postgres, redis, rabbitmq, kafka, k8s, aws'
    return tech, url


def salary():
    '''Software Engineer based in USA'''
    url = 'https://www.levels.fyi/companies/pluralsight/salaries/software-engineer/levels/p4'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/pluralsight'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
