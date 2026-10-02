# calculadora de IMC

print("=== Calculadora de IMC ===")

# 1 entrada de datos 
nombre = str(input("¿Cómo te llamas? "))
edad = int(input("Ingresa tu edad en años: "))
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros (ej. 1.70): "))

# 2 operación aritmética
imc = peso / (estatura ** 2)

# 3 operación lógica (categoría)
if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

# 4 salida con f-strings
print()
print(f"Hola, {nombre} ({edad} años)")
print(f"Peso: {peso} kg | Estatura: {estatura} m")
print(f"Tu IMC es: {imc:.2f}")
print(f"Categoría: {categoria}")