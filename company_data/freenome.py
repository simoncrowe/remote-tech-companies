from company_data import RemotePolicy
from helpers import scrape

name = 'Freenome'
business = 'Biotech'


def remote_policy():
    '''Their careers page which lists remote jobs'''
    url = 'https://careers.freenome.com/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings regional global remote jobs'''
    url = 'https://careers.freenome.com/'
    return 'USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Freenome-EI_IE1411775.11,19.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Freenome-Engineering-Reviews-EI_IE1411775.0,8_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://careers.freenome.com/job?gh_jid=6393364002'
    tech = 'python, k8s, gcp'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/Freenome-Senior-Software-Engineer-Salaries-E1411775_D_KO9,33.htm'
    return scrape.glassdoor_salary(url), url
