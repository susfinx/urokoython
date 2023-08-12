# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import math
import csv
import random
import json

def run_with_csv(func):
    def wrapper_from_csv(csv_filename):
        with open(csv_filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    a, b, c = map(int, row)
                    func(a, b, c)
    return wrapper_from_csv

def save_to_json(func):
    def wrapper_to_json(a, b, c):
        result = func(a, b, c)
        data = {
            "parameters": (a, b, c),
            "result": result
        }
        with open('results.json', 'a') as file:
            json.dump(data, file)
            file.write('\n')
    return wrapper_to_json

@run_with_csv
@save_to_json
def quadratic_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return None

def generate_csv(filename, rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [random.randint(100, 1000) for _ in range(3)]
            writer.writerow(row)


if __name__=='__main__':
    generate_csv('random_numbers.csv', 100)
    quadratic_roots('random_numbers.csv')

