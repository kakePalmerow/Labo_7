"""EJERCICIO 04 — Funciones como valores y argumentos

ENUNCIADO
Completa aplicar_operacion: recibe una lista y una función; aplica esa
función a cada elemento usando un ciclo y devuelve una lista.
Completa transformar: crea un diccionario de funciones lambda con las claves
"doble", "cuadrado" y "negativo". Usa aplicar_operacion para obtener
un diccionario con esas mismas claves y las listas transformadas.
No uses map ni modifiques la lista original.
Con [] cada lista del resultado debe estar vacía.

Entrada de transformar: [1, 2, 3]
Resultado esperado:
{"doble": [2, 4, 6], "cuadrado": [1, 4, 9], "negativo": [-1, -2, -3]}

Entrada de aplicar_operacion: [2, 4] y una función que sume 1.
Resultado esperado: [3, 5]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 04".
"""

def aplicar_operacion(valores, operacion):
    # TODO: implementa lo solicitado y devuelve el resultado.
    for valor in range(len(valores)):
        valores[valor] = operacion(valores[valor])
    return valores


def transformar(valores):
    # TODO: crea el diccionario de funciones y aplica las operaciones.
    resultado = {"doble": [], "cuadrado": [], "negativo": []}

    funciones = {
        "doble": lambda x: x * 2,
        "cuadrado": lambda x: x ** 2,
        "negativo": lambda x: x * -1
    }

    for operacion in resultado:
        for valor in range(len(valores)):
            resultado[operacion].append(funciones[operacion](valores[valor]))

    return resultado
            


# Ejemplo de uso: inicialmente imprime None porque falta la implementación.
valores = [1, 2, 3]
print(transformar(valores))

# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
valores2 = [5, -7, 10]
print(transformar(valores2)) # {'doble': [10, -14, 20], 'cuadrado': [25, 49, 100], 'negativo': [-5, 7, -10]}
