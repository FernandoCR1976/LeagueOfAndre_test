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
cont_play=0
ans=True
contador=0


def list_emp():
    num_ran = round(random.randint(1,100),0)
    for i in range (num_ran):
        my_list.append(round(random.uniform(0.00, 8.99),2))

def crea_div():
    contador=0
    while contador < len(my_list):
        if (my_list[contador] >= 0.00) and (my_list[contador]) <= 0.99:
            hierro.append(my_list[contador])
        elif (my_list[contador] >= 1.00) and (my_list[contador]) <= 1.99:
            bronce.append(my_list[contador])
        elif (my_list[contador] >= 2.00) and (my_list[contador]) <= 2.99:
            plata.append(my_list[contador])
        elif (my_list[contador] >= 3.00) and (my_list[contador]) <= 3.99:
            oro.append(my_list[contador])
        elif (my_list[contador] >= 4.00) and (my_list[contador]) <= 4.99:
            platino.append(my_list[contador])
        elif (my_list[contador] >= 5.00) and (my_list[contador]) <= 5.99:
            diamante.append(my_list[contador])
        elif (my_list[contador] >= 6.00) and (my_list[contador]) <= 6.99:
            maestro.append(my_list[contador])
        elif (my_list[contador] >= 7.00) and (my_list[contador]) <= 7.99:
            gran_maestro.append(my_list[contador])
        elif (my_list[contador] >= 8.00) and (my_list[contador]) <= 8.99:
            retador.append(my_list[contador])
        else:
            print("DIGITO UN NUMERO INVALIDO")

        contador+=1           


def clsifica():
    
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
    print(" ")
    print(" ")
    print("***********CLASIFICACIÓN DE DIVISIONES***********")
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





def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

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

def listOrd():
    ordenada = my_list.copy() 
    ordenada.sort()

def mejorJugador():
    print(" ")
    print(" ")
    ordenada = my_list.copy() 
    ordenada.sort()
    mejor_jugador=ordenada[len(ordenada)-1]
    print("EL JUGADOR CON LA MAYOR DIVISION Y PUNTUACIÓN ES : ",mejor_jugador)
    print(" ")
    print(" ")     ###punto 5#### 

def menorJugador():
    print(" ")
    print(" ")
    ordenada = my_list.copy() 
    ordenada.sort()
    print("EL JUGADOR CON LA MENOR DIVISION Y MENOR PUNTUACIÓN ES : ",ordenada[0])####punto 6####
    print(" ")
    print(" ")


def consultLiga():
    print(" ")
    print(" ")
    print("***********CONSULTA DE PROMEDIO DE DIVISION***********")
    print("0 HIERRO")
    print("1 BRONCE")
    print("2 PLATA")
    print("3 ORO")
    print("4 PLATINO")
    print("5 DIAMANTE")
    print("6 MAESTRO")
    print("7 GRAN MAESTRO")
    print("8 RETADOR")
    consult_divi=int(input("INGRESE EL NUMERO DE DIVISION "))
    print(" ")
    print(" ")
    if consult_divi==0:
        print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION HIERRO ES DE: ",prom_div(hierro))
    elif consult_divi==1:
        print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION BRONCE ES DE: ",prom_div(bronce))
    elif consult_divi==2:
        print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION PLATA ES DE: ",prom_div(plata))
    elif consult_divi==3:
        print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION ORO ES DE: ",prom_div(oro))
    elif consult_divi==4:
        print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION PLATINO ES DE: ",prom_div(platino))
    elif consult_divi==5:
        print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION DIAMANTE ES DE: ",prom_div(diamante))
    elif consult_divi==6:
        print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION MAESTRO ES DE: ",prom_div(maestro))
    elif consult_divi==7:
        print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION GRAN MAESTRO ES DE: ",prom_div(gran_maestro))
    elif consult_divi==8:
        print("EL PROMEDIO DE PUNTUACIÓN DE LA DIVISION RETADOR ES DE: ",prom_div(retador))
    else:
        print("SELECCION NO VALIDA")
    print(" ")
    print(" ")


def promDiv():
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
    print(" ")
    print(" ")


def jugad_lista():
    print(" ")
    print(" ")
    print("***********LISTA DE JUGADORES ALEATORIA***********")
    print(my_list)
    print(" ")
    print(" ")
    

def prom_Todos():
    total=(prom_div(hierro)+prom_div(bronce)+prom_div(plata)+prom_div(oro)+prom_div(platino)+prom_div(diamante)+prom_div(maestro)+prom_div(gran_maestro)+prom_div(retador))/9
    print(" ")
    print(" ")
    return total
    
def promedio_todos():
    print(" ")
    print(" ")
    print("EL PROMEDIO DE PUNTUACION DE TODAS LAS DIVISIONES ES : ",prom_Todos())
    print(" ")
    print(" ")
    
def cantJugadores():
    print("***********CANTIDAD DE JUGADORES POR DIVISION***********") ##punto 10##
    print(" ")
    print(" ")
    print("HIERRO ",len(hierro), "JUGADORES")
    print("BRONCE ",len(bronce),"JUGADORES")
    print("PLATA ",len(plata), "JUGADORES")
    print("ORO ",len(oro), "JUGADORES")
    print("PLATINO",len(platino), "JUGADORES")
    print("DIAMANTE ",len(diamante), "JUGADORES")
    print("MAESTRO ",len(maestro), "JUGADORES")
    print("GRAN MAESTRO ",len(gran_maestro), "JUGADORES")
    print("RETADOR ",len(retador), "JUGADORES")
    print(" ")
    print(" ")


def num_jugadores():
    print(" ")
    print(" ")
    print("HAY ",len(my_list), "JUGADORES")
    print(" ")
    print(" ")



########LISTA DE EMPAREJAMIENTO########





print("-------BIENVENIDO A LIGUE OF ANDRE-------")
print("                  /\                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                  ||                     ")    
print("                  ||                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                [====]                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                 [==]                     ")
print("-----------------------------------------")
print(" ")


while ans:
    print("1. Generar lista de emparejamiento.")
    print("2. Ordenar los jugadores en las listas.")
    print("3. Mostrar la lista inicial de jugadores.")
    print("4. Mostrar las listas de cada división luego de ubicar a los jugadores.")
    print("5. El jugador con mayor división y puntuación.")
    print("6. El jugador con menor división y menor puntuación.")
    print("7. El promedio de todas las divisiones en base a cuantos jugadores contiene.")
    print("8. El promedio de puntuación dada una división.")
    print("9. El promedio de puntuación de todas las divisiones.")
    print("10. Cantidad de jugadores por división.")
    print("11. Cantidad de jugadores totales.")
    print("12. Salir del programa.")
    print(" ")
    menu_select=int(input("POR FAVOR INGRESE LA OPCION DESEADA "))    

    if menu_select==1:
        
        list_emp()
        crea_div()
        print(" ")
        input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")       
    
    elif menu_select==2:
        
        listOrd()
        print(" ")
        input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
        
    elif menu_select==3:
        
        jugad_lista()
        input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
    
    elif menu_select==4:
        
        clsifica()
        input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
    
    elif menu_select==5:
        
        mejorJugador() 
        input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

    elif menu_select==6:
        
        menorJugador()
        input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

    elif menu_select==7:
        
        promDiv()
        input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

    elif menu_select==8:
        
        consultLiga()
        input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

    elif menu_select==9:

        promedio_todos()
        input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

    elif menu_select==10:

        cantJugadores()       
        input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
    
    elif menu_select==11:

        num_jugadores()
        input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

    elif menu_select == 12:
        ans = False


