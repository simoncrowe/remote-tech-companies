from company_data import RemotePolicy
from helpers import scrape

name = 'Casumo'
business = 'Gambling'


def remote_policy():
    '''Their remoteintech profile says they have employees spread around Europe'''
    url = 'https://github.com/remoteintech/remote-jobs/blob/main/company-profiles/casumo.md'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'Europe'
    return 'https://www.casumocareers.com/open-positions/', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Casumo-Reviews-E1443581.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Casumo-Engineering-Reviews-EI_IE1443581.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/Casumo-Software-Engineer-Salaries-E1443581_D_KO7,24.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/casumo/casumo'
    tech = 'js, java, scala, python, swift, mysql, nginx'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/casumo'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
