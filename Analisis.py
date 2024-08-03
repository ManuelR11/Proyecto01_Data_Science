import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

def classify_variable(series):
    if series.dtype == 'object':
        return "Cualitativa (Categórica)"
    elif series.dtype in ['int64', 'float64']:
        if series.nunique() > 10 and (series % 1 != 0).any():
            return "Cuantitativa Continua"
        else:
            return "Cuantitativa Discreta"
    else:
        return "Tipo no reconocido"

def get_var_types(df):
    return {col: classify_variable(df[col]) for col in df.columns}

def get_var_names(df):
    return df.columns.tolist()

def get_null_values(df):
    return df.isnull().sum().to_dict()

def get_stats(df):
    stats = {}
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            stats[col] = {
                "Media": df[col].mean(),
                "Mediana": df[col].median(),
                "Moda": df[col].mode().values.tolist(),
                "Desviación estándar": df[col].std()
            }
    return stats




