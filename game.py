from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
print(f"Recuerde escribir el resultado de la división solo con 3 decimales en caso de ser necesario")
for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    
# Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
# Le pedimos al usuario el resultado
    result = input()
    resultado = float(result)
# Le pedimos que nos diga si está bien o mal
    if operator == "+" and (resultado == (number_1 + number_2)):
        print(f"El resultado esta bien")
    elif operator == "-" and (resultado == (number_1 - number_2)):
        print(f"El resultado esta bien")
    elif operator == "*" and (resultado == (number_1 * number_2)):
        print(f"El resultado esta bien")
    elif operator == "/" and (not number_2 == 0) and (resultado == round((number_1 / number_2), 3)):
        print(f"El resultado esta bien")
    else:
        if ((operator == "/") and (number_2 == 0)):
            print(f"La división por cero no está definida")
        else:
            print(f"El resultado esta mal")

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")