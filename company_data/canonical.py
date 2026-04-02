from company_data import RemotePolicy
from helpers import scrape

name = 'Canonical'
business = 'open-source software'


def remote_policy():
    '''Their careers page, which says they are remote-first'''
    url = 'https://canonical.com/careers/company-culture/remote-work'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://canonical.com/careers/engineering'
    return 'global', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Canonical-EI_IE230560.11,20.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Canonical-Reviews-E230560.htm?filter.jobFunction=1007'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Senior Software Engineer based in the UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Canonical-Senior-Software-Engineer-Salaries-E230560_D_KO10,34.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from himalayas.app'''
    url = 'https://himalayas.app/companies/canonical/tech-stack'
    tech = 'js, python, java, postgres, okta, linux'
    return tech, url
