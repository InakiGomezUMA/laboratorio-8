"""EJERCICIO 10 — Lógica del reporte

Implementa generar_reporte(productos). Cada producto tiene nombre único,
precio y stock enteros no negativos, y categoria.
Devuelve un diccionario con:
- disponibles: lista de nombres con stock > 0, en el orden original.
  Usa filter y map con lambda.
- valor_total: suma de precio * stock de todos los productos.
  Usa map y reduce con lambda, con valor inicial 0.
- hay_agotados: booleano que indica si algún stock es 0.
  Usa any sobre map con lambda.
- categorias: set con todas las categorías. Usa comprensión de sets.
- precios_con_recargo: lista de tuplas (nombre, precio con recargo del 10 %),
  solo para productos con stock > 0, en el orden original.
  Define una lambda para el recargo, redondeado a dos decimales con round,
  e invócala dentro de una comprensión de listas.
No modifiques productos ni imprimas dentro de la función.
Para [] devuelve listas y set vacíos, valor_total=0 y hay_agotados=False.
"""

import functools 
# TODO: importa reduce desde functools.

def generar_reporte(productos):
    # Productos disponibles
    disponibles = list(filter(lambda p: p['stock'] > 0, productos))
    nombres_disponibles = list(map(lambda p: p['nombre'], disponibles))

    # Valor total del inventario
    valor_total = functools.reduce(lambda acc, p: acc + p['precio'] * p['stock'], productos, 0)

    # Verificar si hay productos agotados
    hay_agotados = any(map(lambda p: p['stock'] == 0, productos))

    # Categorías únicas
    categorias = {p['categoria'] for p in productos}

    # Precios con recargo del 10%
    recargo = lambda precio: round(precio * 1.1, 2)
    precios_con_recargo = [(p['nombre'], recargo(p['precio'])) for p in disponibles]

    # Devolver el reporte
    return {
        "disponibles": nombres_disponibles,
        "valor_total": valor_total,
        "hay_agotados": hay_agotados,
        "categorias": categorias,
        "precios_con_recargo": precios_con_recargo
    }
