from company_data import RemotePolicy
from helpers import scrape

name = 'Phaidra'
business = 'AI ICS'


def remote_policy():
    '''Their job board page, which describes them as 100% remote'''
    url = 'https://boards.greenhouse.io/phaidra'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://boards.greenhouse.io/phaidra'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.com/Overview/Working-at-Phaidra-EI_IE6977699.11,18.htm'
    return scrape.glassdoor_rating(url), url


engineering_glassdoor_rating = 'unknown'


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/phaidra-inc/tech-stack'
    tech = 'js, python, flask, graphql, grpc, k8s terraform, gcp'''
    return tech, url


def salary():
    '''UK salary range from Software Engineer job spec'''
    url = 'https://boards.greenhouse.io/phaidra/jobs/4250393005'
    return '£82,000-£105,000', url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/phaidra'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
