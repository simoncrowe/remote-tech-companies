from company_data import RemotePolicy
from helpers import scrape

name = 'Vista'
business = 'Marketing Material'


def remote_policy():
    '''Their careers page, which describes them as remote-first'''
    url = 'https://careers.vista.com/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://jobs.vista.com/Vista/go/Technology/8835800/'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Vista-Reviews-E21719.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Vista-Engineering-Reviews-EI_IE21719.0,5_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/Vista-Software-Engineer-Salaries-E21719_D_KO6,23.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Tech listed on software engineering job spec'''
    url = 'https://jobs.vista.com/Vista/job/Senior-Software-Engineer%2C-Foundations-domain-Europe-Remote/975593600/'
    tech = 'js, html, css, graphql, aws'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/vista'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
