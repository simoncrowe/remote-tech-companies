from company_data import RemotePolicy
from helpers import scrape

name = 'Beyond'
business = 'Property Rental'


def remote_policy():
    '''Their remoteintech profile which says most of their dev team is remote'''
    url = 'https://github.com/remoteintech/remote-jobs/blob/main/company-profiles/beyondpricing.md'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://boards.greenhouse.io/beyond'
    return 'EMEA, India, USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Beyond-Reviews-E2068831.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Beyond-Engineering-Reviews-EI_IE2068831.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Software Developer based in EU'''
    url = 'https://www.glassdoor.co.uk/Salary/Beyond-Software-Developer-Salaries-E2068831_D_KO7,25.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/beyond/tech-stack'
    tech = 'python, js, django, next.js, postgresql, nginx, AWS'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/beyond-pricing'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
