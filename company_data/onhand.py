from company_data import RemotePolicy
from helpers import scrape

name = 'onHand'
business = 'Volunteering'


def remote_policy():
    '''A blog post describing their remote culture'''
    url = 'https://www.abstractops.com/how-to-work-with-teams-in-opposite-time-zones'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.beonhand.co.uk/careers'
    return 'UK', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.com/Overview/Working-at-onHand-EI_IE5661148.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.com/Reviews/onHand-Engineering-Reviews-EI_IE5661148.0,6_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://www.beonhand.co.uk/senior-python-engineer'
    tech = 'python, flask, postgres, docker, k8s, heroku, aws'
    return tech, url


salary = "unknown"
