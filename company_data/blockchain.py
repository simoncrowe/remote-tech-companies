from company_data import RemotePolicy
from helpers import scrape

name = 'blockchain.com'
business = 'Crypto Exchange'


def remote_policy():
    '''Their job board lists some remote jobs'''
    url = 'https://www.blockchain.com/careers#jobs'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for some remote jobs'''
    url = 'https://www.blockchain.com/careers#jobs'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Blockchain-EI_IE1013721.11,21.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Blockchain-Engineering-Reviews-EI_IE1013721.0,10_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/blockchain-com/tech-stack'
    tech = 'java, swift, kotlin, python, objective-c, postgres, cassandra, kafka, gcp'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Blockchain-Senior-Software-Engineer-Salaries-E1013721_D_KO11,35.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/blockchain'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
