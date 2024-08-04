import csv as cv
import json as jsn
import pandas as pd
import pickle
import yaml as yml
import h5py

# Kořenový adresář pro data
root_dir = "C:/data/"

def txt(data, file_path):
    """Ukládá data do textového souboru."""
    file_path = root_dir + file_path
    with open(file_path, 'w') as file:
        file.write(data)
    return file_path

def csv(data, file_path):
    """Ukládá data do CSV souboru."""
    file_path = root_dir + file_path
    with open(file_path, 'w', newline='') as csvfile:
        writer = cv.writer(csvfile)
        writer.writerows(data)
    return file_path

def json(data, file_path):
    """Ukládá data do JSON souboru."""
    file_path = root_dir + file_path
    with open(file_path, 'w') as file:
        jsn.dump(data, file)
    return file_path

def xls(data, file_path):
    """Ukládá data do Excel souboru (.xls a .xlsx)."""
    file_path = root_dir + file_path
    data.to_excel(file_path, index=False)
    return file_path

def pkl(data, file_path):
    """Ukládá data do Pickle souboru."""
    file_path = root_dir + file_path
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)
    return file_path

def yaml(data, file_path):
    """Ukládá data do YAML souboru."""
    file_path = root_dir + file_path
    with open(file_path, 'w') as file:
        yml.safe_dump(data, file)
    return file_path

def h5(data, file_path):
    """Ukládá data do HDF5 souboru."""
    file_path = root_dir + file_path
    with h5py.File(file_path, 'w') as file:
        for key, value in data.items():
            file.create_dataset(key, data=value)
    return file_path

def bin(data, file_path):
    """Ukládá data do binárního souboru."""
    file_path = root_dir + file_path
    with open(file_path, 'wb') as file:
        file.write(data)
    return file_path
