from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd


def convertir(string):
    li = list(string.split(" "))
    return li


def armar_paises(datos):  # Aca armo una listita de paises para despues tener donde comparar en la otra funcion
    lista = []
    for key, value in datos.items():
        if (not value["location"] in lista):
            lista.append(value["location"])
    return lista


def armar_casos(datos, lista_paises):
    global Pais
    casos = []
    fecha = []
    muertes = []
    for localizacion in lista_paises:  # Lista paises es una lista de cada localizacion
        for key, value in datos.items():  # Buscamos que por cada pais me arme los casos y las fechas

            if localizacion == value["location"] and value["total_cases"] != 0:
                casos.append(value["total_cases"])
                aux = datetime.strptime(value["date"], '%Y-%m-%d')
                fecha.append(aux)
                Pais = value["location"]
                muertes.append(value["total_deaths"])
        armar_plot(casos, fecha, Pais, muertes)  # Aca mandamos la lista con los casos, y la fecha para hacer los
        # plots, y el nombre unico del pais que no deberia variar


plt.show()


def armar_plot(casos_totales, fechas, localidad, muertes_totales):
    plt.figure(figsize=(18, 6))
    plt.xlabel('Fechas')
    plt.ylabel('Casos Diarios')
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.plot(fechas, casos_totales, label='Casos totales')
    plt.plot(fechas, muertes_totales, label='Muertes Pais')
    plt.legend()
    print(localidad)
    plt.title("Pais : {}".format(localidad))
    plt.show()
    casos_totales.clear()
    fechas.clear()
    muertes_totales.clear()


archivo = pd.read_csv("full_data.csv", usecols=['date', 'location', 'total_cases', 'total_deaths'])
# Bastante util el usecols, me deja elegir que columnas del cvs quiero
# , en vez de tener que complicarme con un drop del dataframe.

datos = archivo.to_dict("index")
paises_total = []
paises_total = armar_paises(datos)
lista_paises = ['Anguilla']
centinela = 'Chau'
while centinela != 'Hola':  # un control de error humilde, que no este vacia la lista, y que exista en la lista de datos que tenemos
    print("Que paises con covid desea graficar? ELiga de la siguiente lista :\n", paises_total)
    lista_paises = input()
    lista_paises = convertir(lista_paises)
    print(lista_paises)
    if not lista_paises:
        print("Error! La lista esta vacia!")
    result = all(elem in paises_total for elem in lista_paises)
    if result == False:
        print("Error! Ese pais no se encuentra en el csv de paises! Intente con otro!")
    else:
        centinela = 'Hola'

else:

    armar_casos(datos, lista_paises)
