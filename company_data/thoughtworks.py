from company_data import RemotePolicy
from helpers import scrape

name = 'Thoughtworks'
business = 'Software Consultancy'


def remote_policy():
    '''A web page stating that they have long supported remote work '''
    url = 'https://www.thoughtworks.com/careers/remote-working'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional (potentially?) remote jobs'''
    url = 'https://www.thoughtworks.com/en-gb/careers/jobs'
    return 'APAC, EMEA, USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Thoughtworks-EI_IE38334.11,23.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Thoughtworks-Engineering-Reviews-EI_IE38334.0,12_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on their Languages and Frameworks Spotlight'''
    url = 'https://www.thoughtworks.com/radar/faq-and-more/10-years-of-radar/languages-and-frameworks-spotlight'
    tech = 'js, ruby, java, python'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Thoughtworks-Senior-Software-Engineer-Salaries-E38334_D_KO13,37.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/thoughtworks'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
