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
    #obtener los valores nulos de cada columna y mostrar el porcentaje de nulos
    null_dict = {}
    for col in df.columns:
        null_count = df[col].isnull().sum()
        null_dict[col] = null_count
    return null_dict

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

def null_percentage(df):
    return df.isnull().mean() * 100


def dataframe_summary(df):
    # Número de variables (columnas)
    num_variables = df.shape[1]
    
    # Número de observaciones (filas)
    num_observations = df.shape[0]
    
    # Filas duplicadas
    duplicate_rows = df.duplicated().sum()
    
    # Filas duplicadas (%)
    duplicate_rows_percentage = (duplicate_rows / num_observations) * 100
    
    # Celdas faltantes
    missing_cells = df.isnull().sum().sum()
    
    # Celdas faltantes (%)
    total_cells = num_variables * num_observations
    missing_cells_percentage = (missing_cells / total_cells) * 100
    aprox = round(missing_cells_percentage, 2)
    
    
    summary = {
        'Numero de variables': num_variables,
        'Numero de observaciones': num_observations,
        'Celdas Faltantes ': missing_cells,
        'Celdas Faltantes (%)': aprox,
        'Filas duplicadas': duplicate_rows,
        'Filas duplicadas (%)': duplicate_rows_percentage
    }
    
    return summary