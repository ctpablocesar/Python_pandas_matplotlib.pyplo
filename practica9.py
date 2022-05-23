# De adult_data crear un analisis que permita conocer que genero gana mas
# Cambiar el genero a F o M
# Cambiar el income
#   si es menor a 50 poner 49
#   si es mayor poner 51
# Crear un cruce de tabs o columnas

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('adult_data.csv')

d = {'Male': 'M', 'Female': 'F'}

df['gender'] = df['gender'].apply(lambda x: d[x])

# print(df['gender'].head())

d = {'<50K': '49', '>50K': '51', '<=50K': '49'}

df['income'] = df['income'].apply(lambda x: d[x])

# print(df['income'].head())

ct = pd.crosstab(df['gender'], df['income']).plot(kind='bar')
plt.xlabel('Genero')
plt.ylabel('Ingreso')
for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')

plt.show()
