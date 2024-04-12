def cargasum():
    try:
        while True:
            number1 = input(int("Ingrese el primer numero"))
            number2 = input(int"Ingrese el siguiente numero")
            result = number1 + number2
            print("Su suma es ", result)
    except ValueError:
        print("Error! Deben ser numeros enteros")
    finally:
        seguir = input("¿Quieres seguir sumando valores? (s/n): ")
        if seguir.lower() != 's':
            exit
        elif seguir.lower() == "s":
            pass

cargasum()