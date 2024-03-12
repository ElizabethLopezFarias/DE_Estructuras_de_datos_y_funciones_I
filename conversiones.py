import sys

if len(sys.argv) != 5:
    print("Uso: python conversiones.py <Tasa Sol> <Tasa Peso Argentino> <Tasa Dólar Americano> <valor en peso chileno>")
else:
    tasa_sol_peruano, tasa_peso_argentino, tasa_dolar_americano, valor_peso_chileno = map(float, sys.argv[1:])
    sol_convertido = valor_peso_chileno * tasa_sol_peruano
    peso_argentino_convertido = valor_peso_chileno * tasa_peso_argentino
    dolar_americano_convertido = valor_peso_chileno * tasa_dolar_americano

    print(f"Sol peruano: {sol_convertido:.2f}")
    print(f"Peso Argentino: {peso_argentino_convertido:.2f}")
    print(f"Dólar Americano: {dolar_americano_convertido:.2f}")