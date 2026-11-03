"""
Mapa de puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]
0: disponible. 1: ocupado. Las coordenadas son tuplas (fila, columna), desde cero.

IMPLEMENTA
1. crear_mapa(puestos): devuelve un diccionario {(fila, columna): estado}.
   Utiliza una comprension de diccionarios.
2. obtener_disponibles(puestos): devuelve un set de coordenadas disponibles.
   Utiliza una comprension de conjuntos.
No modifiques el tablero.

COMPROBACIONES CON PRINT
- Muestra el mapa completo y los disponibles.
- Consulta el estado de (1, 2) en el mapa: debe ser 1.
- Disponibles esperados: {(0, 1), (1, 0), (1, 1)}. El orden no importa.
- Agrega y comprueba otro tablero propio.

ANALISIS EN COMENTARIOS
- Cuantas celdas se revisan al obtener los disponibles en el ejemplo?
- Cuantas se revisan para f filas y c columnas? Y para n filas y n columnas?

COMMIT SUGERIDO
Completa ejercicio 1: mapa y puestos disponibles
"""

def crear_mapa(puestos):
    # TODO: implementa esta funcion.
    return {(i, j): puestos[i][j] for i in range(len(puestos)) for j in range(len(puestos[0]))}


def obtener_disponibles(puestos):
    # TODO: implementa esta funcion.
    return {(i, j) for i in range(len(puestos)) for j in range(len(puestos[0])) if puestos[i][j] == 0}


if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    # TODO: escribe las llamadas y muestra los resultados con print.
    mapa = crear_mapa(puestos)
    disponibles = obtener_disponibles(puestos)
    print("Mapa completo:")
    for fila in puestos:
        print(fila)
    print("Coordenadas disponibles:", disponibles)
    print("Estado de (1, 2):", mapa.get((1, 2), "No existe"))

    # TODO: agrega al menos un caso propio.

# ANALISIS
# TODO: responde aqui las preguntas del enunciado.

#   Se revisan las 2 filas y 3 columnas. 
#   ya que el ciclo interno recorre cada posición para evaluar si el valor es 0.

#   Para f filas y c columnas se revisan un total de (f * c) celdas. 
#   Para una matriz cuadrada de n filas y n columnas, se revisan n^2 celdas.