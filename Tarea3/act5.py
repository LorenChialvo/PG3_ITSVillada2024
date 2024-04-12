try:
    print("Por favor, escriba el nombre del archivo a crear, evite los caracteres especiales como arrobas, acentos, tildes o signos de exclamación: ")
    name = input()
    name += ".txt"
    with open(name, "w") as archive:
        print("A continaución, usted podrá escribir sus datos y seran guardados automaticamnete en un archivo de texto. PAra frenar esta entrada de datos, escriba el caracter @")
        while True:
            data = input()
            if data == "@":
                break
            archive.write(data + "\n")
except FileNotFoundError:
    print("No se encontro el archivo")
except FileExistsError:
    print("El archivo ya existe")
except IOError:
    print("Error de entrada/salida")
except Exception:
    print("Error inesperado")
except KeyboardInterrupt:
    print("Programa interrumpido")
finally:
    print("Programa terminado")
