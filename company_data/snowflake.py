from company_data import RemotePolicy
from helpers import scrape

name = 'Snowflake'
business = 'Data Cloud'


def remote_policy():
    '''A teamblind.com thread that discusses their rare fully-remote roles'''
    url = 'https://www.teamblind.com/post/Snowflake-allows-remote-work-2yxsZ2bn'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://careers.snowflake.com/us/en/search-results'
    return 'Americas, APAC, EMEA', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Snowflake-Reviews-E928471.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Snowflake-Engineering-Reviews-EI_IE928471.0,9_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.co.uk/Salary/Snowflake-Software-Developer-Salaries-E928471_D_KO10,28.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/snowflake/tech-stack'
    tech = 'js, java, python, php, go, c++, tensorflow, pytorch, linux, postgres, mysql, cassandra, jenkins, k8s, aws'
    return tech, url
