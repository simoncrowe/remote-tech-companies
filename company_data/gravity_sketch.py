from company_data import RemotePolicy
from helpers import scrape

name = 'Gravity Sketch'
business = '3D Design'


def remote_policy():
    '''Their careers page, which says they support remote and hybrid working'''
    url = 'https://www.gravitysketch.com/careers/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional jobs with remote options'''
    url = 'https://www.gravitysketch.com/careers/'
    return 'UK, USA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Gravity-Sketch-EI_IE2328807.11,25.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Gravity-Sketch-Engineering-Reviews-EI_IE2328807.0,14_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://apply.workable.com/gravitysketch/j/F258A828C5/'
    tech = 'c#, java c++'
    return tech, url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Gravity-Sketch-Software-Engineer-Salaries-E2328807_D_KO15,32.htm'
    return scrape.glassdoor_salary(url), url
