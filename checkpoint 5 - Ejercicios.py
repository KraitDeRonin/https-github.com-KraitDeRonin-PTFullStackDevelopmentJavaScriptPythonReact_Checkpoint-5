# Ejercicios

#1. Bucle for en Python

for i in range(1, 6):
    print(f"Número: {i}")

#2. Función de Suma con 3 Argumentos

def suma(a, b, c):
    return a + b + c
# Ejemplo:
resultado = suma(10, 20, 30)
print(f"El resultado de la suma es: {resultado}")

# 3. Función Lambda equivalente

suma_lambda = lambda a, b, c: a + b + c

print(f"Resultado con Lambda: {suma_lambda(10, 20, 30)}")

### 4. Verificación de valor en una lista

nombre = "Enrique"
lista_nombre = ["Jessica", "Paul", "George", "Henry", "Adán"]
# Modo A: Usando in
if nombre in lista_nombre:
    print(f"{nombre} está en la lista.")
else:
    print(f"{nombre} NO está en la lista.")
# Modo B: Con bucle 'for'
encontrado = False
for n in lista_nombre:
    if n == nombre:
        encontrado = True
        break
if encontrado:
    print(f"Bucle: {nombre} encontrado.")
else:
    print(f"Bucle: {nombre} no coincide.")