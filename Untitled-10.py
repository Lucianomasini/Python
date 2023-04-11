
nombres = ['Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
           'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
           'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
           'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
           'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
           'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
           'Yanina']

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def crear_diccionario(nombres, notas_1, notas_2):
    diccionario_notas = {}
    for nombre, nota1, nota2 in zip(nombres, notas_1, notas_2):
        notas = [nota1, nota2]
        diccionario_notas[nombre] = notas
    return diccionario_notas

print(crear_diccionario(nombres, notas_1, notas_2))

diccionario_notas = crear_diccionario(nombres, notas_1, notas_2)

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def calcular_promedio_estudiantes(diccionario_notas):
    promedios = {}
    for nombre, notas in diccionario_notas.items():
        promedio = calcular_promedio(notas)
        promedios[nombre] = promedio
    return promedios

print(calcular_promedio_estudiantes(diccionario_notas))

def calcular_promedio_clase(diccionario_notas):
    notas_totales = []
    for notas in diccionario_notas.values():
        notas_totales.extend(notas)
    return sum(notas_totales) / len(notas_totales)

print(calcular_promedio_clase(diccionario_notas))

promedios = calcular_promedio_estudiantes(diccionario_notas)

def estudiante_con_mayor_promedio(promedios):
    mayor_promedio = max(promedios, key=promedios.get)
    return mayor_promedio

print(estudiante_con_mayor_promedio(promedios))

def estudiante_con_menor_nota(diccionario_notas):
    menor_nota = min(sum(notas) for notas in diccionario_notas.values())
    alumno_nota_menor = next(nombre for nombre, notas in diccionario_notas.items() if sum(notas) == menor_nota)
    return alumno_nota_menor

print(estudiante_con_menor_nota(diccionario_notas))