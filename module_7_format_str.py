team1_num = 5  # кол-во участников команды 1
team2_num = 6  # кол-во участников команды 2
score_1 = 40  # кол-во решенных задач командой 1
score_2 = 42  # кол-во решенных задач командой 2
team1_time = 1552.512  # время решения задач командой 1
team2_time = 2153.31451  # время решения задач командой 2
tasks_total = 82  # кол-во задач
time_avg = 45.2  # среднее время решения задач

challenge_result_1 = 'Победа команды Мастера кода!'
challenge_result_2 = 'Победа команды Волшебники данных!'
# Мастера кода - команда 1
# Волшебники данных - команда 2

# Использование %
team1_num = 5
formatting_strings_1 = 'В команде Мастера кода участников: %d !' % team1_num
print(formatting_strings_1)
formatting_strings_2 = 'Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num)
print(formatting_strings_2)

#Использование format()
formatting_strings_3 = 'Команда Волшебники данных решила задач: {} !'.format(score_2)
print(formatting_strings_3)
formatting_strings_4 = 'Волшебники данных решили задачи за {:.2f} с !'.format(team1_time)
print(formatting_strings_4)

#Использование f-строк
formatting_strings_5 = f'Команды решили {score_1} и {score_2} задач.'
print(formatting_strings_5)
formatting_strings_6 = f'Результат битвы: {challenge_result_1}'
print(formatting_strings_6)
formatting_strings_7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"
print(formatting_strings_7)

#Определение победителя
if (team1_time / score_1)*team1_num < (team2_time / score_2)*team2_num:
    result = challenge_result_1
elif (team1_time / score_1)*team1_num > (team2_time / score_2)*team2_num:
    result = challenge_result_2
else:
    result = 'Ничья'

print(result)

