from company_data import RemotePolicy
from helpers import scrape

name = 'juro'
business = 'Contracts'


def remote_policy():
    '''A job spec that says they accept applicants from UK, EU and EFTA countries'''
    url = 'https://www.notion.so/Senior-Backend-Engineer-de96a55466324920b2a626a8a407c617'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.notion.so/Careers-at-Juro-80907c47473d4fffa5bb30991e5e83bd'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Juro-EI_IE3044304.11,15.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Juro-Engineering-Reviews-EI_IE3044304.0,4_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://www.notion.so/Senior-Fullstack-Engineer-5ab105e3f8974198b65816782262db4e'
    tech = 'js, typescript, react, mongodb'
    return tech, url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Juro-Software-Engineer-Salaries-E3044304_D_KO5,22.htm'
    return scrape.glassdoor_salary(url), url
