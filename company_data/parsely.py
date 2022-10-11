from company_data import RemotePolicy
from helpers import scrape

name = 'Parse.ly'
business = 'Web Analytics'


def remote_policy():
    '''A blog post discussing their fully remote product team'''
    url = 'https://blog.parse.ly/the-how-and-why-of-parse-lys-fully-distributed-team/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://www.parse.ly/careers/'
    return 'global', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Parse-ly-Engineering-Reviews-EI_IE1197400.0,8_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Parse-ly-EI_IE1197400.11,19.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Tech taken from Senior Software Engineer job spec'''
    url = 'https://www.parse.ly/careers/senior-software-engineer-vip-platform'
    tech = 'js, php, go, docker, wordpress, elasticsearch, graphql'
    return tech, url


def salary():
    '''Senior Software Engineer'''
    url = 'https://www.glassdoor.com/Salary/Parse-ly-Senior-Software-Engineer-Salaries-E1197400_D_KO9,33.htm'
    return scrape.glassdoor_salary(url), url
