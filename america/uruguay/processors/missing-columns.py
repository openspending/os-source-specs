#encoding: utf8
import os
import csv

from datapackage_pipelines.wrapper import ingest, spew

params, datapackage, res_iter = ingest()

columns = params.get('columns')


new_columns = [
    'activ_prj_label',
    'admin_1_label',
    'admin_2_label',
    'func_1_label',
    'func_2_label',
    'activ_prj_label',
    'finsrc_1_label',
    'finsrc_2_label',
    'exp_type_label',
    'econ_1_label',
    'econ_2_label',
    'econ_3_label',
    'activ_program_code',
    'activ_program_label',
    'activ_subprogram_code',
    'activ_subprogram_label',
]

field_names = [f['name'] for f in datapackage['resources'][0]['schema']['fields']]

for column in new_columns:
    if column not in field_names:
        datapackage['resources'][0]['schema']['fields'].append({
            'name': column,
            'type': 'string'
        })


def lookup(key, catalog, year):
    return lookup_map[catalog].get(key.strip())


def process_row(row):

    columns = ['admin_1', 'admin_2',
               'func_1', 'func_2',
               'activ_prj',
               'finsrc_1', 'finsrc_2',
               'exp_type',
               'econ_1', 'econ_2', 'econ_3']

    for column in columns:
        column_label = '{}_label'.format(column)
        column_code = '{}_code'.format(column)
        if not row[column_label]:
            row[column_label] = row[column_code]
    row['activ_program_code'] = row['func_1_code']
    row['activ_program_label'] = row['func_1_label']
    row['activ_subprogram_code'] = row['func_2_code']
    row['activ_subprogram_label'] = row['func_2_label']

    return row


def process_resources(_res_iter):
    for rows in _res_iter:
        def process_rows(_rows):
            for row in _rows:
                yield process_row(row)
        yield process_rows(rows)

spew(datapackage, process_resources(res_iter))
