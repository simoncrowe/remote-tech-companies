from company_data import RemotePolicy
from helpers import scrape

name = 'Aiven'
business = 'Data Platform'


def remote_policy():
    '''Their career page, which mentions working from anywhere'''
    url = 'https://aiven.io/careers'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for (possibly) global and regional remote jobs'''
    url = 'https://aiven.io/careers/job'
    return 'global?', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Aiven-Engineering-Reviews-EI_IE2610934.0,5_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Aiven-EI_IE2610934.11,16.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Main languages from their open source repos'''
    url = 'https://github.com/orgs/aiven/repositories'
    tech = 'python, go, java'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Aiven-Senior-Software-Engineer-Salaries-E2610934_D_KO6,30.htm'
    return scrape.glassdoor_salary(url), url
