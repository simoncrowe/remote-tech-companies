from company_data import RemotePolicy
from helpers import scrape

name = 'Shopify'
business = 'eCommerce'


def remote_policy():
    '''Their careers page, which describes them as digital by design'''
    url = 'https://www.shopify.com/careers/work-anywhere'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://www.shopify.com/careers/search'
    return 'global', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Shopify-Engineering-Reviews-EI_IE675933.0,7_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Shopify-EI_IE675933.11,18.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/shopify/shopify'
    tech = 'ruby, rails, mysql, redis, memcached, k8s'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Shopify-Senior-Software-Engineer-Salaries-E675933_D_KO8,32.htm'
    return scrape.glassdoor_salary(url), url
