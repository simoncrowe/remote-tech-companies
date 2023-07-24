from company_data import RemotePolicy
from helpers import scrape

name = 'Red Hat'
business = 'Linux/Cloud'


def remote_policy():
    '''Their jobs page, which says they offer remote options'''
    url = 'https://www.redhat.com/en/jobs'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://careers-redhat.icims.com/jobs/search'
    return 'APAC, EMEA, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Red-Hat-Reviews-E8868.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Red-Hat-Engineering-Reviews-EI_IE8868.0,7_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://us-redhat.icims.com/jobs/97334/software-engineer/job?hub=7&mobile=false&width=708&height=500&bga=true&needsRedirect=false&jan1offset=0&jun1offset=60'
    tech = 'c, python, shell, linux, docker'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Red-Hat-Senior-Software-Engineer-Salaries-E8868_D_KO8,32.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/red-hat'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
