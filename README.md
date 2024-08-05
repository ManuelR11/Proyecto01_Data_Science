# Proyecto01_Data_Science

# Proyecto de Análisis Exploratorio Automatizado

## Descripción del Proyecto
En esta fase del proyecto se pretende desarrollar una interfaz (en consola o gráfica) que permita la carga de archivos .csv y realice análisis exploratorio automatizado. El sistema debe generar estadísticas descriptivas, identificar variables categóricas y numéricas, detectar valores nulos y sugerir gráficos apropiados según el tipo de datos.

## Requisitos
- Python 3.x
- Pandas
- Matplotlib
- Seaborn

## Instrucciones de Uso

### 1. Bienvenida e Ingreso del Archivo de Datos
Al iniciar el programa, se pedirá al usuario que ingrese el nombre del archivo .csv que desea analizar. El archivo debe estar en el mismo directorio que el script o debe especificarse la ruta completa.

```python
print("Bienvenido al programa de análisis de datos.")
name = input("Ingrese el nombre del archivo de datos: \n")
df = pd.read_csv(name)
```


### Opciones del Menú
El programa presenta un menú con varias opciones para analizar los datos cargados:

#### 2.1. Imprimir las variables del archivo
Muestra los nombres y tipos de las variables en el archivo de datos.

```python
var = Analisis.get_var_types(df)
for variable, tipo in var.items():
    print(f"{variable}: {tipo}")
```

#### 2.3. Imprimir las estadísticas de las variables numéricas
Muestra estadísticas descriptivas para las variables numéricas, como la media, mediana, desviación estándar, etc.

```python
estadisticas = Analisis.get_stats(df)
for var, stats in estadisticas.items():
    print(f"{var}:")
    for stat, value in stats.items():
        print(f"{stat}: {value}")
```

#### 2.4. Sugerencias de gráficos
Sugiere tipos de gráficos adecuados según el tipo de variables seleccionadas por el usuario.

```python
Plots.suggest_plots(df)
```

#### 2.5. Observaciones generales
Proporciona un resumen general del dataframe, incluyendo el número total de variables, número de variables categóricas y numéricas, y el número de valores nulos.

```python
summary = Analisis.dataframe_summary(df)
for key, value in summary.items():
    print(f"{key}: {value}")
```

#### 2.6. Salir
Finaliza el programa y guarda el análisis realizado en un archivo JSON.

```python
Salir = True
Export.save_analysis_to_json(df)
```


### 3. Exportación y Visualización de Gráficos
El programa permite la visualización de gráficos para las distribuciones categóricas, valores nulos y sugerencias de gráficos basados en la selección del usuario. Los gráficos se guardan en el directorio graficos.


### Créditos
- Jose Santisteban
- Manuel Rodas
- Sebastian Solorzano

