from company_data import RemotePolicy
from helpers import scrape

name = '15Five'
business = 'HR'


def remote_policy():
    '''Their remoteintech profile which says over half the company works remote'''
    url = 'https://github.com/remoteintech/remote-jobs/blob/main/company-profiles/15five.md'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.15five.com/about/careers/#open-positions'
    return 'Europe, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/15Five-Reviews-E1391015.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/15Five-Engineering-Reviews-EI_IE1391015.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Software Engineer based in USA'''
    url = 'https://www.levels.fyi/companies/15five/salaries/software-engineer'
    return scrape.levels_salary(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/15five/tech-stack'
    tech = 'js, python, php, typescript, nginx, aws'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/15five'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
