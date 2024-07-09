#programa que determina secuencias por repeticion
#elaborado por:Diego Yepez                                                                       fecha02/07/20224
#var. de entrada
numero = int
#var. de salida
factoria_numero_n = int
#var. de proceso
factoria = 1
#lectura de datos
#inicializacion de variablees
#procesamiento de datos
numero = int(input("ingrese numero entero positivo: "))
for k in range(1,numero + 1):
    factoria = factoria * k
    
#escritura de resultados
print("el numero de factoria es: " + str(factoria))
#fin del programa
