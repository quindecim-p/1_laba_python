input_list = []

n = int(input("Введите количество элементов в списке: "))

for i in range(n):
    element = int(input("Введите элемент " + str(i + 1) + ": "))
    input_list.append(element)

max_odd = None
for num in input_list:
    if num % 2 != 0:
        if max_odd is None or num > max_odd:
            max_odd = num

min_abs = None
for num in input_list:
    if min_abs is None or abs(num) < abs(min_abs):
        min_abs = num

if max_odd is not None:
    print("Наибольший нечетный элемент:", max_odd)
else:
    print("Нет нечетных элементов.")

if min_abs is not None:
    print("Минимальный по модулю элемент:", min_abs)
else:
    print("Список пустой, нет элементов для поиска минимального по модулю числа.")
