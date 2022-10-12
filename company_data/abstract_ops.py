from company_data import RemotePolicy
from helpers import scrape

name = 'AbstractOps'
business = 'Legal Docs'


def remote_policy():
    '''A blog post describing their remote culture'''
    url = 'https://www.abstractops.com/how-to-work-with-teams-in-opposite-time-zones'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://work.abstractops.com/'
    return 'global (US timezones)', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/AbstractOps-Engineering-Reviews-EI_IE6885566.0,11_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-AbstractOps-EI_IE6885566.11,22.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Languages listed on Software Engineer job spec'''
    url = 'https://work.abstractops.com/experienced-backend-software-engineer'
    tech = 'js, react, graphql, postgres, gcp, k8s'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/AbstractOps-Software-Engineer-Salaries-E6885566_D_KO12,29.htm'
    return scrape.glassdoor_salary(url), url
