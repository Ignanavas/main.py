import pandas as pd
import matplotlib.pyplot as plt

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

            #if (localizacion == value["location"]):
                #casos.append(value["new_cases"])
                #fecha.append(value["date"])
        #armar_plot(casos,fecha,value["location"])#Aca mandamos la lista con los casos, y la fecha para hacer los plots, y el nombre unico del pais que no deberia variar


#"def armar_plot(casos,fechas,localidad):
    #plt.figure(figsize=(18,6))
    #plt.xlabel('Fechas')
    #plt.ylabel('Casos Diarios')
    #plt.xticks(rotation=90)
    #plt.plot(fechas,casos)
    #plt.yscale('log')
    #plt.xscale('log')
    #plt.grid()
   # plt.show()



archivo = pd.read_csv("full_data.csv",usecols=['date','location','new_cases']) #Bastante util el usecols, me deja elegir que columnas del cvs quiero usar,
                                                                                # En vez de tener que complicarme con un drop del dataframe.

datos = archivo.to_dict("index") # Esto queda indexado como : {'date': '2020-01-01', 'location': 'Afghanistan', 'new_cases': 0.0}
paises_total = []
paises_total = armar_paises(datos)
print(paises_total)
armar_casos(datos,paises_total)


