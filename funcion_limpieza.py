import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

# Cargar el archivo CSV
df = pd.read_csv('Archivos/test.csv')

def limpiar_datos(df):
    # Eliminar columnas no necesarias
    df.drop(['Name', 'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck'], axis=1, inplace=True)
    
    # Rellenar valores faltantes con la mediana para la columna 'Age'
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Age'] = df['Age'].astype(int)
    
    # Rellenar valores faltantes con la moda para las columnas categóricas
    for column in ['HomePlanet', 'CryoSleep', 'VIP', 'Destination']:
        mode_value = df[column].mode()[0]
        df[column] = df[column].fillna(mode_value)
    
    # Separar la columna 'Cabin' en 'Deck', 'Num' y 'Side'
    df[['Deck', 'Num', 'Side']] = df['Cabin'].str.split('/', expand=True)
    
    # Eliminar la columna original 'Cabin'
    df.drop(columns=['Cabin'], inplace=True)
    
    # Llenar valores faltantes en las nuevas columnas con la moda
    for column in ['Deck', 'Num', 'Side']:
        mode_value = df[column].mode()[0]
        df[column] = df[column].fillna(mode_value)


    df[['VIP','CryoSleep']] = df[['VIP','CryoSleep']].astype(int)
    
    # Crear un codificador de etiquetas
    LE = LabelEncoder()
# Codificar la columna 'HomePlanet' donde 'Mars': 2, 'Earth': 1, 'Europa': 0
    df['HomePlanet'] = LE.fit_transform(df['HomePlanet'])
# Codificar la columna 'Destination' donde 'TRAPPIST-1e': 2, 'PSO J318.5-22': 1, '55 Cancri e': 0
    df['Destination'] = LE.fit_transform(df['Destination'])
# Codificar la columna 'Deck' donde 'B':0 'F':1 'A':2 'G':3 'E':4 'D':5 'C':6 'T':7
    df['Deck'] = LE.fit_transform(df['Deck'])
# Codificar la columna 'Side' donde 'P':0 'S':1
    df['Side'] = LE.fit_transform(df['Side'])

    
    return df  # Retornar el DataFrame limpio

# Limpiar los datos
datos_limpios = limpiar_datos(df)

# Guardar el DataFrame limpio en un nuevo archivo 
output_path = './Archivos/datos_test.csv'
datos_limpios.to_csv(output_path, index=False)

# Imprimir la ruta completa del archivo guardado
ruta_completa = os.path.abspath(output_path)
print("Datos limpios guardados en:", ruta_completa)


    

