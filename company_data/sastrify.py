from company_data import RemotePolicy
from helpers import scrape

name = 'Sastrify'
business = 'SaaS procurement'


def remote_policy():
    '''Their careers page, which describes them as a fully remote company'''
    url = 'https://www.sastrify.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://apply.workable.com/sastrify/'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Sastrify-EI_IE5571403.11,19.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Sastrify-Engineering-Reviews-EI_IE5571403.0,8_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech from old Senior FullStack Developer job spec'''
    url = 'https://angel.co/company/sastrify/jobs/1581484-senior-fullstack-developer-m-f-d-remote'
    return 'js, typescript, react, nodejs, postgres, aws', url


def salary():
    '''Salary range from old Senior Software Engineer job Spec'''
    url = 'https://angel.co/company/sastrify/jobs/1581484-senior-fullstack-developer-m-f-d-remote'
    return '€75k – €85k', url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/sastrify'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
