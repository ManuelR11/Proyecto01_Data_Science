import os
import matplotlib.pyplot as plt
import seaborn as sns
import Analisis as an
import math 
import warnings

def filter_columns(df):
    filtered_columns = []
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64'] or (df[col].dtype == 'object' and df[col].nunique() < 50):
            filtered_columns.append(col)
    return filtered_columns

def suggest_plots(df):
    if not os.path.exists('graficos'):
        os.makedirs('graficos')
        
    print("Variables disponibles:")
    filtered_columns = filter_columns(df)
    for col in filtered_columns:
        print(col)
        
    var1 = input("Ingrese el nombre de la primera variable: ")
    var2 = input("Ingrese el nombre de la segunda variable: ")
    
    if var1 not in filtered_columns or var2 not in filtered_columns:
        print("Una o ambas variables no son válidas para graficar.")
        return
    
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

def null_values_to_plot(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Valores nulos en el conjunto de datos')
    plt.savefig(os.path.join('graficos', 'valores_nulos.png'))
    plt.show()

def plot_categorical_distributions(df, threshold=0.05):
    # Ignorar advertencias específicas
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=FutureWarning, message=".*is_categorical_dtype is deprecated.*")
        
        # Definir una lista para almacenar las columnas categóricas
        categorical_columns = []
        
        # Determinar si una columna es categórica
        for col in df.columns:
            unique_ratio = df[col].nunique() / len(df)
            if unique_ratio <= threshold:
                categorical_columns.append(col)
        
        num_categorical = len(categorical_columns)
        
        if num_categorical == 0:
            print("No se encontraron variables categóricas con el umbral especificado.")
            return
        
        # Determinar el tamaño de la cuadrícula
        cols = math.ceil(math.sqrt(num_categorical))
        rows = math.ceil(num_categorical / cols)
        
        # Crear una figura con subplots en una cuadrícula
        fig, axes = plt.subplots(rows, cols, figsize=(15, 10))
        axes = axes.flatten()
        
        # Graficar la distribución de las variables categóricas en subplots
        for i, col in enumerate(categorical_columns):
            sns.countplot(data=df, x=col, palette='viridis', ax=axes[i])
            axes[i].set_title(f'Distribución de la variable categórica: {col}')
            axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation=45)
        
        # Eliminar cualquier subplot no utilizado
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])
        
        plt.tight_layout()
        plt.savefig(os.path.join('graficos', 'distribucion_categorica.png'))
        plt.show()
        
    return categorical_columns
