from company_data import RemotePolicy
from helpers import scrape

name = 'OpenCraft'
business = 'EdTech'


def remote_policy():
    '''Their careers page, which describes them as truly remote'''
    url = 'https://opencraft.com/jobs/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Page with link to apply to globally remote position'''
    url = 'https://opencraft.com/jobs/'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-OpenCraft-EI_IE1513555.11,20.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/OpenCraft-Engineering-Reviews-EI_IE1513555.0,9_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/opencraft/tech-stack'
    tech = 'php, js, typescript, python, django, react, redis, postgres, rabbitmq, mongodb, ansible, terraform, docker, aws'
    return tech, url


def salary():
    '''Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/OpenCraft-Software-Developer-Salaries-E1513555_D_KO10,28.htm'
    return scrape.glassdoor_salary(url), url
