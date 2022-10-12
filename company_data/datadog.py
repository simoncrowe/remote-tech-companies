from company_data import RemotePolicy
from helpers import scrape

name = 'Datadog'
business = 'Observability'


def remote_policy():
    '''Blog post describing one employee's experience of remote work'''
    url = 'https://www.datadoghq.com/blog/pup-culture/9-ways-to-make-working-remote-work-for-you/'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.datadoghq.com/jobs-engineering/'
    return 'EMEA, USA', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Datadog-Engineering-Reviews-EI_IE762009.0,7_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Datadog-EI_IE762009.11,18.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of tech from stackshare.io'''
    url = 'https://stackshare.io/datadog/datadog'
    tech = 'js, python, go, react, nginx, redis, postgres, kafka, aws'
    return tech, url


def salary():
    '''Senior Software Engineer salary from UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Datadog-Senior-Software-Engineer-Salaries-E762009_D_KO8,32.htm'
    return scrape.glassdoor_salary(url), url
