from company_data import RemotePolicy
from helpers import scrape

name = 'Omnipresent'
business = 'HR'


def remote_policy():
    '''Their careers page, which describes them as remote-first'''
    url = 'https://www.omnipresent.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global and regional remote jobs'''
    url = 'https://www.omnipresent.com/jobs'
    return 'global', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Omnipresent-EI_IE289172.11,22.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Omnipresent-Engineering-Reviews-EI_IE289172.0,11_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/omnipresent/tech-stack'
    tech = 'js, node.js, typescript, react, python, terraform, docker, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Omnipresent-Senior-Software-Engineer-Salaries-E289172_D_KO12,36.htm'
    return scrape.glassdoor_salary(url), url
