#encoding: utf8
from decimal import Decimal
from datetime import datetime
from datapackage_pipelines.wrapper import ingest, spew

params, datapackage, res_iter = ingest()

columns = params.get('columns')

def fix_amount(v):
    v = v.replace(',', '.')
    return Decimal(v) * 1000000


def process_resources(_res_iter):
    for rows in _res_iter:
        def process_rows(_rows):
            for row in _rows:
                yield dict((k, v if k not in columns else fix_amount(v)) for (k, v)
                           in row.items())
        yield process_rows(rows)

spew(datapackage, process_resources(res_iter))
