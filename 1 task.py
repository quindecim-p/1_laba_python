number = 1
counter = 0

while counter < 1001:
    divider = 2
    check = True

    while divider <= int(number ** 0.5):
        if number % divider == 0:
            check = False
            break
        divider += 1

    if check:
        counter += 1
        print(str(counter) + ")", number)

    number += 1
