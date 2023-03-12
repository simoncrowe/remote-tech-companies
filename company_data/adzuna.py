from company_data import RemotePolicy
from helpers import scrape

name = 'Adzuna'
business = 'Job Search'


def remote_policy():
    '''Their remoteintech profile, which says mostly their tech team work remotely'''
    url = 'https://github.com/remoteintech/remote-jobs/blob/main/company-profiles/adzuna.md'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.adzuna.co.uk/jobs/search?cmp=31381'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Reviews/Adzuna-Reviews-E406247.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Adzuna-Engineering-Reviews-EI_IE406247.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Adzuna-Software-Developer-Salaries-E406247_D_KO7,25.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/adamtaylor/adzuna'
    tech = 'perl, js. mysql, nginx jenkins, aws'
    return tech, url
