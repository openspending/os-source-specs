#encoding: utf8
from decimal import Decimal
from datetime import datetime
from datapackage_pipelines.wrapper import ingest, spew

params, datapackage, res_iter = ingest()

fields = params.get('fields')

def process_resources(_res_iter):
    for rows in _res_iter:
        def process_rows(_rows):
            for row in _rows:
                for item in fields:
                    for parent, child in zip(item[:-1], item[1:]):
                        row[child] = row[parent] + '/' + row[child]
                yield row
        yield process_rows(rows)

spew(datapackage, process_resources(res_iter))
