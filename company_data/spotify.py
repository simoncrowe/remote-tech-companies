from company_data import RemotePolicy
from helpers import scrape

name = 'Spotify'
business = 'Streaming'


def remote_policy():
    '''A web page stating that employees can work from anywhere'''
    url = 'https://www.lifeatspotify.com/being-here/work-from-anywhere'
    return RemotePolicy.REMOTE_FRIENDLY, url


def hiring_region():
    '''Listings for regional remote jobs'''
    url = 'https://www.lifeatspotify.com/jobs'
    return 'Americas, APAC EMEA', url


def engineering_glassdoor_rating():
    '''Average glassdoor rating for engineers'''
    url = 'https://www.glassdoor.co.uk/Reviews/Spotify-Engineering-Reviews-EI_IE408251.0,7_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME'
    return scrape.glassdoor_engineering_rating(url), url


def overall_glassdoor_rating():
    '''Overall average glassdoor rating'''
    url = 'https://www.glassdoor.co.uk/spotify'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    '''Selected tech from stackshare.io'''
    url = 'https://stackshare.io/spotify/spotify'
    tech = 'python, java, postgres, cassandra, kafka, aws'
    return tech, url


def salary():
    '''Senior Software Engineer based in UK'''
    url = 'https://www.glassdoor.co.uk/Salary/Spotify-Senior-Software-Engineer-Salaries-E408251_D_KO8,32.htm'
    return scrape.glassdoor_salary(url), url
