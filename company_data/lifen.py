from company_data import RemotePolicy
from helpers import scrape

name = 'Lifen'
business = 'HealthTech'


def remote_policy():
    '''Their remoteintech profile, which cites flexibility regarding remote work'''
    url = 'https://github.com/remoteintech/remote-jobs/blob/main/company-profiles/lifen.md'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://jobs.lever.co/lifen?'
    return 'France, Germany, UK', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Lifen-Reviews-E1036418.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Lifen-Engineering-Reviews-EI_IE1036418.0,5_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from remoteintech profile'''
    url = 'https://github.com/remoteintech/remote-jobs/blob/main/company-profiles/lifen.md'
    tech = 'python, ruby, js, rails, nodejs, react, java, k8s, terraform, docker'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/lifen'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
