from company_data import RemotePolicy
from helpers import scrape

name = 'Fraudio'
business = 'Fintech'


def remote_policy():
    '''Their remoteintech profile, which says they are a 'fully distributed' team'''
    url = 'https://github.com/remoteintech/remote-jobs/blob/main/company-profiles/fraudio.md'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.linkedin.com/company/fraudio/jobs/'
    return 'Europe', url


def funding():
    '''Funding information scraped from Crunchbase'''
    url = 'https://www.crunchbase.com/organization/fraudio'
    funding_info = scrape.crunchbase_funding(url)
    return funding_info, url
