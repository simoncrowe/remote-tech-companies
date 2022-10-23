from company_data import RemotePolicy
from helpers import scrape

name = 'Primer'
business = 'Payments'


def remote_policy():
    '''Their team page describes them as remote-fist'''
    url = 'https://primer.io/team/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://primerio.notion.site/primerio/Careers-Primer-aff1f1be31054c9eae0f1c75acd642d0'
    return 'global', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Primer-Engineering-Reviews-EI_IE4211292.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Primer-EI_IE4211292.11,17.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/primer-io/primer'
    tech = 'js, python, react, fastapi, postgres, redis, k8s, aws'
    return tech, url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Primer-Software-Engineer-Salaries-E4211292_D_KO7,24.htm'
    return scrape.glassdoor_salary(url), url
