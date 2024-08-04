# __init__.py

import os

konfigurace = {
    'version': '1.0',
    'author': 'Danb1551',
    "description":"PySql is a tool for efficiently storing data in \nthe 'data' folder stored in the Windows root directory \nand then you can read that data and save it to a variable."
}

def initialize():
    for key, value in konfigurace.items():
        print(f"{key}: {value}")


def save(data, name):
    name = "C:/data/" + name
    with open(name, "w") as file:
        file.write(data)

def load(name):
    with open(name, "r") as file:
        data = file.read()
    return data

adresar = "C:/data"
if not os.path.exists(adresar):
    os.makedirs(adresar)
else:
    existuje = True