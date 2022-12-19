from company_data import RemotePolicy
from helpers import scrape

name = 'Vareto'
business = 'Financial Planning Platform'


def remote_policy():
    '''Their careers page describes their team as fully remote'''
    url = 'https://www.vareto.com/careers'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://boards.greenhouse.io/vareto'
    return 'Europe, Americas', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Vareto-EI_IE3565267.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Vareto-Engineering-Reviews-EI_IE3565267.0,6_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://startup.jobs/senior-backend-engineer-vareto-3976237'
    tech = 'python'
    return tech, url


def salary():
    '''Estimate on Senior Backend engineer job spec'''
    url = 'https://www.glassdoor.com/Job/sunnyvale-ca-senior-back-end-engineer-jobs-SRCH_IL.0,12_IC1147442_KO13,37.htm?src=GD_JOB_AD&rdserp=true&srs=EI_JOBS&jl=1008349010689&ao=1136043&s=21&guid=000001852be555ba99e2f207ff6eb863&pos=101&t=ESR&vt=w&uido=D94720BC0895752F6C324BBA984BADE1&cs=1_140617d6&cb=1671478728749&jobListingId=1008349010689&jrtk=3-0-1gklualsgjm5g801-1gklualteh7gj800-57f70735a3777c31-'
    return '$117K - $167K', url
