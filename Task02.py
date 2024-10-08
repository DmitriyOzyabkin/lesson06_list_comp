'''
Задача 2. Случайные соревнования
Мы хотим протестировать работу электронной таблицы для участников
некоторых соревнований. Есть два списка, то есть две команды, по 20
участников в каждом. В них хранятся очки каждого участника — вещественные
числа с двумя знаками после точки, например 4.03.
Член одной команды соревнуется с участником другой команды под таким же
номером. То есть первый соревнуется с первым, второй — со вторым и так
далее.
Напишите программу, которая генерирует два списка участников (по 20
элементов) из случайных вещественных чисел (от 5 до 10). Для этого найдите
подходящую функцию из модуля random. Затем сгенерируйте третий список, в
котором окажутся только победители из каждой пары'''
import random


def generate_team(participants: int) -> list:
    return [round(random.uniform(5, 10), 2) for _ in range(participants)]

def find_winners(team1: list, team2: list) -> list:
    return [max(team1[i], team2[i]) for i in range(20)]


team_1 = generate_team(20)
team_2 = generate_team(20)

winners = find_winners(team_1, team_2)
print('First team', team_1)
print('Second team', team_2)
print('Winners', winners)
