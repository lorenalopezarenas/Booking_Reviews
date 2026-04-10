# Tratamiento de datos
import pandas as pd 
from IPython.display import display
import pycountry # Mapea códigos ISO a nombres completos

# ------------------------------FUNCIONES------------------------------

# -------------Función para eliminar columnas-------------
def eliminar_columns(df, cols):
    """Función que elimina columnas específicas de un DataFrame dado.

    Args:
        df: DataFrame
        cols: columnas a eliminar
    """
    
    return df.drop(columns=cols)

#------------------------------------------------------------------------------------------

# -------------Función para convertir códigos ISO alpha-3 a nombres de países-------------
def code_to_name(code):
    """
    Convierte un código de país en formato ISO alpha-3 a su nombre completo.

    Args:
        code (str): Código ISO alpha-3 del país (ej: 'ESP', 'USA').

    Returns:
        str | None: Nombre completo del país si el código es válido,
        o None si no se encuentra o el valor no es válido.
    """
    country = pycountry.countries.get(alpha_3=str(code).upper())
    return country.name if country else None

#------------------------------------------------------------------------------------------

# -------------Función para pasar sacar los datos únicos de columnas-------------
def datos_unicos(df, cols):
    """Función que muestra los datos únicos de las columnas dadas de un DataFram

    Args:
        df: DataFrame
        cols: columnas a analizar
    """
    for col in cols:
        print(f'\n\nLos datos únicos de la varible {col} son:\n\n {df[col].unique()}\n')
        print('\n-----------------------------------------------------------------')

#------------------------------------------------------------------------------------------

# -------------Función para pasar datos a minúscula-------------
def minus (df, cols):
    """Función que transforma los datos de columnas dadas de una DataFrame a minúsculas.

    Args:
        df: DataFrame
        cols: columnas a modificar
    """
    for col in cols:
        df[col] = df[col].str.lower().str.strip()

#------------------------------------------------------------------------------------------

# -------------Función para reemplazar palabras o caracteres de columnas-------------
def reemplazar (df, cols, x, y):
    """Función que sirve para reemplazar palabras o caracteres de columnas dadas de un DataFrame.

    Args:
        df: DataFrame
        cols: columnas en las cuales queremos reemplazar datos
        x: dato a reemplazar
        y: dato por el que reemplazar
    """
    for col in cols:
        df[col] = df[col].str.replace(x,y)

#------------------------------------------------------------------------------------------

# -------------Función para sacar las columnas con nulos y su porcentaje-------------
def nulos(df):
    columnas = df.columns[df.isnull().sum() > 0]
    print(f'Las columnas con nulos son: {list(columnas)}\n')
    
    porcentaje = (df[columnas].isnull().sum() / df.shape[0] * 100).round(3)
    print(f'El porcentaje de nulos de cada columna es:\n{porcentaje}')

#------------------------------------------------------------------------------------------

# -------------Función para rellenar nulos con la moda-------------
def rellenar_nulos_moda(df, cols):
    """Función que sirve para rellenar los nulos de unas columnas dadas por la moda.

    Args:
        df: DataFrame
        cols: columnas en las que rellenar los nulos
    """
    for col in cols:
        df[col] = df[col].fillna(df[col].mode()[0])

#------------------------------------------------------------------------------------------

# -------------Función para rellenar nulos de columnas categóricas-------------
def rellenar_nulos_cat(df, cols, x):
    """Función que sirve para rellenar los nulos de unas columnas dadas por la categoría indicada.

    Args:
        df: DataFrame
        cols: columnas en las que rellenar los nulos
        x: categoría con la que rellenar (ej: "unknown")
    """
    for col in cols:
       df[col] = df[col].fillna(x) 

#------------------------------------------------------------------------------------------

# -------------Función para estandarizar nombres de columnas-------------
def estandar_columns(df):
    """Función que estandariza los nombres de las columnas de un DataFrame dado:
       - Cambio a minúsculas
       - Eliminación de espacios al principio y al final
       - Cambio de espacios intermedios por "_"

    Args:
        df: DataFrame
    """
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

#------------------------------------------------------------------------------------------

# -------------Función para clasificar reseñas de huéspedes en categorías-------------
def clasificar_review(texto):
    """
    Clasifica las reseñas de huéspedes en distintas categorías según palabras clave.

    Args:
        texto (str): Reseña del huésped.

    Returns:
        str: Categoría asignada a la reseña (por ejemplo: 'cleanliness', 'staff', 'location', etc.).
             Devuelve 'other' si no se encuentra ninguna coincidencia.
    """
   
    if any(word in texto for word in ['clean', 'dirty']):
        return 'cleanliness'
    elif any(word in texto for word in ['staff', 'service', 'check in', 'check out']):
        return 'staff'
    elif any(word in texto for word in ['location', 'area', 'distance']):
        return 'location'
    elif any(word in texto for word in ['room', 'bed', 'bathroom', 'shower']):
        return 'room'
    elif any(word in texto for word in ['ac', 'air_condition']):
        return 'air_conditioning'
    elif any(word in texto for word in ['amenities', 'mattress', 'pillow']):
        return 'amenities'
    elif any(word in texto for word in ['breakfast', 'food', 'restaurant']):
        return 'food'
    elif any(word in texto for word in ['price', 'value', 'expensive', 'refund']):
        return 'value'
    elif any(word in texto for word in ['wifi', 'tv', 'pool', 'gym', 'parking']):
        return 'facilities'
    elif any(word in texto for word in ['noise', 'noisy', 'quiet']):
        return 'noise'
    elif any(word in texto for word in ['construction', 'renovation']):
        return 'construction'
    elif any(word in texto for word in ['nothing', 'anything', 'negtive', 'positive']):
        return 'no_comment'
    else:
        return 'other'

#------------------------------------------------------------------------------------------

# -------------Función para procesar tags de reservas y generar columnas-------------
def procesar_tags(lista):
    """
    Procesa una lista de etiquetas de la descripción de la reserva de un huésped 
    y las clasifica en columnas específicas: tipo de viaje, tipo de grupo, tipo de habitación,
    número de noches y dispositivo.

    Args:
        lista (list of str): Lista de etiquetas asociadas a la reserva.

    Returns:
        pd.Series: Serie con las columnas generadas:
            - 'trip_type': tipo de viaje ('leisure trip' o 'business trip')
            - 'group_type': tipo de grupo (ej. 'couple', 'family with', 'traveler', etc.)
            - 'room_type': tipo de habitación
            - 'nights': número de noches
            - 'device': dispositivo usado para la reserva
    """

    result = { 'trip_type': None, 
              'group_type': None, 
              'room_type': None, 
              'nights': None, 
              'device': None } 
    
    for item in lista: 
        if ('leisure trip' in item) or ('business trip' in item):
            result['trip_type'] = item
        elif 'night' in item:
            result['nights'] = item
        elif 'submitted' in item:
            result['device'] = item
        elif ('couple' in item) or ('family with' in item) or ('traveler' in item) or ('group' in item) or ('with friends' in item):
            result['group_type'] = item
        else:
            result['room_type'] = item
    return pd.Series(result)

#------------------------------------------------------------------------------------------

# -------------Función para un análisis rápido-------------
def analisis_rapido (df, n=3):
    """Función que genera un análisis rápido del DataFrame.

    Args:
        df: Dataframe
        n: número de filas (por defecto = 3)
    """
    print(f'\n\nLas {n} primeras filas del Dataframe son:\n')
    display(df.head(n))
    print('\n-----------------------------------------------------------')

    print(f'\nLa información básica del Dataframe es la siguiente:\n')
    df.info()
    print('\n-----------------------------------------------------------')

    print(f'\nEl número de nulos por columna del Dataframe es:\n')
    display(df.isnull().sum())

#------------------------------------------------------------------------------------------