import pandas as pd
import Analisis
import Plots
import Export



print("Bienvenido al programa de análisis de datos.")
print("Este programa te permitirá cargar un archivo de datos y realizar un análisis exploratorio de los mismos.")
Salir = False 
# Cargar el archivo de datos
try:
    name = input("Ingrese el nombre del archivo de datos: \n")
    df = pd.read_csv(name)
        
except FileNotFoundError:
    print("El archivo no existe, por favor ingrese un archivo válido.")


while not Salir:
    print('\n\nPor favor seleccione una de las siguientes opciones:')
    print('1. Imprimir las variables del archivo.')
    print('2. Visualizar los valores nulos.')
    print('3. Imprimir las estadísticas de las variables numéricas.')
    print('4. Sugerencias de gráficos.')
    print('5. Observaciones generales')
    print('6. Salir.')
    opcion = int(input('Opción: '))

    if opcion == 1:
        print("\n-------------Tipos de variables-------------")
        var = Analisis.get_var_types(df)
        for variable, tipo in var.items():
            print(f"{variable}: {tipo}")

        desicion = input("Desea visualizar la distribuicion de las variables categoricas? ")
        if desicion == "si" or desicion == "Si" or desicion == "SI":
            Plots.plot_categorical_distributions(df)
        else:
            print("No se exportaron las variables categoricas a una grafica")


    elif opcion == 2:
        print("\n----------------Valores nulos----------------")
        null_dict = Analisis.get_null_values(df)
        for var, null_count in null_dict.items():
            percentage = (null_count / df.shape[0]) * 100
            print(f"{var}: {null_count} valores nulos, {percentage:.2f}%")

        desicion = input("Desea visualizar los valores nulos en una grafica? ")
        if desicion == "si" or desicion == "Si" or desicion == "SI":
            Plots.null_values_to_plot(df)
        else:
            print("No se exportaron los valores nulos a una grafica")

    elif opcion == 3:
        print("\n----------------Estadísticas de variables numéricas----------------")
        estadisticas = Analisis.get_stats(df)
        for var, stats in estadisticas.items():
            print(f"{var}:")
            for stat, value in stats.items():
                print(f"{stat}: {value}")

    elif opcion == 4:
        print("\n-------------------Sugerencias de gráficos-------------------")
        Analisis.suggest_plots(df)

    elif opcion == 5:
        summary = Analisis.dataframe_summary(df)
        print("\n-------------------Observaciones generales-------------------")
        for key, value in summary.items():
            print(f"{key}: {value}")


    elif opcion == 6:
        Salir = True
        print("\nGracias por usar el programa.")
        print("Los que hacen el trabajo pesado son:")
        print("Jose Santisteban \nManuel Rodas \nSol")

    else:
        print("Opción no válida. Por favor seleccione una opción válida.")
    

    




