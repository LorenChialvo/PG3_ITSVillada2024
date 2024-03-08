def paint(leng, height, letter):
    for i in range(height):
        print(letter * leng)

def paint_tri (height, letter):
    try:
        lines = float(height)
    except ValueError:
        lines = height
        lines = int(lines)
    for letter in letter:
        for line in range(1, lines + 1):
            print(str(letter) * line)
        print("")




obj = input ("que desea dibujar?\n1) Un cuadrado\n2)Un trinagulo\n>>>")
if obj == 1:
    letra = input("ingrese una letra: ")
    largo = int(input("ingrese el largo: "))
    alto = int(input("ingrese el alto: "))
    paint(largo, alto, letra)
else:
    if (obj == 2):
        letra = input("ingrese una letra: ")
        alto = int(input("ingrese el alto: "))
        paint_tri(alto, letra)
    else:
        print("Por favor introduzca un numero dentro de ese rango")
