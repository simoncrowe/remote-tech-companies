from company_data import RemotePolicy
from helpers import scrape

name = 'GoTo'
business = 'Collaboration Software'


def remote_policy():
    '''Their careers page, which says most employees work remotely'''
    url = 'https://www.goto.com/company/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://goto.wd5.myworkdayjobs.com/GoToCareers'
    return 'APAC, EMEA, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/GoTo-Reviews-E43330.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/GoTo-Engineering-Reviews-EI_IE43330.0,4_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.co.uk/Salary/GoTo-Senior-Software-Engineer-Salaries-E43330_D_KO5,29.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Tech mentioned on Software Engineer job spec'''
    url = 'https://goto.wd5.myworkdayjobs.com/en-US/GoToCareers/job/Bangalore-KA-IN/Software-Development-Engineer_R-2022-2810-1?jobFamilyGroup=9147d7f6d775102e29bacc9daeba85a0'
    tech = 'java'
    return tech, url
