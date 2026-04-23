# Tratamiento de datos
import pandas as pd 
from IPython.display import display

# Visualización de librerías
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# ------------------------------FUNCIONES------------------------------

# -------------Función para mostrar gráficos de bigotes de las columnas numéricas-------------
def boxplots(df):
    """Función que grafica todas las columnas numéricas de un DataFrame.

    Args:
        df: DataFame
    """
    col_num = df.select_dtypes(include='number').columns

    for col in col_num:
        plt.figure(figsize=(6, 1))
        sns.boxplot(x=df[col], color="DarkSlateBlue")
        plt.title(col)
        plt.show()

#------------------------------------------------------------------------------------------

# -------------Función para generar una gráfica de barrras apiladas-------------
def crosstab(df, col1, col2):
    """Función enera una gráfica de barras apiladas a partir de una tabla de contingencia (crosstab)
    entre dos variables categóricas.

    La función normaliza los valores por fila para mostrar proporciones y permite visualizar
    la relación entre ambas variables de forma comparativa.

    Args:
        df: DataFrame 
        col1: Variable categórica en el eje X
        col2: Variable categórica representada en el color 

    """
    pd.crosstab(
    df[col1], 
    df[col2], 
    normalize="index"
    
    ).plot(
        kind="bar",
        stacked=True,
        figsize=(8,5),
        color=["lightblue", "DarkSlateBlue", "darkgray"]
    )

    plt.xticks(rotation=45)
    plt.title(f"{col1} vs {col2}")
    plt.tight_layout()
    plt.show()

#------------------------------------------------------------------------------------------

# -------------Función para generar un gráfico de dispersión-------------
def scatterplot (df, x, y): 
    """Genera un gráfico de dispersión (scatter plot) entre dos variables numéricas.

    El gráfico permite visualizar la relación entre las variables especificadas,
    mostrando posibles correlaciones, patrones o valores atípicos.

    Args:
        df: DataFrame
        x: Nombre de la variable para el eje X
        y: Nombre de la variable para el eje Y
    """
    plt.figure(figsize=(6,4))
    sns.scatterplot(data=df, x=x, y=y, alpha=0.5)
    plt.title(f"{x} vs {y}")
    plt.show()

#------------------------------------------------------------------------------------------

# -------------Función para generar gráficos de bigotes de dos variables-------------
def boxplots_bi (df, x, y):
    """Genera un gráfico de cajas (boxplot) para analizar la distribución de una variable numérica
    en función de una variable categórica.

    Args:
        df: DataFrame
        x: Variable categórica en el eje X
        y: Variable numérica en el eje Y
    """
    plt.figure(figsize=(7,4))
    sns.boxplot(data=df, x=x, y=y, color="DarkSlateBlue")
    plt.title(f"{x} vs {y}")
    plt.xticks(rotation=45)
    plt.show()

#------------------------------------------------------------------------------------------

# -------------Función para generar un heatmap-------------
def grafica_correlacion(df):
    """Función que genera una matriz de correlación de las variables numéricas de un DataFrame.

    Args:
        df: DataFrame
    """
    # Seleccionar solo columnas numéricas
    col_num = df.select_dtypes(include='number')

    # Matriz de correlación
    corr = col_num.corr()

    # Mapa de colores personalizado
    colors = ["white", "lightgrey", "DarkSlateBlue"]  # baja → alta correlación
    cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)

    # Dibujar el heatmap
    plt.figure(figsize=(8, 4)) 
    sns.heatmap(
        corr, 
        annot=True, 
        fmt=".2f", 
        cmap=cmap, 
        center=0, 
    linewidths=0.5, 
    linecolor='black'
    )
    plt.title("Heatmap de correlación")
    plt.show()

#------------------------------------------------------------------------------------------