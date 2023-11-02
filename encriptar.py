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
