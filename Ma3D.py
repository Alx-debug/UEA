import numpy as np

# Definir las ciudades y los parámetros de la matriz
num_ciudades = 3
num_dias = 7
num_semanas = 4
ciudades = ['CiudadA', 'CiudadB', 'CiudadC']

# Crear la matriz 3D con temperaturas aleatorias
matriz_temperaturas = np.random.randint(15, 31, (num_semanas, num_dias, num_ciudades))

# Inicializar un array para almacenar los promedios semanales
promedios_semanales = np.zeros((num_semanas, num_ciudades))

# Calcular el promedio de temperaturas por ciudad y semana
for semana in range(num_semanas):
    for ciudad in range(num_ciudades):
        promedios_semanales[semana][ciudad] = np.mean(matriz_temperaturas[semana][:, ciudad])

# Visualizar los resultados
for i, ciudad in enumerate(ciudades):
    print(f'Promedios de temperaturas para {ciudad}:')
    for semana in range(num_semanas):
        print(f'Semana {semana + 1}: {promedios_semanales[semana][i]:.2f} grados')
    print('')
