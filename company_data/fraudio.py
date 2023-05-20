from company_data import RemotePolicy

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
