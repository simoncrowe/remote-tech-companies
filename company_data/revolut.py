from company_data import RemotePolicy
from helpers import scrape

name = 'Revolut'
business = 'Fintech'


def remote_policy():
    '''An article that discusses their flexible work policy'''
    url = 'https://employeebenefits.co.uk/revolut-offers-full-staff-flexibility-with-working-abroad-policy/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for reginal in-office and remote jobs'''
    url = 'https://www.revolut.com/careers/'
    return 'global', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Revolut-Engineering-Reviews-EI_IE1176471.0,7_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Revolut-EI_IE1176471.11,18.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/revolut/revolut'
    tech = 'java, scala, kotlin, js, docker, ansible'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Revolut-Senior-Software-Engineer-Salaries-E1176471_D_KO8,32.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/revolut'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
