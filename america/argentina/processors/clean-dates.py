#encoding: utf8
import locale
from datetime import datetime
from datapackage_pipelines.wrapper import ingest, spew

locale.setlocale(locale.LC_ALL, 'es_AR')

params, datapackage, res_iter = ingest()

columns = params.get('columns')


def clean_value(v):
    constant_phrase = 'Última actualización del ejercicio 2019: '
    if constant_phrase in v:
        v = v.replace(constant_phrase, '')[:-1]
    date_value = datetime.strptime(v, '%d %B %Y')
    return date_value.strftime('%Y-%m-%d')


def process_resources(_res_iter):
    for rows in _res_iter:
        def process_rows(_rows):
            for row in _rows:
                yield dict((k, v if k not in columns else clean_value(v)) for (k, v)
                           in row.items())
        yield process_rows(rows)

spew(datapackage, process_resources(res_iter))
