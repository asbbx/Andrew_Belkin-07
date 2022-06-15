# Массив размером 2m + 1, где m – натуральное число,
# заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках


from random import randint

numb = randint(2, 4)

our_arr = [randint(0, 100) for _ in range(2 * numb + 1)]


# Блинная сортировка
def pancake(our_arr):
    if len(our_arr) > 1:
        for size in range(len(our_arr), 1, -1):
            maxindex = max(range(size), key=our_arr.__getitem__)
            if maxindex + 1 != size:
                if maxindex != 0:
                    our_arr[:maxindex + 1] = reversed(our_arr[:maxindex + 1])
                our_arr[:size] = reversed(our_arr[:size])
    return our_arr


print(f'Исходный массив: {our_arr}')
print(f'Сортированный массив: {(pancake(our_arr))}')
print(f'Медиана по блинной сортировки {pancake(our_arr)[len(our_arr) // 2]}')
