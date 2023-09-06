text = 'Enjoy every moment'
el_count = {}

for el in text:
    if el.isalpha():
        el = el.lower()
        if el in el_count:
            el_count[el] += 1
        else:
            el_count[el] = 1

print(el_count)
