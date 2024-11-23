from company_data import RemotePolicy
from helpers import scrape

name = 'Fastly'
business = 'Edge (Cloud)'


def remote_policy():
    '''A blog post describing remote culture before and after the COVID-19 pandemic.'''
    url = 'https://www.fastly.com/blog/its-in-our-dna-how-fastlys-history-of-flexible-work-is-shaping-our-future'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for seemingly regional remote jobs'''
    url = 'https://www.fastly.com/about/careers/current-openings'
    return 'USA, UK, Canada', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Fastly-Engineering-Reviews-EI_IE814479.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Fastly-EI_IE814479.11,17.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Select tech from himalayas.app'''
    url = 'https://himalayas.app/companies/fastly/tech-stack'
    tech = 'js, go, java, kotlin, terraform, mysql, mongodb, kafka, cassandra, nginx, gcp'
    return tech, url


def salary():
    '''Senior Software Engineer based in USA'''
    url = 'https://www.levels.fyi/companies/fastly/salaries/software-engineer/levels/e4'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/fastly'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
