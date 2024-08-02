import pandas as pd
import Analisis

# Cargar el archivo de datos
name = input("Ingrese el nombre del archivo de datos: ")
df = pd.read_csv(name)

# Imprimir las variables del archivo
print("Variables del archivo:")
Analisis.print_var_name(df)

print("\nTipo de variables:")
Analisis.print_var(df)

print("\nValores nulos:")
Analisis.print_null_values(df)

print("\nEstadísticas de variables numéricas:")
Analisis.print_stats(df)

print("\nSugerencias de gráficos:")
Analisis.suggest_plots(df)

# Guardar el análisis en un archivo json
Analisis.save_analysis_to_json(df)