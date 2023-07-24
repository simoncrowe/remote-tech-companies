from company_data import RemotePolicy
from helpers import scrape

name = 'Automattic'
business = ''


def remote_policy():
    '''Their careers page, which suggest one works 'from anywhere' '''
    url = 'https://automattic.com/work-with-us/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Forms to register interest in global remote jobs'''
    url = 'https://automattic.com/work-with-us/'
    return 'global', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Automattic-Reviews-E751107.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Automattic-Engineering-Reviews-EI_IE751107.0,10_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Automattic-Software-Engineer-Salaries-E751107_D_KO11,28.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/automattic/tech-stack'
    tech = 'php, ruby, python, go, java, scala, swift, kotlin, js, docker, k8s, mysql, redis, kafka'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/automattic'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
