from company_data import RemotePolicy
from helpers import scrape

name = 'Coinbase'
business = 'Crypto Exchange'


def remote_policy():
    '''An article discussing their remote culture'''
    url = 'https://www.protocol.com/workplace/coinbase-remote-work'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.coinbase.com/careers/positions?department=Engineering'
    return 'global (US timezones)', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Coinbase-Engineering-Reviews-EI_IE779622.0,8_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Coinbase-EI_IE779622.11,19.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of tech listed on himalayas.app'''
    url = 'https://himalayas.app/companies/coinbase/tech-stack'
    tech = 'python, js, java, scala, kotlin, go, rails, django, react native, docker, kafka, postgres, mysql, hadoop, aws'
    return tech, url


def salary():
    '''Median salary for Software Engineer level IC4'''
    url = 'https://www.levels.fyi/companies/coinbase/salaries/software-engineer/levels/ic4'
    return scrape.levels_salary(url), url
