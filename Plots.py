import os
import matplotlib.pyplot as plt
import seaborn as sns
import Analisis as an

def suggest_plots(df):
    if not os.path.exists('graficos'):
        os.makedirs('graficos')
        
    print("Variables disponibles:")
    var_names = an.get_var_names(df)
    for col in var_names:
        print(col)
        
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
