input_lista= input("ingrese una lista de numeros enteros separados por espacios: ")
lista = input_lista.split()
lista= [int(i) for i in lista]

def arrange(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

print("La lista ordenada se veria asi: ",arrange(lista))