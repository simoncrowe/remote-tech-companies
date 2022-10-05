from company_data import RemotePolicy

name = "GitLab"
industry = "DevOps"


def remote_policy():
    """One of the largest remote-first companies."""
    return (RemotePolicy.REMOTE_FIRST,
            "https://about.gitlab.com/company/culture/all-remote/guide/")
