from company_data import RemotePolicy
from helpers import scrape

name = "GitLab"
industry = "DevOps"


def remote_policy():
    """One of the largest remote-first companies."""
    url = 'https://about.gitlab.com/company/culture/all-remote/guide/'
    return RemotePolicy.REMOTE_FIRST, url


def overall_glassdoor_rating():
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-GitLab-EI_IE1296544.11,17.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    url = 'https://www.glassdoor.co.uk/Reviews/GitLab-Engineering-Reviews-EI_IE1296544.0,6_DEPT1007.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    """Based on stackshare.io"""
    url = "https://stackshare.io/gitlab/gitlab"
    tech = 'js, ruby, go, postgres, redis, nginx, k8s'
    return tech, url
