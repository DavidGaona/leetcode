from numpy import argsort

# Sort and get indices
rating = [2, 5, 3, 4, 1]
indexes = argsort(rating)
print(indexes)
# Sort and get indexes
indexes = sorted(range(len(rating)), key=lambda x: indexes[x])
print(indexes)
dicto = {2: 4, 3: 3, 5: 1, 4: 1}
print(type(dicto), type(list(dicto.keys())))

total_val = 0
for i, key in enumerate(dicto):
    for key2 in list(dicto.keys())[i:]:
        if key < key2:
            total_val += dicto[key2]

print(total_val)
hola = [1, 2, 3, 4, 5]
hola.reverse()
print(hola)
