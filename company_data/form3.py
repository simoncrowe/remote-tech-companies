from company_data import RemotePolicy
from helpers import scrape

name = "Form3"
business = 'Legal Docs'


def remote_policy():
    '''A blog post describing their remote culture'''
    url = 'https://www.form3.tech/why-form3/insights/a-remote-first-culture'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    '''Listings regional remote jobs'''
    url = 'https://www.form3.tech/careers/vacancies'
    return 'Americas, Europe', url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Form3-Financial-Cloud-EI_IE2008415.11,32.htm'
    return scrape.glassdoor_rating(url), url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Form3-Financial-Cloud-Engineering-Reviews-EI_IE2008415.0,21_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/form3/main'
    tech = 'java, go, postgres, redis, cockroachdb, ansible, k8s, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Form3-Financial-Cloud-Senior-Software-Engineer-Salaries-E2008415_D_KO22,46.htm'
    return scrape.glassdoor_salary(url), url
