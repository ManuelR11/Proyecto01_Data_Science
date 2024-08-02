import pandas as pd
import Analisis

# Cargar el archivo de datos
name = input("Ingrese el nombre del archivo de datos: ")
df = pd.read_csv(name)

# Imprimir las variables del archivo
print("Variables del archivo:")
variables = Analisis.get_var_names(df)
for var in variables:
    print(var)

print("\nTipo de variables:")
tipos_var = Analisis.get_var_types(df)
for var, tipo in tipos_var.items():
    print(f"{var}: {tipo}")

print("\nValores nulos:")
nulos = Analisis.get_null_values(df)
for var, nulo in nulos.items():
    print(f"{var}: {nulo}")

print("\nEstadísticas de variables numéricas:")
estadisticas = Analisis.get_stats(df)
for var, stats in estadisticas.items():
    print(f"{var}:")
    for stat, value in stats.items():
        print(f"{stat}: {value}")

print("\nSugerencias de gráficos:")
Analisis.suggest_plots(df)

# Guardar el análisis en un archivo json
Analisis.save_analysis_to_json(df)
