# Libraries
import pandas as pd

def createDummies(df, var_name):
    """
    Función que nos crea variables dummy a partir de una columna con valores categóricos
    df: DataFrame
    var_name: Nombre de la columna

    return: DataFrame
    """
    # Variables dummy
    dummy_var = pd.get_dummies(df[var_name], prefix = var_name)

    # Eliminamos la columna original
    df.drop(var_name, axis = 1, inplace=True)

    # añadimos las columnas dummy
    df = pd.concat([df, dummy_var], axis = 1)

    return df
