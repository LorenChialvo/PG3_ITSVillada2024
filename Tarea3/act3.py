month = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

print("del 1 al 12, que numero de mes desea saber?")
index=int(input())-1
try:
    print("el mes que desea saber es ", month[index])
except IndexError:
    print("el mes que desea saber no existe o excede el numero de meses en el año")