"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes


def calcular_promedio(lista):
    """Recibo una lista, la sumo y retorno el promedio"""
    promedio=sum(lista)/len(lista)
    return promedio

def calcular_logro_meta(lista_ventas, meta):
    """calculo el porcentaje de logro de la meta"""
    total_ventas= (sum(lista_ventas))
    return (total_ventas * 100) / meta

def calcular_clasificacion(porcentaje):
    if porcentaje >= 100:
        mensaje = "Felicidades, meta alcanzada"
    elif porcentaje >= 80:
        mensaje = "Llamada de atencion, debe trabajar por la meta"
    else:
        mensaje = "urgente, crisis de ventas. Atencion prioritaria"
        
    return mensaje
def imprimir_reporte(datos_reporte):
    """imprime el reporte finasl de cada sede"""
    print("\nREPORTE FINAL")
    print("-" * 60)
    # Se recorre cada fila del reporte.
    for fila in datos_reporte:
        print(f"Sede: {fila['nombre']}")
        print(f"Provincia: {fila['provincia']}")
        print(f"Tipo: {fila['tipo']}")
        print(f"Total semanal: {fila['total']:,.0f}")
        #se imprime el promedio diario con formato moneda y sin decimales.
        print(f"promedio diario: {fila['total']:,.0f}")
        #se imprime el porcentaje con dos decimales
        print(f"cumplimiento de meta: {fila['porcentaje']:.2f}%")
        print(f"estadp: {fila['estado']}")
        print("-" * 60)
    print("cantidad de sedes:", len(datos_reporte))
        
        


#print("Tipo sedes: ", type(sedes).__name__)
#print("Cantidad de emprendimientos: ", len(sedes))
#primer_emprendimiento = sedes[0]
#print("Tipo de indice [0]: ", type(primer_emprendimiento).__name__)
#print("Emprendimiento", primer_emprendimiento["nombre"])
#print("ventas emprendimiento:", sum(primer_emprendimiento["ventas"]))

reporte = []

for emprendimiento in sedes: 
    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]
    nombre = emprendimiento["nombre"]
    promedio_diario = calcular_promedio(ventas)
    porcentaje_logro = calcular_logro_meta(ventas, meta)
    clasificacion = calcular_clasificacion(porcentaje_logro)
    
    reporte.append(
        {
        "nombre": nombre,
        "provincia": emprendimiento["provincia"],
        "tipo": emprendimiento["tipo"],
        "total": sum(emprendimiento["ventas"]),
        "porcentaje": porcentaje_logro,
        "estado": clasificacion
        }
    )
    
imprimir_reporte(reporte)
    #print(f"---Emprendimiento {nombre}---")
    #print("Promedio diario de ventas: ", promedio_diario)
    #print("Porcentaje logro: ", porcentaje_logro)
    #print("clasificacion: ", clasificacion)



    #promedio_diario = calcular_promedio(primer_emprendimiento["ventas"])
    #porcentaje_logro = calcular_logro_meta(primer_emprendimiento["ventas"], primer_emprendimiento["meta"])


