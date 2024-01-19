import timeit
from typing import Callable

from bm import boyer_moore_search
from kmp import kmp_search
from rabina import rabin_karp_search

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()
    
def benchmark(func: Callable, text_: str, pattern_:str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)

# Функція для запуску бенчмарків
def run_benchmarks(text, patterns, algorithms):
    results = []
    for pattern in patterns:
        for algorithm in algorithms:
            time = benchmark(algorithm, text, pattern)
            results.append((algorithm.__name__, pattern, time))
    return results

# Функція для виведення результатів
def print_results(results):
    title = f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Час виконання, сек'}"
    print(title)
    print("-" * len(title))
    for result in results:
        print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")

# Головний блок виконання
if __name__ == '__main__':
    # Читання текстів
    text1 = read_file('st1.txt')
    real_pattern1 = "Зміст такої бібліотеки зазвичай описано у специфікації мови"
    text2 = read_file('st2.txt')
    real_pattern2 = "є дослідження та програмна реалізація методів"
    fake_pattern = "мама мила раму"

    # Визначення алгоритмів
    algorithms = [boyer_moore_search, kmp_search, rabin_karp_search]

    # Тестування для першого тексту
    results1 = run_benchmarks(text1, [real_pattern1, fake_pattern], algorithms)
    print("Результати для першого тексту:")
    print_results(results1)

    # Тестування для другого тексту
    results2 = run_benchmarks(text2, [real_pattern2, fake_pattern], algorithms)
    print("\nРезультати для другого тексту:")
    print_results(results2)

