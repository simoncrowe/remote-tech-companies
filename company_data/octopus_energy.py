from company_data import RemotePolicy
from helpers import scrape

name = 'Octopus Energy'
business = 'Green Energy'


def remote_policy():
    '''A job spec that says that they will 'consider' remote candidates'''
    url = 'https://jobs.lever.co/octoenergy/ce50dbb9-5235-497a-ba29-1a04a9e714a7'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for in office jobs and regional remote jobs'''
    url = 'https://octopus.energy/careers/join-us/'
    return 'Europe, APAC', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Octopus-Energy-Engineering-Reviews-EI_IE1482748.0,14_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-Octopus-Energy-EI_IE1482748.11,25.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Tech listed on a blog post by Director of Engineering'''
    url = 'https://daniel.feldroy.com/posts/whats-the-best-thing-about-working-for-octopus-energy-part-1'
    tech = 'python, js, django, react, aws, terraform'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Octopus-Energy-Senior-Software-Engineer-Salaries-E1482748_D_KO15,39.htm'
    return scrape.glassdoor_salary(url), url
