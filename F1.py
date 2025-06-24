import csv
import random
from typing import List, Optional
from pathlib import Path

# Класс узла бинарного дерева
class TreeNode:
    """Узел бинарного дерева поиска."""
    def __init__(self, value: int):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# Функция вставки значения в бинарное дерево
def insert(root: Optional[TreeNode], value: int) -> TreeNode:
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

# In-order обход дерева (сортировка по возрастанию)
def in_order_traversal(root: Optional[TreeNode], result: List[int]) -> None:
    if root is not None:
        in_order_traversal(root.left, result)
        result.append(root.value)
        in_order_traversal(root.right, result)

#Генерирует случайные числа и сохраняет в CSV
def generate_random_numbers(filename: str, count: int, min_val: int, max_val: int) -> List[int]:
    numbers = [random.randint(min_val, max_val) for _ in range(count)]
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(numbers)
    return numbers

def manual_input(filename: str) -> List[int]:
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

def get_fill_method() -> str:
    print("Выберите способ заполнения файла:")
    print("1 - Вручную")
    print("2 - Случайными числами")
    while True:
        choice = input("Ваш выбор (1/2): ")
        if choice in ['1', '2']:
            return choice
        print("Неверный ввод! Попробуйте снова.")

def fill_csv(filename: str) -> None:
    choice = get_fill_method()
    if choice == '1':
        manual_input(filename)
    else:
        count = int(input("Введите количество чисел в массиве: "))
        min_val = int(input("Введите нижнюю границу диапазона: "))
        max_val = int(input("Введите верхнюю границу диапазона: "))
        generate_random_numbers(filename, count, min_val, max_val)

#Запускает тест производительности через отдельный файл
def run_benchmark():
    try:
        from benchmark import run_benchmark as benchmark
        print("\nЗапуск теста производительности...")
        benchmark()
    except ImportError:
        print("Файл benchmark.py не найден. Создайте его для тестирования.")

def main():
    """Основная функция программы."""
    # Выбор входного файла
    file_input = input("Введите имя входного файла (по умолчанию data.csv): ") or 'data.csv'
    fill_csv(file_input)

    #Проверка существования файла
    try:
        with open(file_input, 'r') as file:
            reader = csv.reader(file)
            data = [int(num) for row in reader for num in row if num.strip()]
    except FileNotFoundError:
        print(f"Файл {file_input} не найден.")
        return

    #Построение бинарного дерева
    root = None
    for num in data:
        root = insert(root, num)
    
    #Сортировка чисел с помощью обхода дерева
    sorted_data = []
    in_order_traversal(root, sorted_data)

    # Выбор выходного файла
    file_output = input("Введите имя выходного файла (по умолчанию data1.csv): ") or 'data1.csv'

    #Запись отсортированных чисел в файл
    with open(file_output, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(sorted_data)
    
    print(f"\nСортировка завершена.")
    print(f"Результат записан в {file_output}")

    # Предложение запустить бенчмарк
    if len(data) > 1000:
        choice = input("\nЗапустить тест производительности? (y/n): ").lower()
        if choice == 'y':
            run_benchmark()

if __name__ == "__main__":
    main()