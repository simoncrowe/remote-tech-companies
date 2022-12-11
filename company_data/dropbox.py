from company_data import RemotePolicy
from helpers import scrape

name = 'Dropbox'
business = 'Cloud Storage'


def remote_policy():
    '''A blog post announcing their transition to Virtual First'''
    url = 'https://blog.dropbox.com/topics/company/dropbox-goes-virtual-first'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://jobs.dropbox.com/all-jobs'
    return 'USA, Canada, Poland, Ireland', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Dropbox-Engineering-Reviews-EI_IE415350.0,7_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Dropbox-EI_IE415350.11,18.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of tech from stackshare.io'''
    url = 'https://stackshare.io/dropbox/dropbox'
    tech = 'python, rust, nginx, AWS'
    return tech, url


def salary():
    '''Median IC2 Software Engineer salary'''
    url = 'https://www.levels.fyi/companies/dropbox/salaries/software-engineer/levels/ic2'
    return scrape.levels_salary(url), url
