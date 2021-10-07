lista = [82,23,144,3,56,71]

print(lista)
for index in range(len(lista)):
    for num in range(len(lista)-index-1):
        if lista[num] < lista[num+1]:
            lista[num], lista[num+1] = lista[num+1], lista[num]
print("Sort list: "+str(lista))  

for index in range(len(lista)):
    for num in range(len(lista)-index-1):
        if lista[num] > lista[num+1]:
            lista[num], lista[num+1] = lista[num+1], lista[num]
print("==========================")
print("Inversion list: "+str(lista))     




