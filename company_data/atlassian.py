from company_data import RemotePolicy
from helpers import scrape

name = 'Atlassian'
business = 'Software'


def remote_policy():
    '''Their careers page, which says they support in office or remote work'''
    url = 'https://www.atlassian.com/company/careers'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.atlassian.com/company/careers/all-jobs'
    return 'APAC, EMEA, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Atlassian-EI_IE115699.11,20.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Atlassian-Engineering-Reviews-EI_IE115699.0,9_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/atlassian/tech-stack'
    tech = 'java, kotlin, js, python, react, django, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Atlassian-Senior-Software-Engineer-Salaries-E115699_D_KO10,34.htm'
    return scrape.glassdoor_salary(url), url
