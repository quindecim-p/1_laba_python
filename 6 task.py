C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C_2 = (45, 21, 124, 76, 5, 23, 91, 234)

sum_C_1 = sum(C_1)
sum_C_2 = sum(C_2)

if sum_C_1 > sum_C_2:
    print("Сумма больше в кортеже C_1 -", sum_C_1)
elif sum_C_2 > sum_C_1:
    print("Сумма больше в кортеже C_2 -", sum_C_2)
else:
    print("Суммы в обоих кортежах равны -", sum_C_1)

min_C_1_index = C_1.index(min(C_1)) + 1
max_C_1_index = C_1.index(max(C_1)) + 1
min_C_2_index = C_2.index(min(C_2)) + 1
max_C_2_index = C_2.index(max(C_2)) + 1

print("Минимальный элемент в кортеже C_1 -", min(C_1), "его порядковый номер -", min_C_1_index)
print("Максимальный элемент в кортеже C_1 -", max(C_1), "его порядковый номер -", max_C_1_index)
print("Минимальный элемент в кортеже C_2 -", min(C_2), "его порядковый номер -", min_C_2_index)
print("Максимальный элемент в кортеже C_2 -", max(C_2), "его порядковый номер -", max_C_2_index)
