from company_data import RemotePolicy
from helpers import scrape

name = 'Open Corporates'
business = 'Company Data'


def remote_policy():
    '''A job spec that describes them as remote-first'''
    url = 'https://jobs.opencorporates.com/o/senior-engineer-python'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for remote jobs'''
    url = 'https://jobs.opencorporates.com/'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-OpenCorporates-EI_IE827216.11,25.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/OpenCorporates-Engineering-Reviews-EI_IE827216.0,14_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://jobs.opencorporates.com/o/senior-engineer-python'
    tech = 'ruby, python'
    return tech, url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/OpenCorporates-Software-Engineer-Salaries-E827216_D_KO15,32.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/opencorporates'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
