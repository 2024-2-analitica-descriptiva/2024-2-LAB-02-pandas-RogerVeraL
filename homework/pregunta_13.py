"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    import pandas as pd
    import homework.read_data as rd
    tbl0 = rd.read_data("tbl0.tsv")
    tbl2 = rd.read_data("tbl2.tsv")
    tabla = (pd.merge(tbl0, tbl2, on="c0")
             .groupby("c1")["c5b"]
             .sum())
    return tabla
print(pregunta_13())
