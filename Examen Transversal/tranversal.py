import os
os.system("cls")

import random
import statistics as st
import csv
from statistics import geometric_mean

trabajadores = ["Juan Perez", "Maria Garcia","Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
sueldos = {}

def validarNumero(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print("Solo se permiten numeros")
        else:
            return num    

def asignarSueldo():
    global sueldos
    sueldos = {nombre: random.randint(300000, 2500000) for nombre in trabajadores}
    print("""
    ------------------------------------------------
     Se han generado los sueldos de forma aleatoria.
    ------------------------------------------------
          """)
    
def clasificarSueldo():
    for nombre, sueldosB in sueldos.items():
        if sueldosB < 800000:
            clasificacion = "Sueldos menores a $800.000"
        elif 800000 <= sueldosB <= 2000000:
            clasificacion = "Sueldos entre $800.000 y $2.000.000"
        elif sueldosB > 2000000:
            clasificacion = "Sueldos superiores a $2.000.000"
        print (f"Nombre: {nombre}, Sueldo Base: ${sueldosB}, Clasificación: {clasificacion}")
   
def verStats():
    sueldoValues = list(sueldos.values())
    sueldoAlto = max(sueldoValues)
    sueldoBajo= min(sueldoValues)
    sueldoPromedio= st.mean(sueldoValues)
    mediaGeometrica = round(geometric_mean(sueldoValues), 1)
    print ("-------------Estadisticas-------------")
    print("")
    print (f"Sueldo mas alto: ${sueldoAlto}")
    print (f"Sueldo mas Bajo: ${sueldoBajo}")
    print (f"Sueldo promedio: ${sueldoPromedio}")
    print(f"Media geometrica: ${mediaGeometrica}")
    print("")
    menu()

def reporteSueldos():
    with open("reporteSueldos.csv","w") as archivo_csv:
     lector_csv = csv.writer(archivo_csv)
     lector_csv.writerow(["Nombre del empleado", "Sueldo base", "Descuento salud", "Descuento AFP", "Sueldo liquido"])
     for nombre, sueldosB in sueldos.items():
      salud = round(sueldosB * 0.07)
      afp = round(sueldosB * 0.12)
      liquido = round(sueldosB - salud - afp)
      lector_csv.writerow([ nombre, sueldosB, salud, afp, liquido])
      print("Nombre:", nombre, "Sueldo: $", sueldosB,"Descuento Salud: $",salud,"Descuento AFP: $",afp, "Sueldo liquido: $",liquido)      

def salir():
    print("\nFinalizando el programa...")
    print("Desarrollado por Matias Vargas")
    print("RUT 21.648.765-6")
    print("")
    exit()

def menu():
    print("-------------Menu-------------")
    print("""
    1. Asignar sueldos aleatorios
    2. Clasificar sueldos
    3. Ver estadisticas
    4. Reporte de sueldos
    5. Salir del programa""")
    print("")
    while True:
        op = validarNumero("Seleccione una opcion: ")

        if op == 1:
            asignarSueldo()
        if op == 2:
            clasificarSueldo()
        if op == 3:
            verStats()
        if op == 4:
            reporteSueldos()
        if op == 5:
            salir()             

menu()