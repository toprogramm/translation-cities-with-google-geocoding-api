import pandas as pd

# Загрузите CSV файл в DataFrame
df = pd.read_csv('cities_translated.csv')

# Имя столбца, в котором нужно искать дубликаты
column_name = 'Original City English Name'

# Найдите дубликаты в указанном столбце
duplicates = df[df.duplicated(subset=[column_name], keep=False)]

# Группируйте дубликаты по значению столбца и объединяйте строки в одну строку
grouped_duplicates = duplicates.groupby(column_name).agg(lambda x: ', '.join(x)).reset_index()

# Выведите результат
print("Дубликаты по группам:")
print(grouped_duplicates)

