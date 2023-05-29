nombre_completo = input("Ingrese su nombre completo: ")
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso / (altura ** 2)
print("\n")
if imc <= 15:
    print("Delgadez muy severa")
elif imc < 16:
    print("Delgadez severa")
elif imc < 18.5:
    print("Delgadez")
elif imc < 25:
    print("Peso saludable")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidad moderada")
elif imc < 40:
    print("Obesidad severa")
else:
    print("Obesidad muy severa (obesidad mórbida)")