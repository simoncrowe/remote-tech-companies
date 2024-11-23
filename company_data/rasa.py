from company_data import RemotePolicy
from helpers import scrape

name = 'Rasa'
business = 'Chatbots'


def remote_policy():
    '''A blog post that discusses their remote-first onboarding'''
    url = 'https://rasa.com/blog/what-does-it-mean-to-be-an-engineering-buddy-at-rasa/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://rasa.com/careers/#jobs'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Rasa-Technologies-EI_IE1888472.11,28.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Rasa-Technologies-Engineering-Reviews-EI_IE1888472.0,17_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selection of tech from stackshare.io'''
    url = 'https://stackshare.io/rasa/stack'
    tech = 'python, go, js, redis, postgres, kafka, k8s, gcp'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Rasa-Technologies-Senior-Software-Engineer-Salaries-E1888472_D_KO18,42.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/rasa'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
