# Programa que permite ingresar tasas de conversión mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano. 
# python conversiones.py 0.0046 0.093 0.0013 10000

#Importacion de bibliotecas
import sys
#Consulta si los argumentos tienen la cantidad de datos necesarios

if len(sys.argv) != 5:
    print("Ingrese de forma correcta la sentencia, por ejemplo: python conversiones.py <Tasa Sol> <Tasa Peso Argentino> <Tasa Dólar Americano> <valor en peso chileno>")
else:
    #asigna los argumentos ingresados
    tasa_sol_peruano, tasa_peso_argentino, tasa_dolar_americano, valor_peso_chileno = map(float, sys.argv[1:])
   
    #realiza cálculos para la reconversión
    sol_convertido = valor_peso_chileno * tasa_sol_peruano
    peso_argentino_convertido = valor_peso_chileno * tasa_peso_argentino
    dolar_americano_convertido = valor_peso_chileno * tasa_dolar_americano

    #imprime los resultados obtenidos en la conversión
    print(f"Sol peruano: {sol_convertido:.2f}")
    print(f"Peso Argentino: {peso_argentino_convertido:.2f}")
    print(f"Dólar Americano: {dolar_americano_convertido:.2f}")
