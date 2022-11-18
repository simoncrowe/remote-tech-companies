from company_data import RemotePolicy
from helpers import scrape

name = 'Zoe'
business = 'Nutrition'


def remote_policy():
    '''Their careers page, which describes them as remote-first'''
    url = 'https://www.notion.so/Working-at-ZOE-We-Are-Hiring-8b8954cb8b50419e8f7d87b9ea176e1f'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://jobs.lever.co/joinzoe'
    return 'USA, Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Zoe-EI_IE2886051.11,14.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Zoe-Engineering-Reviews-EI_IE2886051.0,3_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://jobs.lever.co/joinzoe/95cd8193-7356-4593-9263-51803ac38263'
    tech = 'python, fastapi, kotlin, spring boot, typescript, react, postgres, terraform, k8s, gcp'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.glassdoor.co.uk/Salary/Zoe-Software-Engineer-Salaries-E2886051_D_KO4,21.htm'
    return scrape.glassdoor_salary(url), url
