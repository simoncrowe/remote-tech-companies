from company_data import RemotePolicy
from helpers import scrape

name = 'Snowplow'
business = 'Behavioral Data'


def remote_policy():
    '''A promotional video on their careers page references remote-first culture'''
    url = 'https://snowplow.io/careers/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://snowplow.io/careers/#open-positions'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Snowplow-EI_IE1482594.11,19.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Snowplow-Engineering-Reviews-EI_IE1482594.0,8_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io (plus go from a 2022 job spec)'''
    url = 'https://stackshare.io/snowplow-analytics/snowplow-analytics'
    tech = 'js, python, go, bash, k8s, gcp, aws'
    return tech, url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Snowplow-Software-Engineer-Salaries-E1482594_D_KO9,26.htm'
    return scrape.glassdoor_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/snowplow-analytics'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
