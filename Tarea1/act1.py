def search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
input_lista= input("ingrese una lista de numeros separados por espacios: ")
lista = input_lista.split()
lista= [int(i) for i in lista]
bleh =int(input("ingrese el numero a buscar: "))
print("El numero esta en el indice: ",search(lista, bleh))
