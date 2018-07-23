import numpy as np
import statsmodels.formula.api as sm

def rsquared_ajust(x_before, x_after, y):
    """
    Función que comprueba que el coeficiente R cuadrado ajustado ha mejorado significativamente
    """
    # Variable resultado
    resultado = False
    
    # Comprobamos que este nuevo modelo mejora r^2 ajustado
    regressor_before = sm.OLS(y, x_before).fit()
    regressor_after = sm.OLS(y, x_after).fit()
            
    # r2 ajustado
    r2_before = regressor_before.rsquared_adj
    r2_after = regressor_after.rsquared_adj
    # comparamos
    if r2_before - r2_after <= 0.05:
        
        # La diferencia no es significativa
        resultado = True
        
    return resultado

# Nuestra función
def backward_elimination(x, y, sl, rsquared = False):
    """
    Función que nos selecciona las variables que mejor describen
    nuestro modelo. 
    
    :params
    
    :x Array
    :sl Int
    
    """
    # variables
    maxVar = sl + 1
    num_variables = len(x[0])
    
    # while-loop
    for i in range(0, num_variables):
        # Realizamos la regresión
        regressor_OLS = sm.OLS(y, x).fit()

        # Valor máximo
        maxVar = max(regressor_OLS.pvalues).astype(float) 
        
        # comparamos con nuestro nivel de significancia
        if maxVar > sl:
            # Buscamos el índice de maxVar
            idx = np.where(regressor_OLS.pvalues == maxVar)

            # Eliminamos la variable con pvalor = maxVar
            x_temp = np.delete(x, idx, axis = 1)

            if rsquared:
                # Comprobamos la variación de r2 ajustado
                if rsquared_ajust(x, x_temp, y):
                    # Eliminamos la variable
                    x = x_temp.copy()
            else:
                # Asignamos a x el nuevo conjunto de datos x_temp
                x = x_temp.copy()            
    
    regressor_OLS.summary()
    
    return x