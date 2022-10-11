from company_data import RemotePolicy
from helpers import scrape

name = 'GitLab'
business = 'DevOps'


def remote_policy():
    '''Extensive info about their remote culture'''
    url = 'https://about.gitlab.com/company/culture/all-remote/guide/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings for global and regional remote jobs'''
    url = 'https://about.gitlab.com/jobs/all-jobs/#Engineering'
    return 'global', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/GitLab-Engineering-Reviews-EI_IE1296544.0,6_DEPT1007.htm'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-GitLab-EI_IE1296544.11,17.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''A selection of the tech listed on stackshare.io'''
    url = 'https://stackshare.io/gitlab/gitlab'
    tech = 'js, ruby, go, postgres, redis, nginx, k8s'
    return tech, url


def salary():
    '''Senior Software Engineer in USA'''
    url = 'https://www.glassdoor.co.uk/Salary/GitLab-Senior-Software-Engineer-US-Salaries-EJI_IE1296544.0,6_KO7,31_IL.32,34_IN1.htm'
    return scrape.glassdoor_salary(url), url
