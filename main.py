import pandas as pd
import matplotlib.pyplot as plt
from matplotlib._cm_listed import cmaps


def armar_paises(datos) : # Aca armo una listita de paises para despues tener donde comparar en la otra funcion
    lista = []
    for key , value in datos.items():
        if(not value["location"] in lista):
            lista.append(value["location"])
    return lista

def armar_casos(datos,lista_paises):
    casos = []
    fecha = []
    for localizacion in lista_paises: #Lista paises es una lista de cada localizacion
        for key , value in datos.items(): #Buscamos que por cada pais me arme los casos y las fechas

            if (localizacion == value["location"] and value["new_cases"] != 0):
                casos.append(value["new_cases"])
                fecha.append(value["date"])
        armar_plot(casos,fecha,value["location"])#Aca mandamos la lista con los casos, y la fecha para hacer los plots, y el nombre unico del pais que no deberia variar


def armar_plot(casos,fechas,localidad):
    plt.figure(figsize=(18,6))
    plt.xlabel('Fechas')
    plt.ylabel('Casos Diarios')
    plt.scatter(fechas,casos)
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.plot(fechas,casos,label=localidad)
    plt.show()
    casos.clear()
    fechas.clear()



archivo = pd.read_csv("full_data.csv",usecols=['date','location','new_cases']) #Bastante util el usecols, me deja elegir que columnas del cvs quiero usar,
                                                                                # En vez de tener que complicarme con un drop del dataframe.

datos = archivo.to_dict("index") # Esto queda indexado como : {'date': '2020-01-01', 'location': 'Afghanistan', 'new_cases': 0.0}
paises_total = []
paises_total = armar_paises(datos)
#q pasises_a_buscar=input()
#print("Que paises con covid desea graficar? ELiga de la siguiente lista : /n",paises_total)
#paises_buscados = input()
#print(paises_buscados)
armar_casos(datos,paises_total)


