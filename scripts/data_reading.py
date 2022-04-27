#!/usr/bin/python

'''
Reading data from .xls and .csv files.
'''

import os
import re
import pandas as pd


def read_file(path: str) -> pd.DataFrame:

    _, file_extention = os.path.splitext(path)

    if file_extention == '.csv':
        df = pd.read_csv(path)
    elif file_extention == ('.xlsx' or '.xls'):
        df = pd.read_excel(path)

    return df


def fill_df(path: str) -> pd.DataFrame:

    for roots, _, files in os.walk(path):
        for file in files:

            file_path = os.path.join(roots, file)
            _, file_extention = os.path.splitext(file)

            if file_extention == '.csv':
                df = pd.read_csv(file_path, skiprows=[1, 2])

            elif file_extention == '.xlsx' or '.xls':
                df = pd.read_excel(file_path, skiprows=[1, 2])

            else:
                raise TypeError('Path contains not csv/xls files')



            data_f['file'] = file
            if 'Stick_Slip_Ratio' in data_f.columns:
                data_f.rename(columns=recolumn_2, inplace=True)
            else:
                data_f.rename(columns=recolumn_1, inplace=True)