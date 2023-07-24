from company_data import RemotePolicy
from helpers import scrape

name = 'Moov'
business = 'Fintech'


def remote_policy():
    '''Their careers page, which describes them as 100% remote'''
    url = 'https://moov.io/careers/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://moov.io/careers/#open-roles'
    return 'USA', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Moov-Financial-Engineering-Reviews-EI_IE4223522.0,14_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Moov-Financial-EI_IE4223522.11,25.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Tech listed on Senior Software Engineer job spec'''
    url = 'https://boards.greenhouse.io/moovfinancial/jobs/4535076004'
    tech = 'go, docker, k8s, mysql, kafka'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.co.uk/Salary/Moov-Financial-Senior-Software-Engineer-Cedar-Falls-Salaries-EJI_IE4223522.0,14_KO15,39_IL.40,51_IC1149509.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/moov'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
