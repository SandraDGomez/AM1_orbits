

def factorial(n):
    if n==1:
        return 1
    else:
         return factorial(n-1)*n

numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")


