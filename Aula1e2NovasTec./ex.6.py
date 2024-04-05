def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return None 
    elif delta == 0:
        x = -b / (2*a) 
        return x
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return x1, x2

a = float(input("Insira o coeficiente a: "))
b = float(input("Insira o coeficiente b: "))
c = float(input("Insira o coeficiente c: "))

raizes = calcular_raizes(a, b, c)

if raizes is None:
    print("A equação não possui raízes reais.")
else:
    print(f"Raízes reais: x1 = {raizes[0]}, x2 = {raizes[1]}")
