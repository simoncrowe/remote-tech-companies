from company_data import RemotePolicy
from helpers import scrape

name = 'Compuco'
business = 'UX/CRM/Hosting for Nonprofits'


def remote_policy():
    '''Their culture page, which says they support remote work'''
    url = 'https://www.compuco.io/company-culture'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://careers.compuco.io/open-roles'
    return 'global', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.com/Reviews/Compuco-Reviews-E1375270.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.com/Reviews/Compuco-Engineering-Reviews-EI_IE1375270.0,7_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def salary():
    '''Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Compuco-Software-Engineer-Salaries-E1375270_D_KO8,25.htm'
    return scrape.glassdoor_salary(url), url


def tech_stack():
    '''Selected tech from remoteintech profile'''
    url = 'https://github.com/remoteintech/remote-jobs/blob/main/company-profiles/compucorp.md'
    tech = 'php, python, drupal, civicrm, react, ansible, packer, jenkins, aws'
    return tech, url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/compuco'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
