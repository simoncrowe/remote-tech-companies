from company_data import RemotePolicy
from helpers import scrape

name = 'PostHog'
business = 'Product Analytics'


def remote_policy():
    '''Their HR benefits page, which says they are fully remote'''
    url = 'https://posthog.com/handbook/people/benefits'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://posthog.com/careers'
    return 'Americas, APAC', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-PostHog-EI_IE4260520.11,18.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/PostHog-Reviews-E4260520.htm?filter.jobFunction=1007'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in the UK'''
    url = 'https://www.glassdoor.co.uk/Salary/PostHog-Senior-Software-Engineer-Salaries-E4260520_D_KO8,32.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from PostHog engineering handbook'''
    url = 'https://posthog.com/handbook/engineering/stack'
    tech = 'python, js, rust, postgres, react, django, celery, dagster, redis, kafka, clickhouse, aws, k8s'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/posthog'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
