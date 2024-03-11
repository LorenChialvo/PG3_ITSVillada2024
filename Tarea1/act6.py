palabra = str(input("ingrese una palabra: "))
def vocals(word):
    vocals.number = 0
    for i in word:
        if i in "aeiouAEIOU":
            vocals.number += 1
    return(vocals.number)

print("la palabra tiene ",vocals(palabra), " vocales")
