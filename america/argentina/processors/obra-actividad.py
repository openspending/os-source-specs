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
                yield row
        yield process_rows(rows)

spew(datapackage, process_resources(res_iter))
