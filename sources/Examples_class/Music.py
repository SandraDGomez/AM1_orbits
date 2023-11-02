
file_path = "C:\GITHUB\AM1_orbits\sources\Examples_class\Wonderwall.txt"
# Abre el archivo "Wonderwall.txt" en modo lectura
with open(file_path, 'r') as file:
    # Lee el contenido del archivo
    file_contents = file.read()
    # Haz algo con el contenido, como imprimirlo
    print(file_contents)

# Abre el archivo de entrada
with open(file_path, 'r') as archivo_entrada:
    lineas = archivo_entrada.readlines()

# Separa las líneas en pares e impares
lineas_pares = []
lineas_impares = []
for i, linea in enumerate(lineas):
    if i % 2 == 0:
        lineas_pares.append(linea)
    else:
        lineas_impares.append(linea)


# Guarda las líneas pares en un archivo
with open('pares.txt', 'w') as archivo_pares:
    archivo_pares.writelines(lineas_pares)
print(lineas_pares)
# print(f"Archivo guardado en: 'C:\GITHUB\AM1_orbits\sources\Examples_class\pares.txt'")


# Guarda las líneas impares en otro archivo
with open('impares.txt', 'w') as archivo_impares:
    archivo_impares.writelines(lineas_impares)
#print(lineas_impares)
#print(f"Archivo guardado en: 'C:\GITHUB\AM1_orbits\sources\Examples_class\impares.txt'")
