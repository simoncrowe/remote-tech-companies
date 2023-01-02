from company_data import RemotePolicy
from helpers import scrape

name = 'Meta'
business = 'Social Media'


def remote_policy():
    '''A web page that claims they're building a distributed-first future'''
    url = 'https://www.metacareers.com/facebook-life/remote/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.metacareers.com/jobs'
    return 'Europe, USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Meta-Reviews-E40772.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Meta-Engineering-Reviews-EI_IE40772.0,4_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Meta-Software-Engineer-Salaries-E40772_D_KO5,22.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from stackshare.io (NB: for facebook, not Instagram etc.)'''
    url = 'https://stackshare.io/facebook/facebook'
    tech = 'php, hack, js, react, graphql, cassandra, jenkins, chef'
    return tech, url
