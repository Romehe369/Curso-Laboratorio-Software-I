# Hacemos la limpieza e imputacion de datos
import pandas as pd
from sklearn.impute import SimpleImputer
#Libreria para .. faltantes de cada muestra se imputan utilizando el valor medio de los n_neighborsvecinos
from sklearn.impute import KNNImputer
#importamos los datos
df = pd.read_csv("encuesta.csv")
#Procedemos a mostrar
print(df)
# Contar todos los vacios por columna
df.isnull().sum()

# Remplazamos los none and null el valor mas frecuente.
simple = SimpleImputer(strategy='most_frequent')
moda = simple.fit_transform(df)
print(moda)