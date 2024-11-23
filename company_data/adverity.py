from company_data import RemotePolicy
from helpers import scrape

name = 'Adverity'
business = 'Data platform'


def remote_policy():
    '''A job spec that says candidates could work remotely in Europe or from an office'''
    url = 'https://www.adverity.com/careers/python-engineer-fmd'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.adverity.com/careers'
    return 'global (US timezones)', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Adverity-EI_IE2105171.11,19.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Adverity--Engineering-Reviews-EI_IE2105171.0,9_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://www.adverity.com/careers/python-engineer-fmd'
    tech = 'python'
    return tech, url


def salary():
    '''Software Engineer Salary'''
    url = 'https://www.levels.fyi/companies/adverity/salaries/software-engineer'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/adverity'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
