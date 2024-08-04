# __init__.py
# PySql.load.text/json/csv/xls(excel)/pkl(pickle)/yaml nebo yml/bin
import os

konfigurace = {
    'version': '2.0',
    'author': 'Danb1551',
    "description":"PySql is a tool for efficiently storing data in \nthe 'data' folder stored in the Windows root directory \nand then you can read that data and save it to a variable."
}

def initialize():
    for key, value in konfigurace.items():
        print(f"{key}: {value}")

adresar = "C:/data"
if not os.path.exists(adresar):
    os.makedirs(adresar)
else:
    existuje = True
