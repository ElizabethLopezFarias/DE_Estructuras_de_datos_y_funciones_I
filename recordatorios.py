# Código que agrega, modifica y ordena una agenda

# Diccionario original
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
                 ['2021-05-01', "15:00", "No trabajar"],
                 ['2021-07-15', "13:00", "No hacer nada es feriado"],
                 ['2021-09-18', "16:00", "Ramadas"],
                 ['2021-12-25', "00:00", "Navidad"]]

# Nuevo evento
nuevo_evento = ['2021-01-02', '06:00', 'Empezar el año']

# Agregar el nuevo evento al diccionario original
recordatorios.append(nuevo_evento)

#Busca la fecha del recordatorio a modificar
for i, recordatorio in enumerate(recordatorios):
    fecha = recordatorio[0]
    if fecha == '2021-07-15':
        # Actualiza la fecha al 16 de julio
        recordatorios[i][0] = '2021-07-16'
        break

# Filtrar los recordatorios excluyendo el del Día del Trabajo
recordatorios = [recordatorio for recordatorio in recordatorios if recordatorio[0] != '2021-05-01']

# Agregar los eventos de Cena de Navidad y Año Nuevo
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Año Nuevo'])


# Ordenar por fecha (primer elemento en cada sublista)
recordatorios_ordenados = sorted(recordatorios, key=lambda x: x[0])

# Luego, ordenar por hora (segundo elemento en cada sublista)
# recordatorios_ordenados = sorted(recordatorios_ordenados, key=lambda x: x[1])

# Verificar los cambios
for recordatorio in recordatorios_ordenados:
    print(f"Fecha: {recordatorio[0]}, Hora: {recordatorio[1]}, Actividad: {recordatorio[2]}")

