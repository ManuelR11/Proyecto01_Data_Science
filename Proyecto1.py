import pandas as pd
import Analisis
import Plots
import Export



print("Bienvenido al programa de análisis de datos.")
print("Este programa te permitirá cargar un archivo de datos y realizar un análisis exploratorio de los mismos.")
Salir = False 
# Cargar el archivo de datos
try:
    name = input("Ingrese el nombre del archivo de datos: ")
    df = pd.read_csv(name)
        
except FileNotFoundError:
    print("El archivo no existe, por favor ingrese un archivo válido.")


while not Salir:
    print('Por favor seleccione una de las siguientes opciones:')
    print('1. Imprimir las variables del archivo.')
    print('2. Visualizar los valores nulos.')
    print('3. Imprimir las estadísticas de las variables numéricas.')
    print('4. Sugerencias de gráficos.')
    print('5. Salir.')
    opcion = int(input('Opción: '))

    if opcion == 1:
        print("Variables del archivo:")
        variables = Analisis.get_var_names(df)
        for var in variables:
            print(var)

    elif opcion == 2:
        print("Valores nulos:")
        nulos = Analisis.get_null_values(df)
        for var, nulo in nulos.items():
            print(f"{var}: {nulo}")

    elif opcion == 3:
        print("Estadísticas de variables numéricas:")
        estadisticas = Analisis.get_stats(df)
        for var, stats in estadisticas.items():
            print(f"{var}:")
            for stat, value in stats.items():
                print(f"{stat}: {value}")

    elif opcion == 4:
        print("Sugerencias de gráficos:")
        Analisis.suggest_plots(df)

    elif opcion == 5:
        Salir = True
        print("Gracias por usar el programa.")
    

    






# Guardar el análisis en un archivo json
Analisis.save_analysis_to_json(df)
