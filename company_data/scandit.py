from company_data import RemotePolicy
from helpers import scrape

name = 'Scandit'
business = 'Computer Vision'


def remote_policy():
    '''Their careers page, which says they support WFH, office or hybrid'''
    url = 'https://www.scandit.com/careers/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for a few remote jobs'''
    url = 'https://www.scandit.com/careers/current-openings/'
    return 'Americas, APAC, EMEA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Scandit-EI_IE1406277.11,18.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Scandit-Engineering-Reviews-EI_IE1406277.0,7_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech from a Full-stack Engineer job spec'''
    url = 'https://www.scandit.com/careers/job-description/?gh_jid=4661352'
    tech = 'python, typescript, react, ruby, rails, mysql, postgres, k8s, aws'
    return tech, url


def salary():
    '''Software Engineer salary'''
    url = 'https://www.levels.fyi/companies/scandit/salaries/software-engineer'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/scandit'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
