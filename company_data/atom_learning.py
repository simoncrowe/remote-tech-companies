from company_data import RemotePolicy
from helpers import scrape

name = 'Atom Learning'
business = 'EdTech'


def remote_policy():
    '''Their careers page, which says they offer fully remote and flexible work'''
    url = 'https://atomlearning.co.uk/careers'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://jobs.lever.co/atomlearning'
    return 'Europe?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Atom-Learning-EI_IE3996943.11,24.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Atom-Learning-Engineering-Reviews-EI_IE3996943.0,13_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on their careers page'''
    url = 'https://atomlearning.co.uk/careers'
    tech = 'js, typescript, mysql, mongodb, redis, k8s'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Atom-Learning-Senior-Software-Engineer-Salaries-E3996943_D_KO14,38.htm'
    return scrape.glassdoor_salary(url), url
