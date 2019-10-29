#encoding: utf8
from decimal import Decimal
from datetime import datetime
from datapackage_pipelines.wrapper import ingest, spew

params, datapackage, res_iter = ingest()

columns = params.get('columns')

def process_resources(_res_iter):
    for rows in _res_iter:
        def process_rows(_rows):
            for row in _rows:
                row['obra_actividad'] = 'obra' if row['obra_id'] else ('actividad' if row['actividad_id'] else None)
                del row['obra_id']
                del row['actividad_id']
                yield row
        yield process_rows(rows)

def process_datapackage(datapackage):
    fields = [f 
              for f in datapackage['resources'][0]['schema']['fields']
              if f['name'] not in ('obra_id', 'actividad_id')]
    fields.append(dict(
        name='obra_actividad',
        title='obra_actividad',
        osType='activity:generic:subproject:type',
        type='string'
    ))
    datapackage['resources'][0]['schema']['fields'] = fields
    return datapackage

spew(process_datapackage(datapackage), 
     process_resources(res_iter))
