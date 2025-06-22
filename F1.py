import csv
import random

# Класс узла бинарного дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функция вставки значения в бинарное дерево
def insert(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    return root

# In-order обход дерева (сортировка по возрастанию)
def in_order_traversal(root, result):
    if root is not None:
        in_order_traversal(root.left, result)
        result.append(root.value)
        in_order_traversal(root.right, result)

def generate_random_numbers(filename, count, min_val, max_val):
    numbers = [random.randint(min_val, max_val) for _ in range(count)]
    # Записываем числа в CSV файл
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(numbers)
    return numbers

def manual_input(filename):
    print("Введите числа через пробел:")
    numbers = input().split()
    try:
        numbers = [int(num) for num in numbers]
        # Записываем числа в CSV файл
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(numbers)
        return numbers
    except ValueError:
        print("Ошибка: введите только целые числа!")
        return manual_input(filename)

def write_to_file(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def get_fill_method():
    print("Выберите способ заполнения файла:")
    print("1 - Вручную")
    print("2 - Случайными числами")
    choice = input("Ваш выбор (1/2): ")
    while True:
        if choice not in ['1', '2']:
            print("Неверный ввод! Попробуйте снова.")
            choice = input("Ваш выбор (1/2): ")
        return choice

def fill_csv(filename):
    choice = get_fill_method()
    if choice=='1':
        manual_input(filename)
    if choice=='2':
        count = int(input("Введите количество чисел в массиве: "))
        min_val = int(input("Введите нижнюю границу диапазона: "))
        max_val = int(input("Введите верхнюю границу диапазона: "))
        generate_random_numbers(filename,count, min_val, max_val)


def main():
    # Выбор входного файла
    file_input = input("Введите имя входного файла (по умолчанию data.csv): ") or 'data.csv'
    fill_csv(file_input)

    # Проверка существования файла
    try:
        with open(file_input, 'r') as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                numbers = [int(num) for num in row if num.strip() != '']
                data.extend(numbers)
    except FileNotFoundError:
        print(f"Файл {file_input} не найден. Создаем новый файл.")
       
        
    
    
    # Построение бинарного дерева
    root = None
    for num in data:
        root = insert(root, num)
    
    # Сортировка чисел с помощью обхода дерева
    sorted_data = []
    in_order_traversal(root, sorted_data)
    
    # Выбор выходного файла
    file_output = input("Введите имя выходного файла (по умолчанию data1.csv): ") or 'data1.csv'
    
    # Запись отсортированных чисел в файл
    with open(file_output, 'w', newline='') as file:
        writer = csv.writer(file)
        for sorted_num in sorted_data:
            writer.writerow([sorted_num])
    
    print(f"Сортировка завершена. Результат записан в файл {file_output}")

if __name__ == "__main__":
    main()