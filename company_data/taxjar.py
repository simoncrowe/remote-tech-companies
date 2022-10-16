from company_data import RemotePolicy
from helpers import scrape

name = 'Taxjar'
business = 'eCommerce Tax'


def remote_policy():
    '''A blog post describing their remote culture'''
    url = 'https://www.taxjar.com/blog/2021-09-demonstrating-their-trailblazing-stance-on-working-remotely-taxjar-releases-docuseries-titled-remotelife'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Page that should list remote jobs - possibly unused since they were acquired by Stripe'''
    url = 'https://apply.workable.com/taxjar/'
    return 'global', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/TaxJar-Engineering-Reviews-EI_IE1450050.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-TaxJar-EI_IE1450050.11,17.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of tech from stackshare.io'''
    url = 'https://stackshare.io/taxjar/taxjar'
    tech = 'ruby, rails, postgres, redis'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.com/Salary/TaxJar-Senior-Software-Engineer-Salaries-E1450050_D_KO7,31.htm'
    return scrape.glassdoor_salary(url), url
