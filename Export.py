import Analisis as an
import pandas as pd
import os 
import json

def save_analysis_to_json(df, folder='analisis_exploratorio', filename='analisis.json'):
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    analysis = {
        "Variables": an.get_var_names(df),
        "Tipos de variables": an.get_var_types(df),
        "Estadísticas": an.get_stats(df),
        "Valores nulos": an.get_null_values(df),
        "Porcentaje de valores nulos": an.null_percentage(df),
        "Resumen del dataframe": an.dataframe_summary(df)
    }
    
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, ensure_ascii=False, indent=4)