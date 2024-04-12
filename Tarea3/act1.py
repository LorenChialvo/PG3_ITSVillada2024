def cargasum():
    total_sum = 0
    print("Para frenar el programa, ingrese un caracter que no sea un numerico")
    try:
        while True:
            number = int(input("Ingrese un numero: "))
            total_sum += number
            print("Su suma acumulada es ", total_sum)
    except ValueError:
        print("Error! Debe ingresar un numero entero")
    finally:
        seguir = input("¿Quieres seguir sumando valores? (s/n): ")
        if seguir.lower() != 's':
            exit()
        elif seguir.lower() == "s":
            pass

cargasum()