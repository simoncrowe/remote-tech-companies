import os
import time
from datetime import timedelta
from importlib import import_module
from os import path

from pytablewriter import MarkdownTableWriter

import company_data

CACHE_DIRPATH = './.cache'
CACHE_LIFETIME = timedelta(days=90).total_seconds()
README_FILENAME = 'README.md'
TABLE_START = '<!--- START TABLE --->'
TABLE_END = '<!--- END TABLE --->'
COLUMNS = {
    'name': 'Name',
    'business': 'Business',
    'remote_policy': 'Remote Policy',
    'hiring_region': 'Hiring Region',
    'engineering_glassdoor_rating': 'Eng. Glassdoor Rating',
    'overall_glassdoor_rating': 'Glassdoor Rating',
    'tech_stack': 'Tech',
    'salary': 'Pay',
}


def render_markdown(data_source):
    if callable(data_source):
        value, link = data_source()
        if tooltip := data_source.__doc__:
            return f'[{value}]({link} "{tooltip}")'
        else:
            return f'[{value}]({link})'
    return data_source


def get_data(module, name):
    data_key = f'{module.__name__}.{name}'
    cache_path = path.join(CACHE_DIRPATH, data_key)
    if (
        path.exists(cache_path) and
        time.time() - path.getmtime(cache_path) < CACHE_LIFETIME
    ):
        print(f'{data_key} found in cache. Using cached value...')
        with open(cache_path, 'r') as fileobj:
            return fileobj.read()

    if data_source := getattr(module, name, None):
        markdown = render_markdown(data_source)
        with open(cache_path, 'w') as fileobj:
            fileobj.write(markdown)
        return markdown
    else:
        return ''


def iter_values(module):
    for name in COLUMNS.keys():
        yield get_data(module, name)


def iter_data():
    for name in company_data.MODULE_NAMES:
        module = import_module('.'.join(('company_data', name)))
        yield iter_values(module)


def update_readme(data):
    with open(README_FILENAME) as fileobj:
        readme = fileobj.read()
    start = readme.find(TABLE_START) + len(TABLE_START) + 1
    end = readme.find(TABLE_END) - 1
    assert end > start > -1, 'Table start/end comments are broken!'

    val_matrix = [tuple(row_vals) for row_vals in data]
    writer = MarkdownTableWriter(table_name='Company Data',
                                 headers=COLUMNS.values(),
                                 value_matrix=val_matrix)

    with open(README_FILENAME, 'w') as fileobj:
        fileobj.write('\n'.join((readme[:start],
                                 writer.dumps(),
                                 readme[end:])))


if __name__ == '__main__':
    if not path.exists(CACHE_DIRPATH):
        os.mkdir(CACHE_DIRPATH)

    update_readme(iter_data())
