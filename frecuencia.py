def frecuencia_palabras_en_archivo(archivo_entrada, archivo_salida):
    """Analiza la frecuencia con que ocurren diferentes palabras en un archivo
    de texto."""
    frecuencias = {}
    with open(archivo_entrada, "r", encoding="utf8") as f:
        # Leer cada línea
        for linea in f:
            # Dejar únicamente letras y espacios
            linea = linea.lower()
            letras = ""
            for caracter in linea:
                if caracter.isalpha() or caracter == " ":
                    letras += caracter
            palabras = letras.split()
            for palabra in palabras:
                if palabra in frecuencias:
                    frecuencias[palabra] += 1
                else:
                    frecuencias[palabra] = 1

    # Ordenar el diccionario por frecuencia
    # La colección .items() de un diccionario son las tuplas (clave, valor) que
    # lo conforman
    items = frecuencias.items()
    # Ordenarlo: sorted
    # en orden descendente: reverse=True
    # por frecuencia: la frecuencia es el segundo elemento de la tupla: item[1]
    # el parámetro key indica en base a qué se hace el ordenamiento,
    # lambda crea una función "anónima", es decir, sin nombre.
    # lambda item: item[1]
    # sería el equivalente a definir una función como la siguiente
    # (excepto por el nombre):
    # def nombre(item):
    #     return item[1]
    items = sorted(items, key=lambda item: item[1], reverse=True)
    # Convertir la colección de tuplas ordenadas en diccionario
    frecuencias = dict(items)

    # Escribir el archivo de salida
    with open(archivo_salida, "w", encoding="utf8") as f:
        for palabra in frecuencias:
            linea = f"{palabra}: {frecuencias[palabra]}\n"
            f.write(linea)
    # Regresar el diccionario
    return frecuencias


def main():
    """Probar la función"""
    archivo = "data/Asimov, Isaac - Cómo ocurrió.txt"
    salida = "data/Asimov-análisis.txt"
    prueba = frecuencia_palabras_en_archivo(archivo, salida)
    # Mostrar las diez palabras más frecuentes
    i = 0
    for palabra in prueba:
        print(f"{palabra}: {prueba[palabra]}")
        i += 1
        if i >= 10:
            break


main()