#encoding: utf8
from datapackage_pipelines.wrapper import ingest, spew

params, datapackage, res_iter = ingest()

columns = params.get('columns')

def format_number(value):
    if not value:
        return ''

    parts = value.split(',')
    integer = parts[0].replace('.', '')

    try:
        decimals = parts[1]
    except IndexError:
        decimals = '00'

    new_value = '{}.{}'.format(integer, decimals)
    return new_value


def process_resources(_res_iter):
    for rows in _res_iter:
        def process_rows(_rows):
            for row in _rows:
                yield dict((k, v if k not in columns else format_number(v)) for (k, v)
                           in row.items())
        yield process_rows(rows)

spew(datapackage, process_resources(res_iter))
