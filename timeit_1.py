import timeit
from kmp import kmp_search
from B_M import boyer_moore_search
from R_K import rabin_karp_search

# Функція для зчитування текстового файлу
def read_file(filename):
    with open(filename, 'r', encoding='latin-1') as file:
        return file.read()

# Зчитуємо вміст текстових файлів
article1 = read_file("стаття 1.txt")
article2 = read_file("стаття 2.txt")

# Підрядки для пошуку
existing_substring = "пошук"  # Одне, що дійсно існує в тексті
non_existing_substring = "xyzabc"  # Вигаданий підрядок



# Вимірюємо час для алгоритмів пошуку
boyer_moore_existing_time_article1 = timeit.timeit(lambda: boyer_moore_search(article1, existing_substring), number=1000)
kmp_existing_time_article1 = timeit.timeit(lambda: kmp_search(article1, existing_substring), number=1000)
rabin_karp_existing_time_article1 = timeit.timeit(lambda: rabin_karp_search(article1, existing_substring), number=1000)

boyer_moore_non_existing_time_article1 = timeit.timeit(lambda: boyer_moore_search(article1, non_existing_substring), number=1000)
kmp_non_existing_time_article1 = timeit.timeit(lambda: kmp_search(article1, non_existing_substring), number=1000)
rabin_karp_non_existing_time_article1 = timeit.timeit(lambda: rabin_karp_search(article1, non_existing_substring), number=1000)

boyer_moore_existing_time_article2 = timeit.timeit(lambda: boyer_moore_search(article2, existing_substring), number=1000)
kmp_existing_time_article2 = timeit.timeit(lambda: kmp_search(article2, existing_substring), number=1000)
rabin_karp_existing_time_article2 = timeit.timeit(lambda: rabin_karp_search(article2, existing_substring), number=1000)

boyer_moore_non_existing_time_article2 = timeit.timeit(lambda: boyer_moore_search(article2, non_existing_substring), number=1000)
kmp_non_existing_time_article2 = timeit.timeit(lambda: kmp_search(article2, non_existing_substring), number=1000)
rabin_karp_non_existing_time_article2 = timeit.timeit(lambda: rabin_karp_search(article2, non_existing_substring), number=1000)

# Виводимо результати
print("Для статті 1:")
print("Boyer-Moore (існуючий підрядок):", boyer_moore_existing_time_article1)
print("KMP (існуючий підрядок):", kmp_existing_time_article1)
print("Rabin-Karp (існуючий підрядок):", rabin_karp_existing_time_article1)

print("Boyer-Moore (вигаданий підрядок):", boyer_moore_non_existing_time_article1)
print("KMP (вигаданий підрядок):", kmp_non_existing_time_article1)
print("Rabin-Karp (вигаданий підрядок):", rabin_karp_non_existing_time_article1)

print("\nДля статті 2:")
print("Boyer-Moore (існуючий підрядок):", boyer_moore_existing_time_article2)
print("KMP (існуючий підрядок):", kmp_existing_time_article2)
print("Rabin-Karp (існуючий підрядок):", rabin_karp_existing_time_article2)

print("Boyer-Moore (вигаданий підрядок):", boyer_moore_non_existing_time_article2)
print("KMP (вигаданий підрядок):", kmp_non_existing_time_article2)
print("Rabin-Karp (вигаданий підрядок):", rabin_karp_non_existing_time_article2)