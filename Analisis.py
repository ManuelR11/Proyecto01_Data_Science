import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

# Funcion para identificar variables categoricas y numericas de un csv
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

def print_var(df):
    variable_types = {col: classify_variable(df[col]) for col in df.columns}
    
    for var, tipo in variable_types.items():
        print(f"{var}: {tipo}")

# Funcion para imprimir el nombre de las variables
def print_var_name(df):
    for col in df.columns:
        print(col)

# Funcion para imprimir los valores nulos
def print_null_values(df):
    print(df.isnull().sum())

# Funcion para imprimir la media, mediana, moda, desviación estándar de variables numericas
def print_stats(df):
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            print(f"{col}:")
            print(f"Media: {df[col].mean()}")
            print(f"Mediana: {df[col].median()}")
            print(f"Moda: {df[col].mode().values}")
            print(f"Desviación estándar: {df[col].std()}")
            print()

# Funcion para guardar el analisis en un archivo json
def save_analysis_to_json(df, folder='analisis_exploratorio', filename='analisis.json'):
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    analysis = {
        "Tipos de variables": print_var(df),
        "Nombres de variables": print_var_name(df),
        "Valores nulos": print_null_values(df),
        "Estadísticas": print_stats(df)
    }
    
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, ensure_ascii=False, indent=4)

# Funcion donde se seleccionen dos variables y sugerir graficos
def suggest_plots(df):
    if not os.path.exists('graficos'):
        os.makedirs('graficos')
        
    print("Variables disponibles:")
    print_var_name(df)
    var1 = input("Ingrese el nombre de la primera variable: ")
    var2 = input("Ingrese el nombre de la segunda variable: ")
    
    suggestions = []

    if df[var1].dtype == 'object' and df[var2].dtype == 'object':
        suggestions = ["Diagrama de barras", "Diagrama de sectores"]
    elif df[var1].dtype in ['int64', 'float64'] and df[var2].dtype == 'object':
        suggestions = ["Diagrama de caja", "Histograma"]
    elif df[var1].dtype == 'object' and df[var2].dtype in ['int64', 'float64']:
        suggestions = ["Diagrama de caja", "Histograma"]
    elif df[var1].dtype in ['int64', 'float64'] and df[var2].dtype in ['int64', 'float64']:
        suggestions = ["Diagrama de dispersión", "Diagrama de línea"]
    else:
        print("No se puede sugerir un gráfico para las variables ingresadas")
        return
    
    print("Sugerencias:")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"{i}. {suggestion}")

    choice = int(input("Ingrese el número del gráfico que desea ver (1 o 2): "))
    
    if choice not in [1, 2]:
        print("Elección no válida")
        return
    
    selected_plot = suggestions[choice - 1]
    
    if selected_plot == "Diagrama de barras":
        plt.figure(figsize=(10, 6))
        sns.countplot(x=var1, hue=var2, data=df)
        plt.title(f'Diagrama de barras de {var1} y {var2}')
        plt.savefig(os.path.join('graficos', 'diagrama_barras.png'))
        plt.show()

    elif selected_plot == "Diagrama de sectores":
        plt.figure(figsize=(8, 8))
        df[var1].value_counts().plot.pie(autopct='%1.1f%%')
        plt.title(f'Diagrama de sectores de {var1}')
        plt.ylabel('')
        plt.savefig(os.path.join('graficos', 'diagrama_sectores.png'))
        plt.show()

    elif selected_plot == "Diagrama de caja":
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=var2, y=var1, data=df)
        plt.title(f'Diagrama de caja de {var1} y {var2}')
        plt.savefig(os.path.join('graficos', 'diagrama_caja.png'))
        plt.show()

    elif selected_plot == "Histograma":
        plt.figure(figsize=(10, 6))
        sns.histplot(df[var1], bins=30)
        plt.title(f'Histograma de {var1}')
        plt.savefig(os.path.join('graficos', 'histograma.png'))
        plt.show()

    elif selected_plot == "Diagrama de dispersión":
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=var1, y=var2, data=df)
        plt.title(f'Diagrama de dispersión de {var1} y {var2}')
        plt.savefig(os.path.join('graficos', 'diagrama_dispersion.png'))
        plt.show()

    elif selected_plot == "Diagrama de línea":
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=var1, y=var2, data=df)
        plt.title(f'Diagrama de línea de {var1} y {var2}')
        plt.savefig(os.path.join('graficos', 'diagrama_linea.png'))
        plt.show()
