from company_data import RemotePolicy
from helpers import scrape

name = 'Upvest'
business = 'Investment'


def remote_policy():
    '''Their careers page which lists hybrid and fully remote jobs'''
    url = 'https://careers.upvest.co/jobs'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for global remote jobs'''
    url = 'https://careers.upvest.co/jobs'
    return 'Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Upvest-EI_IE2948356.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Upvest-Engineering-Reviews-EI_IE2948356.0,6_DEPT1007.htm?filter.iso3Language=eng'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/upvest/upvest'
    tech = 'go, python, js, postgres, kafka, k8s, gcp'
    return tech, url


def salary():
    '''Salary range from 2022 job spec'''
    url = 'https://golang.cafe/job/golang-backend-engineer-f-m-d-upvest-1606150893'
    return '€70-85k', url
