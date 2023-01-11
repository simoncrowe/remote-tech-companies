from company_data import RemotePolicy
from helpers import scrape

name = 'Blackbaud'
business = 'Cloud Software'


def remote_policy():
    '''Their careers page, which describes them as a global remote-first team'''
    url = 'https://careers.blackbaud.com/us/en/home'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://careers.blackbaud.com/us/en/search-results'
    return 'APAC, UK, USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Blackbaud-Reviews-E15863.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Blackbaud-Engineering-Reviews-EI_IE15863.0,9_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/blackbaud/blackbaud'
    tech = 'java, js, php, gcp, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Blackbaud-Senior-Software-Engineer-Salaries-E15863_D_KO10,34.htm'
    return scrape.glassdoor_salary(url), url
