import time
import random
from F1 import TreeNode, insert, in_order_traversal
from typing import List

def benchmark_tree_sort(data: List[int]) -> float:
    """Замер времени сортировки бинарным деревом."""
    root = None
    start_time = time.perf_counter()
    
    # Вставка всех элементов
    for num in data:
        root = insert(root, num)
    
    # Обход дерева
    sorted_data = []
    in_order_traversal(root, sorted_data)
    
    return time.perf_counter() - start_time

def benchmark_python_sort(data: List[int]) -> float:
    """Замер времени встроенной сортировки Python."""
    start_time = time.perf_counter()
    sorted_data = sorted(data)
    return time.perf_counter() - start_time

def generate_test_data(size: int = 10000) -> List[int]:
    """Генерирует тестовые данные."""
    return [random.randint(-100000, 100000) for _ in range(size)]

def run_benchmark():
    """Запускает сравнительный тест производительности."""
    sizes = [100, 1000, 5000, 10000, 20000]
    print("Сравнение скорости сортировки:\n")
    print(f"{'Размер':<10} | {'Дерево (сек)':<12} | {'Python (сек)':<12} | Разница (сек)")
    print("-" * 55)
    
    for size in sizes:
        data = generate_test_data(size)
        
        tree_time = benchmark_tree_sort(data)
        python_time = benchmark_python_sort(data)
        
        diff = tree_time - python_time
        print(f"{size:<10} | {tree_time:<12.6f} | {python_time:<12.6f} | {diff:.6f}")

if __name__ == "__main__":
    run_benchmark()