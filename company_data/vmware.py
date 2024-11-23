from company_data import RemotePolicy
from helpers import scrape

name = 'VMware'
business = 'Virtualisation / Cloud'


def remote_policy():
    '''Their jobs page, which lists many remote jobs'''
    url = 'https://careers.vmware.com/main/jobs'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://careers.vmware.com/main/jobs'
    return 'APAC, Americas, EMEA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/VMware-Reviews-E12830.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/VMware-Engineering-Reviews-EI_IE12830.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/VMware-Senior-Software-Engineer-Salaries-E12830_D_KO7,31.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Tech mentioned on a software engineer job spec'''
    url = 'https://careers.vmware.com/main/jobs/R2222782?lang=en-us'
    tech = 'java, go, python, kafka, jenkins, docker, k8s, aws'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/vmware'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
