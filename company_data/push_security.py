from company_data import RemotePolicy
from helpers import scrape

name = 'Push Security'
business = 'SaaS'


def remote_policy():
    '''An Otta job spec, which says they're an all-remote company'''
    url = 'https://app.otta.com/dashboard/jobs/SHVVZlVV'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://pushsecurity.bamboohr.com/jobs/'
    return 'UK, USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.ca/Reviews/Push-Security-Reviews-E6189394.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.ca/Reviews/Push-Security-Engineering-Reviews-EI_IE6189394.0,13_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech mentioned on Python Engineer job spec'''
    url = 'https://pushsecurity.bamboohr.com/jobs/view.php?id=54&source=bamboohr'
    tech = 'python, aws'
    return tech, url
