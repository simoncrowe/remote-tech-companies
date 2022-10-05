from importlib import import_module

from pytablewriter import MarkdownTableWriter

import company_data

README_FILENAME = "README.md"
TABLE_START = '<!--- START TABLE --->'
TABLE_END = '<!--- END TABLE --->'
COLUMNS = {
   'name': 'Name',
   'industry': 'Industry',
   'remote_policy': 'Remote Policy',
}


def render_markup(data_source):
    if callable(data_source):
        value, link = data_source()
        tooltip = data_source.__doc__ or ''
        return f'[{value}]({link} "{tooltip}")'
    return data_source


def iter_values(module):
    for name in COLUMNS.keys():
        if data_source := getattr(module, name, None):
            yield render_markup(data_source)
        else:
            yield ''


def iter_data():
    for name in company_data.MODULE_NAMES:
        module = import_module(".".join(("company_data", name)))
        yield iter_values(module)


def update_readme(data):
    with open(README_FILENAME) as fileobj:
        readme = fileobj.read()
    start = readme.find(TABLE_START) + len(TABLE_START) + 1
    end = readme.find(TABLE_END) - 1
    assert end > start > -1, "Table start/end comments are broken!"

    val_matrix = [tuple(row_vals) for row_vals in data]
    writer = MarkdownTableWriter(table_name="Company Data",
                                 headers=COLUMNS.values(),
                                 value_matrix=val_matrix)

    with open(README_FILENAME, "w") as fileobj:
        fileobj.write('\n'.join((readme[:start],
                                 writer.dumps(),
                                 readme[end:])))


if __name__ == "__main__":
    update_readme(iter_data())
