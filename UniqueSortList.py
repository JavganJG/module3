lista2 = [82,23,14,144,82,3,56,71,144,66,71,3,14,16,8,12,34,21,567,23,45,12,78,65,43]
lista = []
print("Complete list: "+str(lista2)) 
print("==========================")

"""UNIQUE NUMBERS IN THIS LIST"""
for num in lista2:
    if num not in lista:
        lista.append(num)
"""DELETE OLD LIST"""
del lista2

print("Unique list: "+str(lista)) 
print("==========================")
for index in range(len(lista)//2):
    lista[index],lista[len(lista)-index-1] = lista[len(lista)-index-1],lista[index]

print("Inversion list: "+str(lista)) 
print("==========================")

for index in range(len(lista)):
    for num in range(len(lista)-index-1):
        if lista[num] > lista[num+1]:
            lista[num], lista[num+1] = lista[num+1], lista[num]

print("Sort list: "+str(lista)) 
print("==========================")

