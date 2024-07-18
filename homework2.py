kol_dz = 12
kol_hour = 1.5
name_train = 'Курс:Python'
time_1_dz = kol_hour / kol_dz

# Или так
# middle_hour = 'среднее время выполнения'
# kol_dz1 = 'всего задач:'
# kol_hour1 = 'затрачено часов:'

print(name_train, ',' ' ' 'всего задач:', kol_dz,  ',' ' ' 'затрачено часов:', ' ', kol_hour, ',' ' ', 'среднее время выполнения', ' ', time_1_dz, ' ', 'часа', '.', sep='')
# Или так print(name_train, ',', " ", kol_dz1, kol_dz, ",", " ", kol_hour1, ' ', kol_hour, ",", " ", middle_hour, " ", time_1_dz, " ", 'часа.', sep='')