palabra = str(input("ingrese una palabra: "))
print("ahora veremos si es un palindromo")
def palindrome(word):
    if word == word[::-1]:
        return print("es un palindromo")
    else:
        return print("no es un palindromo")
    end
palindrome(palabra)
