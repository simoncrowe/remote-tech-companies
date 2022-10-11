from company_data import RemotePolicy
from helpers import scrape

name = 'Etsy'
business = 'eCommerce'


def remote_policy():
    '''One of their career pages which lists several fully-remote regions'''
    url = 'https://careers.etsy.com/global/en/how-and-where-we-work'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Remote locations listed on one of their career pages'''
    url = 'https://careers.etsy.com/global/en/how-and-where-we-work'
    return 'US, Canada, Ireland, UK, Mexico, India', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Etsy-Engineering-Reviews-EI_IE42751.0,4_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Etsy-EI_IE42751.11,15.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of tech from stackshare.io'''
    url = 'https://stackshare.io/etsy/etsy'
    tech = 'javascript, python, react, aws, jenkins'
    return tech, url


def salary():
    '''Senior Software Engineer'''
    url = 'https://www.glassdoor.com/Salary/Etsy-Senior-Software-Engineer-Salaries-E42751_D_KO5,29.htm'
    return scrape.glassdoor_salary(url), url
