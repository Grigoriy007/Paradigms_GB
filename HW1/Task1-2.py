# Парадигмы программирования и языки парадигм (семинары)
# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
# Императивный код здесь
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
numbers = [9, 3, 17, -7, 6, 12, 1]
sort_list_imperative(numbers)
print(numbers)

# Задача-2: Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(number):
 # Декларативный код здесь
    return sorted(number, reverse = True)

print(sort_list_declarative(numbers))