from company_data import RemotePolicy
from helpers import scrape

name = 'Grafana'
business = 'Observability'


def remote_policy():
    '''Blog post about their remote-first culture'''
    url = 'https://grafana.com/blog/2022/01/28/inside-grafana-labs-learn-about-our-remote-first-culture-and-meet-our-teams-at-our-virtual-open-house/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global and regional remote jobs'''
    url = 'https://grafana.com/about/careers/open-positions/'
    return 'global', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Grafana-Labs-Engineering-Reviews-EI_IE2300269.0,12_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Grafana-Labs-EI_IE2300269.11,23.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Main languages from their open source repos'''
    url = 'https://github.com/orgs/grafana/repositories'
    tech = 'go, typescript'
    return tech, url


def salary():
    '''Senior Software Engineer in USA'''
    url = 'https://www.levels.fyi/companies/grafana/salaries/software-engineer?country=254'
    return scrape.levels_salary(url), url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/raintank'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
