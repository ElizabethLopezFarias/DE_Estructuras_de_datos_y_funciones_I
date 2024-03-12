# este programa es útil para analizar archivos de texto y obtener estadísticas sobre caracteres y palabras distintas. Puedes ejecutarlo desde la línea de comandos de la siguiente manera:
# python word_count.py <ruta_del_archivo>

import sys
# Esta función toma un argumento ruta_archivo, que debe ser la ruta al archivo de texto
def contar_palabras_y_caracteres(ruta_archivo):
    try:
        # abre el archivo de texto, lo lee y lo guarda en la variable texto
        with open(ruta_archivo, "r") as file:
            texto = file.read()
            # cuenta la cantidad de caracteres tiene el archivo de texto
            caracteres_distintos = len(set(texto))
            # elimina los espacios para contar las palabras
            palabras = texto.split()
            palabras_distintas = len(set(palabras))
            # imprime resultados
            print(f"Cantidad de caracteres distintos: {caracteres_distintos}")
            print(f"Número de palabras distintas: {palabras_distintas}")
    except FileNotFoundError:
        print("Error: El archivo no existe o no se puede abrir.")

if __name__ == "__main__":
    # verifica si los argumentos ingresados son válidos, si no es válido imprime un mensaje y si es válido lee el argumento y ejecuta la función
    if len(sys.argv) != 2:
        print("Ingrese parametro de ejecución válido: python word_count.py <ruta_del_archivo>")
    else:
        ruta_archivo = sys.argv[1]
        contar_palabras_y_caracteres(ruta_archivo)
