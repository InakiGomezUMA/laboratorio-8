"""
Reservar y liberar puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]

IMPLEMENTA
1. reservar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta disponible, cambia su estado a 1 y devuelve True. En otro caso, False.
2. liberar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta ocupado, cambia su estado a 0 y devuelve True. En otro caso, False.
Rechaza indices negativos y coordenadas fuera del tablero.
Supone que coordenada es una tupla de dos enteros y el tablero es rectangular,
no vacio y contiene solo 0 y 1. Estas funciones SI modifican el tablero.

COMPROBACIONES CON PRINT
Realiza en orden, sobre el mismo tablero:
- Reservar (0, 1): True.
- Reservar otra vez (0, 1): False.
- Liberar (1, 2): True.
- Liberar otra vez (1, 2): False.
- Reservar (5, 0): False.
- Reservar (-1, 0): False.
Muestra el tablero final y agrega una comprobacion propia.

ANALISIS EN COMENTARIOS
Es necesario recorrer todo el tablero para reservar una coordenada conocida?
Justifica la complejidad de reservar, sin contar la impresion del tablero.

COMMIT SUGERIDO
Completa ejercicio 3: reservas y liberaciones
"""

def reservar_puesto(puestos, coordenada):
  fila, columna = coordenada
  if (
      0 <= fila < len(puestos)
      and 0 <= columna < len(puestos[0])
      and puestos[fila][columna] == 0
  ):
    puestos[fila][columna] = 1
    return True
  return False


def liberar_puesto(puestos, coordenada):
  fila, columna = coordenada
  if (
      0 <= fila < len(puestos)
      and 0 <= columna < len(puestos[0])
      and puestos[fila][columna] == 1
  ):
    puestos[fila][columna] = 0
    return True
  return False


if __name__ == "__main__":
  puestos = [[1, 0, 1], [0, 0, 1]]

  print(reservar_puesto(puestos, (0, 1)))  
  print(reservar_puesto(puestos, (0, 1)))  
  print(liberar_puesto(puestos, (1, 2)))  
  print(liberar_puesto(puestos, (1, 2)))  
  print(reservar_puesto(puestos, (5, 0)))  
  print(reservar_puesto(puestos, (-1, 0)))  

  print("Comprobación propia (intentar liberar una posición ya libre (0, 1)):",liberar_puesto(puestos, (0, 1)),)

  print("Tablero final:", puestos)

# ANALISIS
# No es necesario recorrer todo el tablero.
# La complejidad temporal es O(1).
