import sys

def contar_palabras_y_caracteres(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as file:
            texto = file.read()

            caracteres_distintos = len(set(texto))

            palabras = texto.split()
            palabras_distintas = len(set(palabras))

            print(f"Cantidad de caracteres distintos: {caracteres_distintos}")
            print(f"Número de palabras distintas: {palabras_distintas}")
    except FileNotFoundError:
        print("Error: El archivo no existe o no se puede abrir.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python word_count.py <ruta_del_archivo>")
    else:
        ruta_archivo = sys.argv[1]
        contar_palabras_y_caracteres(ruta_archivo)
