import random


######################Se generan las variables que se van a utilizar en el programa#####################
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
contador=0
#######Fin de las variables######


############ FUNCIONES ########

def list_emp():  #Genera una lista de 1 a 100 numeros aleatorios con valores de  0.00 a 8.99
    num_ran = random.randint(1,100)
    for i in range (num_ran):
        my_list.append(round(random.uniform(0.00, 8.99),2))

def crea_div(): #Genera las divisiones en base a la lista que define la funcion list_emp
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


def clasifica(): #Ordena y clasifica cada una de las divisiones creadas en crea_div, OPCION 4 DEL MENU PRINCIPAL
    
    hierro_ord=hierro.copy()
    hierro_ord.sort()
    bronce_ord=bronce.copy()
    bronce_ord.sort()
    plata_ord=plata.copy()
    plata_ord.sort()
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
    
    print("\n","***********CLASIFICACI??N DE DIVISIONES***********\n"," HIERRO ",hierro_ord ,
    "\n  BRONCE ",bronce_ord,"\n  PLATA ",plata_ord,"\n  ORO ",oro_ord,"\n  PLATINO",platino_ord,
    "\n  DIAMANTE ",diamante_ord,"\n  MAESTRO ",maestro_ord,"\n  GRAN MAESTRO ",gran_maestro_ord,
    "\n  RETADOR ",retador_ord,"\n")


def prom_div(lista_numeros): #Funcion para calcular el promedio del valor residual de una lista de numeros
    la_suma = 0
    promedio=0
    if len(lista_numeros)!=0:
        for i in lista_numeros:
            la_suma = la_suma + i
            promedio = round((((la_suma / int(len(lista_numeros)))%1)*100),2)
    else:
        promedio=0    
    return promedio

def list_ord(): #Esta funcion ordena de menor a mayor my_list, con esto podemos saber cual es el valor menor y el valor mayor de la lista
    if len(my_list)!=0:
        ordenada = my_list.copy() 
        ordenada.sort()
    else:
        print("\n","NO EXISTEN DIVISIONES CREADAS, Seleccione la opcion 1 en el menu principal","\n")
        

def mejor_jugador(): #Esta funci??n devuelve el ultimo valor de la lista ordenada
    if len(my_list)!=0:

        ordenada = my_list.copy() 
        ordenada.sort()
        mejor_jugador=ordenada[len(ordenada)-1]
        print("\n","EL JUGADOR CON LA MAYOR DIVISION Y PUNTUACI??N ES : ",mejor_jugador,"\n")
        
    else:        
        print("\n","NO EXISTEN DIVISIONES CREADAS, Seleccione la opcion 1 en el menu principal","\n")
        

def menor_jugador(): #Esta funcion devuelve el primer valor de la lista ordenada
    if len(my_list)!=0:

        ordenada = my_list.copy() 
        ordenada.sort()
        print("\n","EL JUGADOR CON LA MENOR DIVISION Y MENOR PUNTUACI??N ES : ",ordenada[0],"\n")####punto 6####
    
    else:
        print("\n","NO EXISTEN DIVISIONES CREADAS, Seleccione la opcion 1 en el menu principal","\n")
    

def consulta_liga(): #Esta funcion calcula el promedio de una division dada
    if len(my_list)!=0:

        print("\n","***********CONSULTA DE PROMEDIO DE DIVISION***********"
        ,"\n","0 HIERRO","\n","1 BRONCE","\n",
        "2 PLATA","\n","3 ORO","\n","4 PLATINO","\n","5 DIAMANTE","\n","6 MAESTRO","\n",
        "7 GRAN MAESTRO","\n","8 RETADOR","\n")
        
        consult_divi=int(input("INGRESE EL NUMERO DE DIVISION \n"))
        
        if consult_divi==0:
            print("EL PROMEDIO DE PUNTUACI??N DE LA DIVISION HIERRO ES DE: ",prom_div(hierro))
        elif consult_divi==1:
            print("EL PROMEDIO DE PUNTUACI??N DE LA DIVISION BRONCE ES DE: ",prom_div(bronce))
        elif consult_divi==2:
            print("EL PROMEDIO DE PUNTUACI??N DE LA DIVISION PLATA ES DE: ",prom_div(plata))
        elif consult_divi==3:
            print("EL PROMEDIO DE PUNTUACI??N DE LA DIVISION ORO ES DE: ",prom_div(oro))
        elif consult_divi==4:
            print("EL PROMEDIO DE PUNTUACI??N DE LA DIVISION PLATINO ES DE: ",prom_div(platino))
        elif consult_divi==5:
            print("EL PROMEDIO DE PUNTUACI??N DE LA DIVISION DIAMANTE ES DE: ",prom_div(diamante))
        elif consult_divi==6:
            print("EL PROMEDIO DE PUNTUACI??N DE LA DIVISION MAESTRO ES DE: ",prom_div(maestro))
        elif consult_divi==7:
            print("EL PROMEDIO DE PUNTUACI??N DE LA DIVISION GRAN MAESTRO ES DE: ",prom_div(gran_maestro))
        elif consult_divi==8:
            print("EL PROMEDIO DE PUNTUACI??N DE LA DIVISION RETADOR ES DE: ",prom_div(retador))
        else:
            print("\n","SELECCION NO VALIDA","\n")
    
    else:
        print("\n","NO EXISTEN DIVISIONES CREADAS, Seleccione la opcion 1 en el menu principal","\n")
        

def promedio_divisiones(): #Esta funcion devuelve el promedio cada una de las divisiones
    if len(my_list)!=0:

        print("\n EL PROMEDIO DE PUNTUACI??N DE LA DIVISION HIERRO ES DE: ",prom_div(hierro),
        "\n EL PROMEDIO DE PUNTUACI??N DE LA DIVISION BRONCE ES DE: ",prom_div(bronce),
        "\n EL PROMEDIO DE PUNTUACI??N DE LA DIVISION PLATA ES DE: ",prom_div(plata),
        "\n EL PROMEDIO DE PUNTUACI??N DE LA DIVISION ORO ES DE: ",prom_div(oro),
        "\n EL PROMEDIO DE PUNTUACI??N DE LA DIVISION PLATINO ES DE: ",prom_div(platino),
        "\n EL PROMEDIO DE PUNTUACI??N DE LA DIVISION DIAMANTE ES DE: ",prom_div(diamante),
        "\n EL PROMEDIO DE PUNTUACI??N DE LA DIVISION MAESTRO ES DE: ",prom_div(maestro),
        "\n EL PROMEDIO DE PUNTUACI??N DE LA DIVISION GRAN MAESTRO ES DE: ",prom_div(gran_maestro),
        "\n EL PROMEDIO DE PUNTUACI??N DE LA DIVISION RETADOR ES DE: ",prom_div(retador),"\n")
    
    else:
        print("\n","NO EXISTEN DIVISIONES CREADAS, Seleccione la opcion 1 en el menu principal","\n")
        

def jugad_lista(): #Esta funcion imprime my_list
    if len(my_list)!=0:

        print("\n","***********LISTA DE JUGADORES ALEATORIA***********","\n",my_list,"\n")
    else:
        print("\n","NO EXISTEN DIVISIONES CREADAS, Seleccione la opcion 1 en el menu principal","\n")
        

def prom_todas_divisiones(): #esta funcion calcula el promedio de todas las divisiones

    promedio=(prom_div(hierro)+prom_div(bronce)+prom_div(plata)+prom_div(oro)+prom_div(platino)+prom_div(diamante)+prom_div(maestro)+prom_div(gran_maestro)+prom_div(retador))/9
    print(" ")
    total=round(promedio,2)
    
    return total
    
def promedio_todos(): #Esta funcion imprime el promedio de todas las divisiones
    if len(my_list)!=0:

        print("\n","EL PROMEDIO DE PUNTUACION DE TODAS LAS DIVISIONES ES : ",prom_todas_divisiones(),"\n")
        
    else:
        print("\n","NO EXISTEN DIVISIONES CREADAS, Seleccione la opcion 1 en el menu principal","\n")
            
def cant_jugadores(): # esta funcion imprime los jugadores de cada divisi??n
    if len(my_list)!=0:

        print("\n","***********CANTIDAD DE JUGADORES POR DIVISION***********","\n", 
        "HIERRO ",len(hierro), "JUGADORES \n",
        "BRONCE ",len(bronce),"JUGADORES \n",
        "PLATA ",len(plata), "JUGADORES \n",
        "ORO ",len(oro), "JUGADORES \n",
        "PLATINO",len(platino), "JUGADORES \n",
        "DIAMANTE ",len(diamante), "JUGADORES \n",
        "MAESTRO ",len(maestro), "JUGADORES \n",
        "GRAN MAESTRO ",len(gran_maestro), "JUGADORES \n",
        "RETADOR ",len(retador), "JUGADORES \n")
        
    else:
        print("\n","NO EXISTEN DIVISIONES CREADAS, Seleccione la opcion 1 en el menu principal","\n")
        
  
def num_jugadores(): #esta funcion imprime la cantidad de jugadores
    if len(my_list)!=0:
        print("\n","HAY ",len(my_list), "JUGADORES","\n")
    else:
        print("\n","NO EXISTEN DIVISIONES CREADAS, Seleccione la opcion 1 en el menu principal","\n")


def menu():
    ans=True
    while ans:
        print("\n","1. Generar lista de emparejamiento.","\n 2. Ordenar los jugadores en las listas. ",
        "\n 3. Mostrar la lista inicial de jugadores.",
        "\n 4. Mostrar las listas de cada divisi??n luego de ubicar a los jugadores.",
        "\n 5. El jugador con mayor divisi??n y puntuaci??n.",
        "\n 6. El jugador con menor divisi??n y menor puntuaci??n. ",
        "\n 7. El promedio de todas las divisiones en base a cuantos jugadores contiene.",
        "\n 8. El promedio de puntuaci??n dada una divisi??n.",
        "\n 9. El promedio de puntuaci??n de todas las divisiones.",
        "\n 10. Cantidad de jugadores por divisi??n.",
        "\n 11. Cantidad de jugadores totales. \n 12. Salir del programa.","\n")
        
        menu_select=int(input("POR FAVOR INGRESE LA OPCION DESEADA "))    

        if menu_select==1:
            
            list_emp()
            crea_div()
            print(" ")
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")       
        
        elif menu_select==2:
            
            list_ord()
            print(" ")
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
            
        elif menu_select==3:
            
            jugad_lista()
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
        
        elif menu_select==4:
            
            clasifica()
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
        
        elif menu_select==5:
            
            mejor_jugador() 
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

        elif menu_select==6:
            
            menor_jugador()
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

        elif menu_select==7:
            
            promedio_divisiones()
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

        elif menu_select==8:
            
            consulta_liga()
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

        elif menu_select==9:

            promedio_todos()
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

        elif menu_select==10:

            cant_jugadores()       
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
        
        elif menu_select==11:

            num_jugadores()
            input("PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

        elif menu_select == 12:

            print("\n"," (:  GRACIAS POR JUGAR  :)", "\n")
            
            ans = False

def bienvenida():

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
########################FIN DE LAS FUNCIONES##################

bienvenida()
menu()


       