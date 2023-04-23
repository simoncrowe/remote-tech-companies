from company_data import RemotePolicy
from helpers import scrape

name = 'Alan'
business = 'Health/Insurtech'


def remote_policy():
    '''A blog post, which says they have a 'work from anywhere' culture'''
    url = 'https://medium.com/alan/working-at-alan-from-anywhere-9a6fe381dc0a'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for some regional remote jobs'''
    url = 'https://jobs.lever.co/alan'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Alan-Reviews-E1696043.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Alan-Engineering-Reviews-EI_IE1696043.0,4_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Software Engineer based in Paris'''
    url = 'https://www.glassdoor.co.uk/Salary/Alan-Software-Engineer-Paris-Salaries-EJI_IE1696043.0,4_KO5,22_IL.23,28_IM1080.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/alan/tech-stack'
    tech = 'python, typescript, flask, react, postgres, aws'
    return tech, url
