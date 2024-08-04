import csv as cv
import json as jsn
import pandas as pd
import pickle
import yaml as yml
import h5py
import zipfile

# Kořenový adresář pro data
root_dir = "C:/data/"

def txt(file_path):
    """Čte textový soubor."""
    file_path = root_dir + file_path
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def csv(file_path):
    """Čte CSV soubor."""
    file_path = root_dir + file_path
    with open(file_path, newline='') as csvfile:
        reader = cv.reader(csvfile)
        data = [row for row in reader]
    return data

def json(file_path):
    """Čte JSON soubor."""
    file_path = root_dir + file_path
    with open(file_path, 'r') as file:
        data = jsn.load(file)
    return data

def xls(file_path):
    """Čte Excel soubor (.xls a .xlsx)."""
    file_path = root_dir + file_path
    df = pd.read_excel(file_path)
    return df

def pkl(file_path):
    """Čte Pickle soubor."""
    file_path = root_dir + file_path
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def yaml(file_path):
    """Čte YAML soubor."""
    file_path = root_dir + file_path
    with open(file_path, 'r') as file:
        data = yml.safe_load(file)
    return data

def h5(file_path):
    """Čte HDF5 soubor."""
    file_path = root_dir + file_path
    with h5py.File(file_path, 'r') as file:
        data = {key: file[key][()] for key in file.keys()}
    return data

def zip(file_path, extract_to=root_dir):
    """Rozbaluje ZIP soubor."""
    file_path = root_dir + file_path
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return f"Files extracted to {extract_to}"

def bin(file_path):
    """Čte binární soubor."""
    file_path = root_dir + file_path
    with open(file_path, 'rb') as file:
        data = file.read()
    return data