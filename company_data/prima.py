from company_data import RemotePolicy
from helpers import scrape

name = 'Prima'
business = 'Insurance'


def remote_policy():
    '''Their careers page, which says they support working from home'''
    url = 'https://www.helloprima.com/careers/prima-benefits'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.helloprima.com/careers/jobs'
    return 'Italy, Spain, UK', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Prima-Assicurazioni-EI_IE1395225.11,30.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Prima-Assicurazioni-Reviews-E1395225.htm?filter.jobFunction=1007'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.co.uk/Salary/Prima-Assicurazioni-Senior-Software-Engineer-Salaries-E1395225_D_KO20,44.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/prima-assicurazioni/prima-assicurazioni'
    tech = 'python, php, rust, elixir, mysql, postgres, redis, nginx, k8s, aws, datadog'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/prima-it'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
