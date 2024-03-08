def biciesto(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return print("Es un año biciesto")
            else:
                return print("No es un año biciesto")
            end
        else:
            return print("Es un año biciesto")
        end
    else:
        return print("No es un año biciesto")
    end

año=int(input("ingrese el año: "))
biciesto(año)