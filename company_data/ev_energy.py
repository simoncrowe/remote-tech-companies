from company_data import RemotePolicy
from helpers import scrape

name = 'ev.energy'
business = 'EV Smart Charging'


def remote_policy():
    '''A blog post describing their remote culture'''
    url = 'https://www.ev.energy/blog/how-we-connect-our-remote-team-to-drive-change-at-a-global-scale'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://business.ev.energy/careers'
    return 'UK, USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.com/Overview/Working-at-ev-energy-EI_IE3429785.11,20.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.com/Reviews/ev.energy-Engineering-Reviews-EI_IE3429785.0,9_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://evenergy.teamtailor.com/en/jobs/2112036-senior-backend-engineer-fully-remote?utm_campaign=jobs-widget&utm_source=evenergy.teamtailor.com&utm_content=jobs&utm_medium=web'
    tech = 'python, django'
    return tech, url


def salary():
    '''Salary range from Senior Software Engineer job spec'''
    url = 'https://evenergy.teamtailor.com/en/jobs/2112036-senior-backend-engineer-fully-remote?utm_campaign=jobs-widget&utm_source=evenergy.teamtailor.com&utm_content=jobs&utm_medium=web'
    return '£66-79k', url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/ev-energy'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
