#encoding: utf8
from datetime import datetime
from datapackage_pipelines.wrapper import ingest, spew

params, datapackage, res_iter = ingest()

columns = params.get('columns')

months = {
    'enero': '01',
    'febrero': '02',
    'marzo': '03',
    'abril': '04',
    'mayo': '05',
    'junio': '06',
    'julio': '07',
    'agosto': '08',
    'septiembre': '09',
    'setiembre': '09',
    'octubre': '10',
    'noviembre': '11',
    'diciembre': '12',
}


def clean_value(v):
    constant_phrase = 'Última actualización del ejercicio 2019: '
    if constant_phrase in v:
        v = v.replace(constant_phrase, '')[:-1]

    parts = v.split(' ')
    if parts[1].lower() in months.keys():
        parts[1] = months[parts[1].lower()]
    v = '-'.join(parts)

    date_value = datetime.strptime(v, '%d-%m-%Y')
    return date_value.strftime('%Y-%m-%d')


def process_resources(_res_iter):
    for rows in _res_iter:
        def process_rows(_rows):
            for row in _rows:
                yield dict((k, v if k not in columns else clean_value(v)) for (k, v)
                           in row.items())
        yield process_rows(rows)

spew(datapackage, process_resources(res_iter))
