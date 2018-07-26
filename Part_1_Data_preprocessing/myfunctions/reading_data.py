import pandas as pd
import requests

def open_file(filename, sep, skiprows=None):    
    """
    Cuando la carga de datos es muy grande, pandas puede que no nos sirva ya que intenta cargar toda la información de golpe, por lo que podemos tener problemas de falta de memoria.

    open_file, va a leer la información línea a línea facilitando el procesado
    """
    data = open(filename, 'r')
    
    if skiprows is None:
        #Usamos la función splitting
        splitting(data)
    
    else:
        #saltamos el número de filas especificado
        for idx in range(skiprows):
            data.readline()
        #Usamos la función splitting
        splitting(data)        


def splitting(data):
    # columnas en raw
    cols = data.readline().strip().split(sep)
        
    # desechamos los valores vacíos
    cols = list(filter(None, cols))
        
    # número de columnas
    n_cols = len(cols)

    # contador
    counter = 0

    # diccionario que nos dará el dataset
    main_dict = {}

    # Realizamos un bucle sobre las columnas
    for col in cols:
        main_dict[col] = []

    # Ahora leemos los datos
    for line in data:
        values = line.strip().split(sep)
            
        # filtramos los valores vacíos
        values = list(filter(None, values))
            
        for i in range(len(cols)):
            main_dict[cols[i]].append(values[i])
        counter += 1
    
    # obtenemos el dataframe
    df = pd.DataFrame(main_dict)

    # imprimimos información
    print("El data set tiene %d filas y %d columnas"%(counter, n_cols))


def SampleRows(df, nrows, replace=False):
    """
    function that takes random samples from a DataFrame.
    
    Args:
        df(DataFrame): DataFrame
        nrows (int): number of rows
        replace (boolean): if we want repeat values or not.
        
    Returns:
        Returns a dataframe with the numbers of rows indicate.
    """
    # select random indices
    indices = np.random.choice(df.index, size=nrows, replace=replace)
    
    # sample
    sample = df.loc[indices]
    
    return sample

def open_url(url):
    """
    xxx
    """
    
    response = requests.get(url)
    data = {}
    
    if response.status_code == 200:
        
        #contenido de la respuesta
        content = response.text
        
        # Realizamos un split por salto de línea obteniendo una lista con todas las filas
        all_rows = content.split("\n")
        
        # Cabeceras
        header = all_rows[0].split(",")
        
        # introducción de las cabeceras en el diccionario
        for head in header:
            data[head] = []
        
        #Eliminamos la primera fila
        all_rows.pop(0)
        
        # for-loop sobre cada fila
        for row in all_rows:
            
            # separamos en columnas
            values = row.split(",")
            
            #loop sobre el diccionario
            for idx, key in enumerate(data.keys()):
                data[key].append(values[idx])
        
        #Una vez tenemos nuestro diccionario completo pasamos a un dataframe
        df = pd.DataFrame(data)
        
        return df