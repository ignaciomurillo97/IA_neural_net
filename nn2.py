#!/bin/python3
import random
import math

''' 
  Rubro              | Porcentaje
  1 Examen 1         : 35
  2 Examen 2         : 20
  3 Proyecto 1       : 15
  4 Proyecto 2       : 5
  5 Tareas           : 10
  6 Trabajo en clase : 15
'''

pesosReales = [0.35, 0.20, 0.15, 0.05, 0.10, 0.15]
learnRate = 0.001

def generarPesosIniciales():
    pesos = []
    for i in range(7):
        pesos.append(random.random())
    return pesos

def generarNotasIniciales():
    notas = []
    for i in range(6):
        # notas.append(random.randint(0, 100))
        notas.append(random.random())
    return notas

def aproboSegunNotas(notas):
    notaFinal = sum([notas[i] * pesosReales[i] for i in range(len(notas) - 1)])
    if (notaFinal >= 0.7):
       return 1 
    return 0

def generarDatosEntrenamiento(cantidad):
    setEntrenamiento = []
    for i in range(cantidad):
        n = generarNotasIniciales()
        setEntrenamiento.append((n, aproboSegunNotas(n)))
    return setEntrenamiento

# Neural Net
def sigmoid(x):
    if x > 0:
        return x
    return 0

def neurona(entradas, pesos):
    if (len(entradas) != len(pesos)):
        print('las entradas y los pesos no tienen el mismo tamano')
        exit(2)
    suma = sum([entradas[i] * pesos[i] for i in range(len(entradas))])
    sig = sigmoid(suma)
    return sig

def truncate(number, digits):
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper

# Entrenamiento
def calcularError(resultado, esperado):
    return esperado - resultado

def calcularNuevoPeso(pesoActual, error):
    nuevoPeso = pesoActual + (pesoActual * error * learnRate)
    return nuevoPeso

def ajustarPesos(pesosActuales, error):
    return [calcularNuevoPeso(peso, error) for peso in pesosActuales]

def aprender(iteraciones):
    conjuntoDeAprendizaje = [generarNotasIniciales() + [1] for _ in range(iteraciones)]
    pesos = generarPesosIniciales()
    for i, nota in enumerate(conjuntoDeAprendizaje):
        res = neurona(nota, pesos)
        resEsperado = aproboSegunNotas(nota)
        error = calcularError(res, resEsperado)
        print(i, res, resEsperado, error)
        nuevosPesos = ajustarPesos(pesos, error)
        pesos = nuevosPesos
    return pesos

def probar(pesos):
    notaPaso = [1, 1, 1, 1, 1, 1, 1]
    notaQuedo = [0.1, 1, 1, 1, 1, 1, 1]
    print(neurona(notaPaso, pesos))
    print(neurona(notaQuedo, pesos))

def main():
    test = aprender(1000000)
    print(test) 
    probar(test)

if __name__ == '__main__':
    main()
