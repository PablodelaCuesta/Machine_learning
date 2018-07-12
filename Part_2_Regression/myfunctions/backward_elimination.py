# necesitamos la biblioteca statsmodels
import statsmodels.formula.api as sm

# Nuestra función
def backward_elimination(x, y, sl):
    """
    Función que nos selecciona las variables que mejor describen
    nuestro modelo. 
    
    :params
    
    :x Array
    :sl Int
    
    """
    # número de variables
    numVars = len(x[0])
    
    # for-loop
    for idx in range(0, numVars):
        
        # Realizamos la regresión
        regressor_OLS =sm.OLS(y, x).fit()
        
        # Valor máximo
        maxVar = max(regressor_OLS.pvalues).astype(float)
        
        # comparamos con nuestro nivel de significancia
        if maxVar > sl:
            
            for j in range(0, numVars - idx):
                
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    
    regressor_OLS.summary()
    
    return x