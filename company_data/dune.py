from company_data import RemotePolicy
from helpers import scrape

name = 'Dune'
business = 'Crypto Analytics'


def remote_policy():
    '''Their job board, which lists globally remote jobs'''
    url = 'https://jobs.ashbyhq.com/dune'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://jobs.ashbyhq.com/dune'
    return 'global (US timezones)', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Dune-Analytics-EI_IE6746061.11,25.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Dune-Analytics-Engineering-Reviews-EI_IE6746061.0,14_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://himalayas.app/companies/dune-analytics/tech-stack'
    tech = 'js, typescript, go, nginx, k8s, terraform, aws'
    return tech, url


def salary():
    '''Software Engineer Salary'''
    url = 'https://www.levels.fyi/companies/dune/salaries/software-engineer'
    return scrape.levels_salary(url), url
