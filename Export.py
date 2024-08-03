import Analisis as an
import pandas as pd
import os 
import json


def save_analysis_to_json(df, folder='analisis_exploratorio', filename='analisis.json'):
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    analysis = {
        "Tipos de variables": an.get_var_types(df),
        "Nombres de variables": an.get_var_names(df),
        "Valores nulos": an.get_null_values(df),
        "Estadísticas": an.get_stats(df)
    }
    
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, ensure_ascii=False, indent=4)