from company_data import RemotePolicy
from helpers import scrape

name = 'John Snow Labs'
business = 'NLP'


def remote_policy():
    '''Their careers page lists the perk: Work remotely from anywhere'''
    url = 'https://www.johnsnowlabs.com/careers/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://www.glassdoor.co.uk/Jobs/John-Snow-Labs-Jobs-E1853626.htm?filter.countryId=1'
    return 'global?', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-John-Snow-Labs-EI_IE1853626.11,25.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/John-Snow-Labs-Engineering-Reviews-EI_IE1853626.0,14_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Tech listed on Software Engineer job spec'''
    url = 'https://www.glassdoor.co.uk/Job/remote-ny-senior-software-engineer-jobs-SRCH_IL.0,9_IC5022349_KO10,34.htm?src=GD_JOB_AD&rdserp=true&srs=EI_JOBS&jl=1008352937787&ao=1136043&s=21&guid=000001852bed17a096108a301497d7db&pos=101&t=ESR&vt=w&uido=D94720BC0895752F6C324BBA984BADE1&ea=1&cs=1_8e8d8e70&cb=1671479236961&jobListingId=1008352937787&jrtk=3-0-1gkluq65aj46q801-1gkluq67l2go2000-c37368a28ad493ae-'
    tech = 'python'
    return tech, url


salary = 'unknown'
