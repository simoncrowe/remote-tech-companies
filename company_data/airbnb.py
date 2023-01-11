from company_data import RemotePolicy
from helpers import scrape

name = 'AirBnB'
business = 'Hospitality'


def remote_policy():
    '''A an article about their remote policy which allows for remote work within a given country'''
    url = 'https://www.inc.com/justin-bariso/airbnb-ceo-brian-chesky-new-remote-work-policy-hybrid-work.html'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://careers.airbnb.com/'
    return 'APAC, EMEA, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Airbnb-Reviews-E391850.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Airbnb-Engineering-Reviews-EI_IE391850.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/airbnb/airbnb'
    tech = 'js, java, ruby, mysql, redis, nginx, aws'
    return tech, url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Airbnb-Software-Engineer-Salaries-E391850_D_KO7,24.htm'
    return scrape.glassdoor_salary(url), url
