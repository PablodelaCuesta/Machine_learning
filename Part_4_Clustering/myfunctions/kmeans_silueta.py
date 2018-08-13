def silueta(max_k, X, x1, x2):
    """
    Nos crea una serie de gráficos que nos determina que número de clusters es óptimo
    """
    # Librerías
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    from sklearn.cluster import KMeans
    from sklearn import metrics
    from scipy.spatial.distance import cdist
    from sklearn.metrics import silhouette_samples, silhouette_score


    max_k = max_k## maximo número de clusters que vamos a crear
    K = range(1,max_k+1)
    ssw = []
    color_palette = [plt.cm.Spectral(float(i)/max_k) for i in K]
    centroid = [sum(X)/len(X) for i in K]
    sst = sum(np.min(cdist(X, centroid, "euclidean"), axis = 1))


    for k in K:
        kmeanModel = KMeans(n_clusters=k).fit(X)
        
        centers = pd.DataFrame(kmeanModel.cluster_centers_)
        labels = kmeanModel.labels_
        
        ssw_k = sum(np.min(cdist(X, kmeanModel.cluster_centers_, "euclidean"), axis = 1))
        ssw.append(ssw_k)
        
        label_color = [color_palette[i] for i in labels]
        
        ##Fabricaremos una silueta para cada cluster
        # Por seguridad, no hacemos silueta si k = 1 o k = len(X)
        if 1<k<len(X):
        ##Crear un subplot de una fila y dos columnas
            fig, (axis1,axis2) = plt.subplots(1,2)
            fig.set_size_inches(20,8)
        
            #El primer subplot contendrá la silueta, que puede tener valores desde -1 a 1
            #En nuestro caso, ya controlamos que los valores están entre -0.1 y 1
            axis1.set_xlim([-0.1, 1.0])
            #El número de clusters a insertar determinará el tamaño de cada barra
            #El coeficiente (n_clusters+1)*10 será el espacio en blanco que dejaremos 
            #entre siluetas individuales de cada cluster para separarlas.
            axis1.set_ylim([0, len(X)+ (k+1)*10])
        
            silhouette_avg = silhouette_score(X, labels)
            print("* Para k = ",k, " el promedio de la silueta es de :",silhouette_avg)
            sample_silhouette_values = silhouette_samples(X, labels)
            
            y_lower = 10
            for i in range(k):
                #Agregamos la silueta del cluster i-ésimo
                ith_cluster_sv = sample_silhouette_values[labels == i]
                print("   - Para i = ", i+1, " la silueta del cluster vale : ", np.mean(ith_cluster_sv))
                #Ordenamos descendientemente las siluetas del cluster i-ésimo
                ith_cluster_sv.sort()
            
                #Calculamos donde colocar la primera silueta en el eje vertical
                ith_cluster_size = ith_cluster_sv.shape[0]
                y_upper = y_lower + ith_cluster_size
                
                #Elegimos el color del cluster
                color = color_palette[i]
                
                #Pintamos la silueta del cluster i-ésimo
                axis1.fill_betweenx(np.arange(y_lower, y_upper),
                                0, ith_cluster_sv, facecolor = color, alpha = 0.7)
                
                
                #Etiquetamos dicho cluster con el número en el centro
                axis1.text(-0.05, y_lower + 0.5 * ith_cluster_size, str(i+1))
                
                #Calculamos el nuevo y_lower para el siguiente cluster del gráfico
                y_lower = y_upper + 10 #dejamos vacías 10 posiciones sin muestra
                
            axis1.set_title("Representación de la silueta para k = %s"%str(k))
            axis1.set_xlabel("S(i)")
            axis1.set_ylabel("ID del Cluster")
            
            ##Fin de la representación de la silueta
            
        ##Plot de los k-means con los puntos respectivos
        plt.plot()
        plt.xlim([0,10])
        plt.ylim([0,10])
        plt.title("Clustering para k = %s"%str(k))
        plt.scatter(x1,x2, c=label_color)
        plt.scatter(centers[0], centers[1], c=color_palette, marker = "x")
        plt.show()