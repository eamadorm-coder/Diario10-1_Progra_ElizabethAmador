#SISTEMA DE CONTROL DE AFORO
# Autor: Elizabeth Amador
# Fecha: 2026/07/21

CAPACIDAD_MAXIMA = 700
UMBRAL_PREVENTIVO = 560

grupos_aceptados = []
grupos_rechazados = []
ocupacion_actual = 0

print("CONTROL DE INGRESO - ANFITEATRO DEL CENAC")
print("Capacidad maxima :700 personas")
print("Escriba 'fin' para cerrar el programa. ")

entrada = input("cantidad de personas en el grupo: ").lower().strip()

while entrada != 'fin':
    try:
        cantidad_grupo = int(entrada)
    except ValueError:
        print("Entrada invalida. Por favor, ingrese un numero entero o 'fin'")
else:
    if cantidad_grupo < 0 :
        print("ERROR: Cantidad no valida")
    elif cantidad_grupo + ocupacion_actual <= CAPACIDAD_MAXIMA:
        grupos_aceptados.append(cantidad_grupo)
        ocupacion_actual += cantidad_grupo
        espacios_disponibles = CAPACIDAD_MAXIMA - ocupacion_actual
        print(f"Grupo aceptado. ingresan {cantidad_grupo} personas.")
        print(f"ocupacion_actual: {ocupacion_actual}")
        print(f"Espacios disponibles: {espacios_disponibles}")
    else:
        grupos_rechazados.append(cantidad_grupo)
        espacios_disponibles = CAPACIDAD_MAXIMA - ocupacion_actual
        print(f"Grupo rechazado. No hay espacio para {cantidad_grupo}personas")
        print(f"ocupacion actual: {ocupacion_actual}")
        print(f"Espacios disponibles: {espacios_disponibles}")
    
    
    
    
    entrada = input("cantidad de personas en el grupo: ").lower().strip()   

