# Definimos una matriz bidimensional de 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    # Recorremos cada fila de la matriz
    for i in range(len(matriz)):
        # Recorremos cada columna de la fila actual
        for j in range(len(matriz[i])):
            # Si encontramos el valor, devolvemos su posición
            if matriz[i][j] == valor:
                return (i, j)
    # Si no encontramos el valor, devolvemos None
    return None

# Definimos el valor que queremos buscar
valor_a_buscar = 5

# Llamamos a la función de búsqueda
posicion = buscar_valor(matriz, valor_a_buscar)

# Función para mostrar el resultado de la búsqueda
def mostrar_resultado(posicion, valor):
    if posicion is not None:
        # Si encontramos el valor, mostramos su posición
        return f'El valor {valor} se encontró en la posición: {posicion}'
    else:
        # Si no encontramos el valor, indicamos que no se encontró
        return f'El valor {valor} no se encontró en la matriz.'

# Mostramos el resultado
mensaje = mostrar_resultado(posicion, valor_a_buscar)
print(mensaje)
