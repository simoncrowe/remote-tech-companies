from company_data import RemotePolicy
from helpers import scrape

name = 'GitHub'
business = 'this platform (lol)'


def remote_policy():
    '''Their careers page, which says they are a remote-first company'''
    url = 'https://github.com/about/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://github.com/about/careers'
    return 'USA, Canada, Europe, APAC', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/GitHub-Reviews-E671945.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/GitHub-Engineering-Reviews-EI_IE671945.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/GitHub-Senior-Software-Engineer-Salaries-E671945_D_KO7,31.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/github/tech-stack'
    tech = 'ruby, java, js, python, go, c, swift, kotlin, rails, mysql,postgres, redis, k8s'
    return tech, url
