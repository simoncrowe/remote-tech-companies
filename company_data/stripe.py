from company_data import RemotePolicy
from helpers import scrape

name = 'Stripe'
business = 'Fintech'


def remote_policy():
    '''A blog post citing that 22% of their engineers are remote'''
    url = 'https://stripe.com/blog/remote-hub-one-year'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://stripe.com/jobs/search'
    return 'APAC, Americas, EMEA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Stripe-EI_IE671932.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Stripe-Engineering-Reviews-EI_IE671932.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''A selection of tech from techstasks.io'''
    url = 'https://techstacks.io/stacks/stripe/'
    tech = 'rub, js, postgres, redis, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Stripe-Senior-Software-Engineer-Salaries-E671932_D_KO7,31.htm'
    return scrape.glassdoor_salary(url), url
