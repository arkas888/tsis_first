def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

# Пример использования генератора с помощью цикла "for"
n = int(input("Введите значение n: "))

# Вывод результатов
print(f"Все числа от {n} до 0:")
for number in countdown_generator(n):
    print(number)
    
'''Генератор countdown_generator создан с использованием ключевого слова yield. Он возвращает числа от n до 0.
Пользователь вводит значение n с консоли.
Цикл while используется для итерации по числам, начиная с n и уменьшая его до 0. Каждое число возвращается генератором с помощью yield.
Цикл for используется для итерации по значениям, сгенерированным генератором countdown_generator, и вывода каждого значения на экран.'''