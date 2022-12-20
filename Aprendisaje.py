import Asignar_puntajes
# librerias necesarias
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# Vamos hacer la imputación por el mas frecuente, ya que tenemos mas de un dato que no es numerico
simple = SimpleImputer(strategy='most_frequent')
moda = simple.fit_transform(data)
data = pd.DataFrame(moda)
data.columns=['sepal-length','sepal-width','petal-length','petal-width','class']
print(data)

# Tomar valores para entrenamiento
# librerias necesarias
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

x = data[['sepal-width']]
y = data['class']
x_train, x_test, y_train, y_test = train_test_split(x, y) 

linear_regression = linear_model.LinearRegression()
# Entrenamos el modelo
linear_regression.fit(x_train, y_train) 
# Obtenemos los datos predecidos
y_train_predicted = linear_regression.predict(x_train) 
y_test_predicted = linear_regression.predict(x_test)   

# calidad obtenida en el conjunto de datos de entrenamiento, debemos tener en cuenta 
train_MSD = mean_squared_error(y_train, y_train_predicted)

# calidad obtenida en el conjunto de datos de prueba
test_MSD = mean_squared_error(y_test, y_test_predicted)

print(train_MSD)
print(test_MSD)

# graficas de datos del entrenamiento y prueba
fig, axs = plt.subplots(1,2, figsize=(15,4)) 
axs[0].scatter(x_train, y_train,  color='orange')
axs[0].plot(x_train, y_train_predicted, color='black')
axs[0].set_title('Training set, MSD:{:.0f}'.format(train_MSD))

axs[1].scatter(x_test, y_test,  color='gray')
axs[1].plot(x_test, y_test_predicted, color='black')
axs[1].set_title('Testing set, MSD:{:.0f}'.format(test_MSD))

plt.show()