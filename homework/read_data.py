import pandas as pd

def read_data(name):
    return pd.read_csv(f"files/input/{name}", sep="\t")

def read_all_data():
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    tbl1 = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    tbl2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    
    # Retornar las tablas como un diccionario o cualquier otra estructura
    return tbl0, tbl1, tbl2
