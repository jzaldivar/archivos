# Archivos

Las variables proveen únicamente almacenamiento *temporal* de los valores, para almacenar dichos valores de manera persistente es necesario utilizar archivos.

Los archivos:

* Proveen almacenamiento persistente
* Permiten el intercambio de información entre diferentes programas
* Pueden albergar los reportes generados por el programa


## Abrir un archivo

Para abrir un archivo, se utiliza la función `open`:

```python
open(nombre_archivo, modo="r", encoding=None)
```

| `modo` | Descripción |
|:-------:|:------------|
| `"r"`   | Abre el archivo en modo lectura (*read*).<br>Esta es la opción predeterminada.|
| `"w"`   | Abre el archivo en modo escritura (*write*).<br>Si el archivo ya existe, su contenido se sobreescribe.|
| `"a"`   | Abre el archivo en modo de adición (*append*).<br>Si el archivo ya existe, lo que se escribe, se añade al final del contenido previo.|
| `"r+"`  | Abre el archivo para leer y escribir.|

De manera predeterminada, la función `open` **no** especifica la codificación que se utilizará para el archivo (valor del parámetro `encoding`, o página de códigos). Para evitar problemas con los caracteres que utilizamos para escribir en español, lo más práctico es especificar que se utilice la codificación UTF-8 (`encoding="utf8"`, notar que no lleva guión) al abrir archivos de texto. Obviamente, hay que verificar que el programa con el que se creó el archivo de texto utilice esta codificación o, en su caso, utilizar la codificación correcta al invocar la función `open`.

Igualmente, de manera predeterminada, los archivos se abren en **modo texto**, para abrirlos en modo binario, hay que agregar `"b"` al `modo` (`"rb"`, `"wb"`, etc.).


## Lectura de archivos

Para propósitos del ejercicio, vamos a crear un archivo de texto para, posteriormente, leerlo.

Crear el archivo `beatles.txt` y escribe en él los nombres de los integrantes del legendario cuarteto:

```
John Lennon
Paul McCarthy
George Harrison
Ringo Star
```

y graba el archivo.

> ***Observación***: Escribe tú mismo todo el código que se muestra, _no lo copies y lo pegues_. Escribir código es didáctico y una buena oportunidad de aprendizaje, no te prives de ella.

A continuación, crea el archivo `beatles.py` y escribe el siguiente código:

```python
f = open("beatles.txt", "r", encoding="utf8")
for line in f:
    print(line)
# Siempre hay que cerrar el archivo al terminar de trabajar con él
f.close()
```

y ejecútalo.

Ya que estamos en esto, vamos a crear un _commit_ con los cambios que acabamos de hacer. Usa el mensaje "`Primer ejemplo con archivos`" para tu _commit_.

Puedes observar que *los archivos son iterables* y que *cada una de las líneas* del archivo *es un elemento* del iterable.

También puedes observar que las líneas se imprimieron a doble espacio. ¿Por qué? 

Lo que sucede es que cada línea del archivo de texto termina con un carácter nueva línea (`"\n"`) que, al imprimirse, cambia de línea. Queda a doble espacio porque el `print`, de manera predeterminada, también termina las cadenas impresas con un carácter nueva línea.

El siguiente código nos permite visualizarlo utilizando la función `repr` (*representación*). Escríbelo en un nuevo archivo (por ejemplo, `beatles2.py`), ejecútalo y observa la salida.

```python
f = open("beatles.txt", "r", encoding="utf8")
for line in f:
    for caracter in line:
        print(repr(caracter), end=" ")
    print()
f.close()
```

Puedes observar, al final de cada línea, el carácter `"\n"`. 

Es una buena práctica hacer un _commit_ después de cada cambio significativo, así que haremos un nuevo _commit_ usando, por ejemplo, un mensaje como "`Usar repr para ver los \n`".

Dependiendo del sistema operativo, algunos archivos de texto pueden terminar cada línea con la combinación de caracteres `"\r\n"`. También es posible que la última línea no tenga un carácter de fin de línea, dependiendo de cómo se haya creado.

Podemos usar el método `.strip()` de la clase `str` para eliminar ese carácter de salto de línea al final. `.strip()` también elimina la combinación `"\r\n"`. En realidad, `.strip()` elimina el [espacio en blanco](https://docs.python.org/3/library/string.html#string.whitespace) al principio y al final de la cadena, como se indica en la [documentación de Python](https://docs.python.org/3/library/stdtypes.html#str.strip). 

Para comprobarlo, añade el método `.strip()` a tu archivo `beatles.py` para que quede como sigue:

```python
f = open("beatles.txt", "r", encoding="utf8")
for line in f:
    print(line.strip())
f.close()
```

ejecútalo y compara la nueva salida con la salida obtenida anteriormente, y haz un nuevo _commit_ ("`Quitar \n con strip`").


## Mejor práctica

Aunque el código anterior funciona, se considera una mejor práctica utilizar la función `open` dentro de un bloque `with`. De esta manera, el archivo se cierra automáticamente al terminar el bloque `with`.

Crea un nuevo archivo `beatles-with.py`, escribe el siguiente código:

```python
with  open("beatles.txt", "r", encoding="utf8") as f:
    for line in f:
        print(line.strip())
# No se necesita f.close()
```

y ejecútalo.

Y, ya lo sabes, haz un nuevo _commit_ ("`Uso de with`", por ejemplo).

***Nota***: En los ejemplos anteriores, hemos utilizado el identificador `f` (inicial de *file*) para referirnos al archivo que abrimos. Esta es una decisión arbitraria y podemos utilizar cualquier identificador válido (que siga las reglas de Python).


## Abrir varios archivos en un bloque `with`

Para abrir varios archivos en un bloque `with`, se pueden enumerar los archivos:

```python
with open(...) as f1, open(...) as f2, ...:
```

Por ejemplo:
```python
with (
    open("entrada.txt", "r") as f_in,
    open("salida.txt, "w") as f_out
):
    for line in f_in:
        f_out.write(line)
```

O se pueden anidar los bloques `with`:

```python
with open(...) as f1:
    with open(...) as f2:
        ...
```
Por ejemplo:
```python
with open("entrada.txt", "r") as f_in:
    with open("salida.txt, "w") as f_out:
        for line in f_in:
            f_out.write(line)
```


## Métodos del objeto archivo (`TextFile`)

| Método | Descripción |
| -------------- | ----------- |
| `.read(size)`  | Lee `size` bytes.<br>Si se omite `size`, lee todo el archivo. |
| `.readline()`  | Lee una línea del archivo, incluyendo el carácter nueva línea (`"\n"`) al final. |
| `.readlines()` | Lee a una lista todas las líneas del archivo, incluyendo los caracteres nueva línea. |
| `.write(string)`| Escribe el contenido de la variable `string` en el archivo.<br> Hay que añadir el carácter nueva línea (`"\n"`) si se requiere.<br>La variable `string` debe ser de tipo texto.<br>Regresa la cantidad de bytes escritos.|
| `.seek(offset,`<br>&nbsp;&nbsp;&nbsp;&nbsp;`from_what)`| Mueve el puntero del archivo `offset` bytes.<br>En modo texto sólo se usa `from_what=0`, para moverse relativo al inicio del archivo, o la forma `f.seek(0, 2)`, para moverse hasta el final. |
| `.close()` | Cierra el archivo. |

Recordar que los archivos se pueden iterar línea por línea sin necesidad de utilizar los métodos `.read()` y relacionados.


## Verificar la existencia de un archivo

Existen dos bibliotecas (*libraries*) populares para el manejo de archivos: `os.path` y `pathlib`.

Para verificar la existencia de un archivo con el módulo `os.path` [(documentación)](https://docs.python.org/3/library/os.path.html), podemos hacer algo como:

```python
import os.path

file = "beatles.txt"
if os.path.isfile(file):
    print(f"El archivo '{file}' existe.")
else:
    print(f"El archivo '{file}' no existe.")
```

Escribe el código anterior en el archivo `beatles-exists-os.py` y pruébalo. Después, haz un _commit_ de tus cambios.

También podemos usar el módulo más moderno (y orientado a objetos) `pathlib` [(documentación)](https://docs.python.org/3/library/pathlib.html). 

Para probarlo, crea un nuevo archivo `beatles-exists-pathlib.py`, escribe y ejecuta el siguiente código y haz un _commit_ de tus cambios:

```python
from pathlib import Path

files = ["beatles.txt", "data", "data/ejemplo.txt"]
for file in files:
    file = Path(file)
    if file.exists():
        if file.is_dir():
            print(f"{file.name} es una carpeta.")
        elif file.is_file():
            print(f"{file.name} es un archivo.")
    else:
        print(f"{file.name} no existe.")
```

¿Puedes verificar en el explorador de archivos que los resultados reportados por el programa son correctos?


## Ejemplo: Verificar la frecuencia de palabras en un archivo

Escribiremos una función que analice la frecuencia de las diferentes palabras contenidas en un archivo. La función recibirá como parámetros el nombre del archivo a analizar y el nombre del archivo de salida. En el archivo de salida, se escribira, en cada línea, una palabra, seguida de dos puntos y la cantidad de veces que la misma aparece en el archivo de entrada, en orden de mayor frecuencia de aparición. Adicionalmente, la función regresará como valor un diccionario con las palabras (clave) y sus frecuencias (valor), en el mismo orden.

Prueba la función con el archivo `Asimov, Isaac - Cómo ocurrió.txt` de la carpeta `data`. Imprime también las diez palabras más frecuentes y las veces que éstas aparecen en el archivo.

Crea el archivo `frecuencia.py` y escribe el siguiente código (enfatizo de nuevo: **escribe**, no copies y pegues; recuerda: escribir código es una oportunidad de aprendizaje):

```python
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
```

Prueba el programa, revisa su funcionamiento. ¿Entiendes qué hace cada instrucción? Si tienes dudas, puedes utilizar el depurador para ejecutar el programa paso a paso y ver lo que va sucediendo en "cámara lenta". Si aún no te queda clara alguna instrucción, pregunta. No te quedes con la duda.

Al final, haz el respectivo _commit_ de este ejemplo.


## Ejemplo: Encriptar un archivo

El siguiente ejemplo utiliza una técnica muy sencilla de encriptamiento por desplazamiento. A cada carácter se le aplica un desplazamiento `x` y se reemplaza por el carácter que corresponda a dicho desplazamiento. Por ejemplo, si el desplazamiento es `2`, cada letra "A" se reemplazará por "C"; las "B" por "D", etc. El desplazamiento puede ser positivo o negativo.

Escribe el siguiente código en el archivo `encriptar.py`:

```python
from pathlib import Path
from string import ascii_lowercase as LETRAS


def encriptar(cadena, desplazamiento):
    """
    Encriptar una cadena aplicando el desplazamiento indicado. 
    Solo se encriptan las letras, los números y los signos de puntuación se dejan sin afectar.
    """
    salida = ""
    for letra in cadena.lower():
        pos = LETRAS.find(letra)
        if pos > -1:
            pos = (pos + desplazamiento) % len(LETRAS)
            letra = LETRAS[pos]
        salida += letra
    return salida


def encriptar_archivo(entrada, desplazamiento):
    """
    Encripta el archivo de entrada aplicando el desplazamiento indicado.
    El archivo de salida tiene el mismo nombre que el de entrada más
    la cadena: -CRIPTO.
    """
    archivo = Path(entrada)
    salida = str(archivo.with_name(archivo.stem + "-CRIPTO" + archivo.suffix))
    with open(archivo, "r", encoding="utf8") as f_in:
        with open(salida, "w", encoding="utf8") as f_out:
            for linea in f_in:
                f_out.write(encriptar(linea, desplazamiento))
```

Y escribe y ejecuta el siguiente código en el archivo `ejemplo-encriptar.py` para encriptar el archivo `Asimov, Isaac - Cómo ocurrió.txt` de la carpeta `data`. 

```python
from encriptar import *


encriptar_archivo("data/Asimov, Isaac - Cómo ocurrió.txt", 2)
```

Podrás observar el resultado en el archivo `-CRIPTO` que se creará, igualmente, en la carpeta `data`.

Puedes probar usando diferentes desplazamientos en tu programa de ejemplo.

Haz un _commit_ de este nuevo ejemplo.

De nueva cuenta, analiza el código que escribiste, verifica que entiendes cómo funcionan y por qué se utilizaron cada una de las instrucciones. Usa el depurador y, al final, pregunta cualquier duda que tengas.

¿Puedes codificar un programa que decifre (o desencripte) el archivo encriptado que se generó? Piénsalo un momento...

Y, después, intenta "*reencriptar*" el archivo ya encriptado usando el negativo del desplazamiento que usaste para encriptarlo. Observa el archivo resultante. ¿Era lo que habías pensado hacer? Por cierto, ¿se recupera el archivo original sin pérdidas?


## Ejercicio

El archivo `data\calificaciones.txt` contiene los nombres y calificaciones de los alumnos del curso de Algoritmos y Programación con el siguiente formato:

`Peter Parker 100 95 98 92`

Las calificaciones aparecen separadas del apellido y entre sí por un espacio. El número de calificaciones por alumno es variable.

Procesarlo y generar un archivo `data\promedios.txt` con el formato:

`PARKER, Peter: 96.3`

El formato consiste en el apellido del alumno en mayúsculas, separado por una coma de su nombre, dos puntos y, enseguida, el promedio de las calificaciones a un decimal.

Todos los alumnos tienen un solo nombre y un solo apellido.

No olvides hacer el _commit_ de tu solución.

### Entregable

Se entregará por Canvas el informe usual en PDF, únicamente para el programa del ejercicio de las calificaciones (no de los ejemplos), con el contenido usual: enunciado, análisis, etc., y, obviamente, sus correspondientes portada y conclusiones.

#### Reflexiones

A lo largo del texto de esta actividad vienen varias preguntas. A diferencia de cuando usamos un cuaderno de Jupyter, aquí no podemos contestarlas en alguna celda ex profeso, así que se añadirá al reporte en PDF una sección **Reflexiones**, antes de las conclusiones, en la que darás respuesta a dichas preguntas.

#### Pruebas de ejecución

Como prueba de ejecución, se utilizará una captura de pantalla mostrando el contenido del archivo `data\promedios.txt` creado por el programa y el contenido de la carpeta `data` en el explorador de archivos de VS Code.

Igualmente, otra captura de pantalla con la historia de _commits_ en GitHub.