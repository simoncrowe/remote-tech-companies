from company_data import RemotePolicy
from helpers import scrape

name = 'DroneDeploy'
business = 'Reality Capture'


def remote_policy():
    '''Their careers page, which says they support a hybrid working model'''
    url = 'https://www.dronedeploy.com/about/careers/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.dronedeploy.com/about/join-the-team/'
    return 'New Zealand, USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-DroneDeploy-EI_IE1103556.11,22.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/DroneDeploy-Engineering-Reviews-EI_IE1103556.0,11_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/dronedeploy/dronedeploy'
    tech = 'js, node, k8s, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/DroneDeploy-Software-Engineer-Salaries-E1103556_D_KO12,29.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/dronedeploy'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
