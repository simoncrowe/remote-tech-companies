from company_data import RemotePolicy
from helpers import scrape

name = 'Acquia'
business = 'SaaS'


def remote_policy():
    '''Their remoteintech profile which claims some teams are 100% distributed'''
    url = 'https://github.com/remoteintech/remote-jobs/blob/main/company-profiles/acquia.md'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.acquia.com/careers/open-positions'
    return 'Europe, Americas, APAC', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Acquia-Reviews-E347852.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Acquia-Engineering-Reviews-EI_IE347852.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Acquia-Senior-Software-Engineer-Salaries-E347852_D_KO7,31.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/acquia/acquia'
    tech = 'php, java, nginx, aws'
    return tech, url
