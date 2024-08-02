import pandas as pd
from ydata_profiling import ProfileReport

# Cargar datos
df = pd.read_csv('netflix_titles.csv')

# Generar reporte
profile = ProfileReport(df, title="Reporte de Análisis Exploratorio")
profile.to_file("reporte_eda.html")
