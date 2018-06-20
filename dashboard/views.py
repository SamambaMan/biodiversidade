from django.shortcuts import render
from django.db import connection

_QUERY_STATUS_POR_CATEGORIA = """
select chm.classname, count(*)
from sample smp
inner join tlcdata tlc on 
    tlc.sampleid = smp.sampleid
inner join chemical_classes chm on
    chm.chemclassid = tlc.chemclassid
where smp.type = 'extract'
group by chm.classname
"""

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def index(request):
    with connection.cursor() as cursor:
        cursor.execute(_QUERY_STATUS_POR_CATEGORIA)

        resultados = dictfetchall(cursor)

    return render(
        request,
        'dashboard/index.html',
        {'resultados': resultados}
    )
