from company_data import RemotePolicy
from helpers import scrape

name = 'Hotjar'
business = 'Behavior Analytics'


def remote_policy():
    '''Blog post about remote work'''
    url = 'https://www.hotjar.com/blog/tips-on-remote-working/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://boards.eu.greenhouse.io/hotjar'
    return 'EMEA, Americas', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Hotjar-Engineering-Reviews-EI_IE1494810.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Hotjar-EI_IE1494810.11,17.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Tech mentioned on a Senior Software Engineer job spec'''
    url = 'https://boards.eu.greenhouse.io/hotjar/jobs/4068204101'
    tech = 'python, flask, elasticsearch, postgresql, kubernetes, kafka, aws'
    return tech, url


def salary():
    '''Salary range mentioned on a Senior Software Engineer job spec (Remote: EMEA)'''
    url = 'https://www.levels.fyi/companies/grafana/salaries/software-engineer'
    return '€80,000 - €105,000', url
