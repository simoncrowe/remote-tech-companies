from company_data import RemotePolicy
from helpers import scrape

name = 'Tessian'
business = 'Email Security'


def remote_policy():
    '''A blog post describing their hybrid approach to remote work'''
    url = 'https://www.tessian.com/blog/hybird-remote-work-policy-at-tessian/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.tessian.com/careers/jobs-list/'
    return 'Europe, US', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Tessian-EI_IE1769981.11,18.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Tessian-Engineering-Reviews-EI_IE1769981.0,7_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://jobs.lever.co/tessian/93d6cfcd-5cf6-4baa-8856-517c8d26a780'
    tech = 'python, js, typescript, docker, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Tessian-Senior-Software-Engineer-Salaries-E1769981_D_KO8,32.htm'
    return scrape.glassdoor_salary(url), url
