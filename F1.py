import csv

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

def main():
    filename = 'data.csv'
    
    # Чтение данных из CSV-файла
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            # Преобразуем все элементы строки в числа
            numbers = [int(num) for num in row if num.strip() != '']
            data.extend(numbers)
    
    if not data:
        print("Файл пуст или не содержит чисел")
        return
    
    # Построение бинарного дерева
    root = None
    for num in data:
        root = insert(root, num)
    
    # Сортировка чисел с помощью обхода дерева
    sorted_data = []
    in_order_traversal(root, sorted_data)
    
    # Запись исходных и отсортированных чисел обратно в файл
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        # Записываем пары исходное, отсортированное
        for original, sorted_num in zip(data, sorted_data):
            writer.writerow([original, sorted_num])
    
    print(f"Сортировка завершена. Результат записан в файл {filename}")

if __name__ == "__main__":
    main()