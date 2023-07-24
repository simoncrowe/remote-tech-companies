from company_data import RemotePolicy
from helpers import scrape

name = 'Deel'
business = 'Payroll'


def remote_policy():
    '''Their careers page, which describes their team as globally distributed'''
    url = 'https://www.deel.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs across the globe'''
    url = 'https://jobs.ashbyhq.com/Deel'
    return 'global', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Deel-EI_IE3728271.11,15.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Deel-Engineering-Reviews-EI_IE3728271.0,4_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/deel/tech-stack'
    tech = 'js, typescript, react, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Deel-Senior-Software-Engineer-Salaries-E3728271_D_KO5,29.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/deel'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
