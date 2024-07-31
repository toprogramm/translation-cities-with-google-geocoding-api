import pandas as pd

# Загрузите CSV файл в DataFrame
df = pd.read_csv('citiesTranslationList.csv')

# Извлеките значения из столбца 'Англ. город' и сохраните их в список
city_names = df['Англ. город'].dropna().tolist()

# Выведите массив городов
print("Города:", city_names)

# Выведите количество элементов в массиве
print("Количество элементов:", len(city_names))
