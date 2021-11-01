import random

my_list=[]
hierro=[]
bronce=[]
plata=[]
oro=[]
platino=[]
diamante=[]
maestro=[]
gran_maestro=[]
retador=[]
hierro_ord=[]
bronce_ord=[]
plata_ord=[]
oro_ord=[]
platino_ord=[]
diamante_ord=[]
maestro_ord=[]
gran_maestro_ord=[]
retador_ord=[]



num_ran = round(random.randint(1,100),0)

for i in range (num_ran):
    my_list.append(round(random.uniform(0.00, 8.99),2))

ordenada = my_list.copy() 
ordenada.sort()

print(" ")
print(" ")
print("***********LISTA DE JUGADORES ALEATORIA***********")
print(" ")
print(" ")
print(my_list)
print("SE GENERARON ",len(my_list)," jugadores")
print(" ")
print(" ")
# print("***********LISTA DE JUGADORES ORDENADA***********")
# print(" ")
# print(" ")
# print(ordenada)
# print("SE GENERARON ",len(ordenada)," jugadores")
# print(" ")
# print(" ")
input("PRESIONE ENTER PARA CONTINUAR")
print(" ")
print(" ")

contador=0
print("***********CLASIFICACIÓN DE JUGADORES ALEATORIA***********")
print(" ")
print(" ")
while contador < len(my_list):

    if (my_list[contador] >= 0.00) and (my_list[contador]) <= 0.99:
        hierro.append(my_list[contador])
        print("El jugador ",my_list[contador]," pertenece a la liga HIERRO \n")
    elif (my_list[contador] >= 1.00) and (my_list[contador]) <= 1.99:
        print("El jugador ",my_list[contador]," pertenece a la liga BRONCE \n")
        bronce.append(my_list[contador])
    elif (my_list[contador] >= 2.00) and (my_list[contador]) <= 2.99:
        plata.append(my_list[contador])
        print("El jugador ",my_list[contador]," pertenece a la liga PLATA \n")
    elif (my_list[contador] >= 3.00) and (my_list[contador]) <= 3.99:
        oro.append(my_list[contador])
        print("El jugador ",my_list[contador]," pertenece a la liga ORO \n")
    elif (my_list[contador] >= 4.00) and (my_list[contador]) <= 4.99:
        platino.append(my_list[contador])
        print("El jugador ",my_list[contador]," pertenece a la liga PLATINO \n")
    elif (my_list[contador] >= 5.00) and (my_list[contador]) <= 5.99:
        diamante.append(my_list[contador])
        print("El jugador ",my_list[contador]," pertenece a la liga DIAMANTE \n")
    elif (my_list[contador] >= 6.00) and (my_list[contador]) <= 6.99:
        maestro.append(my_list[contador])
        print("El jugador ",my_list[contador]," pertenece a la liga MAESTRO \n")
    elif (my_list[contador] >= 7.00) and (my_list[contador]) <= 7.99:
        gran_maestro.append(my_list[contador])
        print("El jugador ",my_list[contador]," pertenece a la liga GRAN MAESTRO \n")
    elif (my_list[contador] >= 8.00) and (my_list[contador]) <= 8.99:
        retador.append(my_list[contador])
        print("El jugador ",my_list[contador]," pertenece a la liga GRAN MAESTRO \n")

    contador+=1
input("PRESIONE ENTER PARA CONTINUAR")
# print(" ")
# print(" ")
# print("***********CLASIFICACIÓN DE JUGADORES ORDENADA***********")
# print(" ")
# print(" ")

# contador2=0
# while contador2 < len(ordenada):

#     if (ordenada[contador2] >= 0.00) and (ordenada[contador2]) <= 0.99:
#         print("El jugador ",ordenada[contador2]," pertenece a la liga HIERRO \n")
#     elif (ordenada[contador2] >= 1.00) and (ordenada[contador2]) <= 1.99:
#         print("El jugador ",ordenada[contador2]," pertenece a la liga BRONCE \n")
#     elif (ordenada[contador2] >= 2.00) and (ordenada[contador2]) <= 2.99:
#         print("El jugador ",ordenada[contador2]," pertenece a la liga PLATA \n")
#     elif (ordenada[contador2] >= 3.00) and (ordenada[contador2]) <= 3.99:
#         print("El jugador ",ordenada[contador2]," pertenece a la liga ORO \n")
#     elif (ordenada[contador2] >= 4.00) and (ordenada[contador2]) <= 4.99:
#         print("El jugador ",ordenada[contador2]," pertenece a la liga PLATINO \n")
#     elif (ordenada[contador2] >= 5.00) and (ordenada[contador2]) <= 5.99:
#         print("El jugador ",ordenada[contador2]," pertenece a la liga DIAMANTE \n")
#     elif (ordenada[contador2] >= 6.00) and (ordenada[contador2]) <= 6.99:
#         print("El jugador ",ordenada[contador2]," pertenece a la liga MAESTRO \n")
#     elif (ordenada[contador2] >= 7.00) and (ordenada[contador2]) <= 7.99:
#         print("El jugador ",ordenada[contador2]," pertenece a la liga GRAN MAESTRO \n")
#     elif (ordenada[contador2] >= 8.00) and (ordenada[contador2]) <= 8.99:
#         print("El jugador ",ordenada[contador2]," pertenece a la liga GRAN MAESTRO \n")

#     contador2+=1
input("PRESIONE ENTER PARA CONTINUAR")
print(" ")
print(" ")
print("***********CLASIFICACIÓN DE DIVISIONES***********") ##punto 4##
print(" ")
print(" ")
print("HIERRO ",hierro)
print("BRONCE ",bronce)
print("PLATA ",plata)
print("ORO ",oro)
print("PLATINO",platino)
print("DIAMANTE ",diamante)
print("MAESTRO ",maestro)
print("GRAN MAESTRO ",gran_maestro)
print("RETADOR ",retador)

input("PRESIONE ENTER PARA CONTINUAR")
print(" ")
print(" ")

hierro_ord=hierro.copy()
hierro_ord.sort()
bronce_ord=bronce.copy()
bronce_ord.sort()
plata_ord=plata.copy()
oro_ord=oro.copy()
oro_ord.sort()
platino_ord=platino.copy()
platino_ord.sort()
diamante_ord=diamante.copy()
diamante_ord.sort()
maestro_ord=maestro.copy()
maestro_ord.sort()
gran_maestro_ord=gran_maestro.copy()
gran_maestro_ord.sort()
retador_ord=retador.copy()
retador_ord.sort()

print("***********CLASIFICACIÓN DE DIVISIONES ORDENADA***********") ##punto 5##
print(" ")
print(" ")
print("HIERRO ",hierro_ord)
print("BRONCE ",bronce_ord)
print("PLATA ",plata_ord)
print("ORO ",oro_ord)
print("PLATINO",platino_ord)
print("DIAMANTE ",diamante_ord)
print("MAESTRO ",maestro_ord)
print("GRAN MAESTRO ",gran_maestro_ord)
print("RETADOR ",retador_ord)
print(" ")
print(" ")
input("PRESIONE ENTER PARA CONTINUAR")
print(" ")
print(" ")
mejor_jugador=ordenada[len(ordenada)-1]
print("EL JUGADOR CON LA MAYOR DIVISION Y PUNTUACIÓN ES : ",mejor_jugador)###punto 5####
print("EL JUGADOR CON LA MENOR DIVISION Y MENOR PUNTUACIÓN ES : ",ordenada[0])####punto 6####

def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

print(" ")
print(" ")
input("PRESIONE ENTER PARA CONTINUAR")
print(" ")
print(" ")
print("EL PROMEDIO DE TODAS LAS DIVISIONES ES: ",round(sumalista(ordenada)/int(len(ordenada)),2))


def prom_div(listaNumeros):
    laSuma = 0
    promedio=0
    if len(listaNumeros)!=0:
        for i in listaNumeros:
            laSuma = laSuma + i
            promedio = round((((laSuma / int(len(listaNumeros)))%1)*100),2)
    else:
        promedio=0    
    return promedio


    
print(" ")
print(" ")
print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION HIERRO ES DE: ",prom_div(hierro))
print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION BRONCE ES DE: ",prom_div(bronce))
print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION PLATA ES DE: ",prom_div(plata))
print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION ORO ES DE: ",prom_div(oro))
print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION PLATINO ES DE: ",prom_div(platino))
print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION DIAMANTE ES DE: ",prom_div(diamante))
print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION MAESTRO ES DE: ",prom_div(maestro))
print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION GRAN MAESTRO ES DE: ",prom_div(gran_maestro))
print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION RETADOR ES DE: ",prom_div(retador))
