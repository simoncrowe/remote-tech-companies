from company_data import RemotePolicy
from helpers import scrape

name = 'The Lifetime Value Co.'
business = 'Data Services'


def remote_policy():
    '''A blog post describing their shift to remote-first'''
    url = 'https://www.ltvco.com/blog/LTV-full-time-remote-work/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://www.ltvco.com/careers/'
    return 'USA, Costa Rica', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/The-Lifetime-Value-Co-Engineering-Reviews-EI_IE4075133.0,21_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-The-Lifetime-Value-Co-EI_IE4075133.11,32.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Tech listed on Director of Software Engineering job spec'''
    url = 'https://www.ltvco.com/careers/job/director-of-software-engineering_job_20220602145107_m3avoagra4o96fl0/'
    tech = 'ruby, rails, go, ember'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/The-Lifetime-Value-Co-Senior-Software-Engineer-Salaries-E4075133_D_KO22,46.htm'
    return scrape.glassdoor_salary(url), url
