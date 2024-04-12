def cargadiv():
    total_div = int()
    try:
            number = int(input("Ingrese un numero: "))
            divisior = int(input("Ingrese el divisor: "))
            total_div = number/divisior
            print("Su division es  igual a", total_div)
    except ZeroDivisionError:
        print("Error! Debe ingresar un numero mayor a 0 para dividirlo")
        #ES LO MISMO, PERO MÁS LARGO ! ! ! ! ! ! WOW
    except ValueError:
        print("Error! Debe ingresar un numero entero")

cargadiv()