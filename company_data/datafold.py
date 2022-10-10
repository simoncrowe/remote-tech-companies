from company_data import RemotePolicy
from helpers import scrape

name = 'Datafold'
business = 'Data Quality'


def remote_policy():
    '''Their career page, which says that the're remote-first'''
    url = 'https://www.datafold.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs with American core hours'''
    url = 'https://www.datafold.com/careers'
    return 'global (9am-12pm EST)', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Datafold-Engineering-Reviews-EI_IE3990562.0,8_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Datafold-EI_IE3990562.11,19.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Tech mentioned in Backend Software Engineer job spec'''
    url = 'https://www.datafold.com/careers?ashby_jid=de4a3572-bde6-4c75-920e-02f769f70281'
    tech = 'python, fastapi, postgres, neo4j, typescript, react, graphql'
    return tech, url


def salary():
    '''Not enough data at present'''
    url = 'https://www.levels.fyi/companies/datafold/salaries/software-engineer'
    return 'unknown', url
