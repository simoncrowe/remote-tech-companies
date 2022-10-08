Below is information on tech companies that hire remotely, mainly intended for
job seeking software engineers.

There is a mixture of manually gathered data and things like average ratings
and salaries that are automatically scraped and periodically updated.
Hyperlinked data lead to their sources. Most hyperlinks also contain
tooltips you can view by hovering over them.

<!--- START TABLE --->

# Company Data
| Name |    Business     |                                                                     Remote Policy                                                                      |                                               Hiring Region                                                |                                                                                                        Eng. Glassdoor Rating                                                                                                        |                                                   Glassdoor Rating                                                    |                                                                                     Tech                                                                                      |                                                                                       Pay                                                                                       |
|------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Planet|Satellite Imaging|[remote-friendly](https://www.planet.com/pulse/making-space-for-everyone-how-planet-is-building-a-global-workforce/ "Article about their remote hiring")|[APAC, Americas, EMEA](https://www.planet.com/company/careers/ "Listings for regional remote jobs")         |[4.9](https://www.glassdoor.co.uk/Reviews/Planet-Engineering-Reviews-EI_IE827495.0,6_DEPT1007.htm?filter.iso3Language=eng&filter.employmentStatus=REGULAR&filter.employmentStatus=PART_TIME "Average glassdoor rating for engineers")|[4.4](https://www.glassdoor.co.uk/Overview/Working-at-Planet-EI_IE827495.11,17.htm "Overall average glassdoor rating") |[js, python, go, c++, c, postgres, mysql, nginx,  ansible, terraform, k8s](https://himalayas.app/companies/planet/tech-stack "A selection of the tech listed on himalayas.app")|[$160K](https://www.levels.fyi/companies/planet/salaries/software-engineer "L4 Software Engineer in USA")                                                                        |
|GitLab|DevOps           |[remote-first](https://about.gitlab.com/company/culture/all-remote/guide/ "Extensive info about their remote culture")                                  |[global](https://about.gitlab.com/jobs/all-jobs/#Engineering "Listings for global and regional remote jobs")|[4.5](https://www.glassdoor.co.uk/Reviews/GitLab-Engineering-Reviews-EI_IE1296544.0,6_DEPT1007.htm "Average glassdoor rating for engineers")                                                                                         |[4.5](https://www.glassdoor.co.uk/Overview/Working-at-GitLab-EI_IE1296544.11,17.htm "Overall average glassdoor rating")|[js, ruby, go, postgres, redis, nginx, k8s](https://stackshare.io/gitlab/gitlab "A selection of the tech listed on stackshare.io")                                             |[$118,684 - $157,000](https://www.glassdoor.co.uk/Salary/GitLab-Senior-Software-Engineer-US-Salaries-EJI_IE1296544.0,6_KO7,31_IL.32,34_IN1.htm "Senior Software Engineer in USA")|


<!--- END TABLE --->

# Contributing
## How to add a company
To add a company to the table, create a module in the `company_data` directory.

Here is an example some example module contents that you can copy
and modify:

```python
from company_data import RemotePolicy
from helpers import scrape

name = "GitLab"
business = "DevOps"


def remote_policy():
    """Extensive info about their remote culture"""
    url = 'https://about.gitlab.com/company/culture/all-remote/guide/'
    return RemotePolicy.REMOTE_FIRST, url


def hiring_region():
    """Listings for global and regional remote jobs"""
    url = "https://about.gitlab.com/jobs/all-jobs/#Engineering"
    return "global", url


def engineering_glassdoor_rating():
    """Average glassdoor rating for engineers"""
    url = 'https://www.glassdoor.co.uk/Reviews/GitLab-Engineering-Reviews-EI_IE1296544.0,6_DEPT1007.htm'
    return scrape.glassdoor_rating(url), url


def overall_glassdoor_rating():
    """Overall average glassdoor rating"""
    url = 'https://www.glassdoor.co.uk/Overview/Working-at-GitLab-EI_IE1296544.11,17.htm'
    return scrape.glassdoor_rating(url), url


def tech_stack():
    """A selection of the tech listed on stackshare.io"""
    url = "https://stackshare.io/gitlab/gitlab"
    tech = 'js, ruby, go, postgres, redis, nginx, k8s'
    return tech, url


def salary():
    """Senior Software Engineer in USA"""
    url = 'https://www.glassdoor.co.uk/Salary/GitLab-Senior-Software-Engineer-US-Salaries-EJI_IE1296544.0,6_KO7,31_IL.32,34_IN1.htm'
    return scrape.glassdoor_salary_range(url), url
```

To update the above table, run:
```sh
python update_readme_table.py
```

## Note regarding the code
The Python code in this repo is not written to a professional standard.
The naming of functions and modules is unorthodox and there are no tests,
type hints or logging.

This is intentional. Python is used here as a scripting language,
so brevity, simplicity and expressiveness take centre stage.
