print("Cuando en un número la diferencia entre cada par de dígitos consecutivos es uno, se lo llama número 'step'")
num = int(input("ingrese un número y le diremos si es step: "))
def stepnumber(num):
    prevDigit = -1
    while (num):
        curDigit = n % 10
        if (prevDigit == -1):
            prevDigit = curDigit
        else:
            if (abs(prevDigit - curDigit) != 1):
                print("no es un step")
        prevDigit = curDigit
        n //= 10
    return print("es un step")
            
stepnumber(num)
