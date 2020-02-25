#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#IMPORTAMOS LA LIBRERIA OS QUE PERMITIRA USAR ALGUNAS FUNCIONES DEL SISTEMA (WINDOWS)
import os

def credenciales(): #CREAMOS UNA FUNCION LLAMADA CREDENCIALES QUE PERMITIRA EVALUAR SI LA CUENTA EXISTE DENTRO DEL SISTEMA
    print("""\t\t\t*******
            \t\t*LOGIN*
            \t\t*******""")# TITULO PARA EL USUARIO QUE SE LLAMARA LOGIN E INDICA QUE ES UN LOGIN
    user = input("\tDigite su Usuario -> ")# PIDE EL NOMBRE DE USUARIO
    password = int(input("\tDigite su Contraseña -> "))# PIDE CONTRASEÑA DEL USUARIO

    user1 = "armando" #INGRESAMOS UN USUARIO OJO PUEDE CAMBIAR POR EL QUE DESEE
    pass1 = 12345   # HACEMOS LO MISMO PARA LA CONTRASEÑA COMO EL USUARIO
    if user == user1 and password == pass1:# EVALUAMOS QUE LOS DATOS QUE EL USUARIO INGRESO COINCIDEN CON LOS QUE NOSOTROS DEFINIMOS
        os.system("cls") #HACEMOS USO DE LA FUNCION DEL SISTEMA CLEAR PARA BORRAR PANTALLA DE LA LIBRERIA OS IMPORTADA
        print("\t*******BIENVENIDO AL SISTEMA*******\n\n")# AL VALIDAR LA CUENTA LUEGO BORRRAMOS PANTALLA MOSTRAMOS UN MENSAJE DE BIENVENIDA
        os.system("pause")#FUNCION PAUSA DEL SISTEMA TRAIDA POR LA LIBRERIA OS
        os.system("cls")#FUNCION CLEAR DEL SISTEMA TRAIDA POR LA LIBRERIA OS
        menu()# LLAMAMOS A LA FUCION LLAMADA MENU
    else:#DE NO SER CORRRECTOS EL USUARIO Y CONTRASEÑA MOSTRAREMOS DATOS INVALIDOS
        os.system("cls")
        if user != user1:# SI EL DATO INGRESADO POR EL USUARIO ES DIFERENTE AL QUE DEFINIMOS MOSTRAREMOS LO SIGUIENTE
            print("Usuario Invalido")#MOSTRAMOS EN PANTALLA QUE ES INVALIDO EL USUARIO
        if password != pass1:# SI EL DATO INGRESADO POR EL USUARIO ES DIFERENTE AL QUE DEFINIMOS MOSTRAREMOS LO SIGUIENTE
            print("Contraseña Invalida")#MOSTRAMOS MEENSAJE QUE ES INVALIDO LA CONTRASEÑA
        os.system("pause")
        os.system("cls")
        credenciales()#HACEMOS LLAMADA A LA FUNCION CREDENCIALES



def menu():#CREAMOS UNA FUNCION LLAMADA MENU QUE SERA LA ENCARGADA DE MOSTRARNOS OPCIONES (SE PUEDE CAMBIAR POR EL QUE DESEE)
    print("\t\t\tMENU")#TITULO MENU
    print("""\n \t    1. SUMAR
            2. RESTAR
            3. MULTIPLICAR
            4. DIVIR
            5. CERRAR SESION
            6. SALIR""") #AQUI CREAMOS UN PEQUEÑO BANNER QUE MOSTRARA LAS OPCIONES DISPONIBLES
    opcion = int(input("Digite la opcion -> "))#PEDIMOS AL USUARIO QUE DIGITE ALGUNA OPCION DISPONIBLE
# ACONTINUACION CREAMOS UNOS IF Y ELIF COMO UN SWITCH PARA ESCOGER MULTIPLES OPCIONES DISPONIBLES
    if opcion == 1:#EVALUAMOS QUE EL DATO INGRESADO POR EL USUARIO SEA IGUAL AL VALOR DE 1 Y ARROJAREMOS LO SIGUIENTE
        pedirdatos1()#HACEMOS LLAMADA A LA FUNCION DENOMINADA PEDIRDATOS1
        os.system("pause")
        os.system("cls")
        menu()
    elif opcion == 2:#EVALUAMOS
        pedirdatos2()#LLAMAMOS A LA FUNCION PEDIRDATOS2
        os.system("pause")
        os.system("cls")
        menu()
    elif opcion == 3:
        pedirdatos3()
        os.system("pause")
        os.system("cls")
        menu()
    elif opcion == 4:
        pedirdatos4()
        os.system("pause")
        os.system("cls")
        menu()
    elif opcion == 5:
        os.system("cls")
        credenciales()#AQUI ALGO INTERESANTE ES QUE PODEMOS CERRAR SESION LA CUAL SOLO HAREMOS LA LLAMADA A LA FUNCION CREDENCIALES CREADA ANTERIORMENTE (SE PUEDE MEJORAR)
    elif opcion == 6:
        exit(0)#AQUI SIMPLEMENTE FINALIZAMO LA EJECUCION DEL PROGRAMA
    else:# EN CASO CONTRARIO DE INGRESAR UN VALOR NO DISPONIBLE LE INDICAMOS QUE DEBE CORREGIR
        os.system("cls")
        print("\nDigite un valor valido\n")
        input("PRESIONE ENTER PARA CONTINUAR")#EL INPUT NOS PERMITIRA PAUSAR EL PROGRAMA PARA QUE MUESTRE EL MENSAJE DE ERROR Y PUEDE PROSEGUIR AL DAR ENTER
        os.system("cls")
        menu()


"""CON LAS SIGUIENTES FUNCIONES CON 2 PARAMETROS HAREMOS POR SEPARADO LAS OPERACIOES ARITMETICAS A
LA QUE CORRESPONDA HACI RETORNANDO EL RESULTADO PARA NO SER (VALOR NONE)"""
def suma(y,x):
    resultado = y + x
    return resultado

def resta(y,x):
    resultado = y - x
    return resultado

def multiplicar(y,x):
    resultado = y * x
    return resultado

def dividir(y,x):
    resultado = y // x#OJO QUE AL DIVIDIR MOSTRAMOS RESULTADO SIN DECIMALES
    return resultado

def pedirdatos1():#FUNCION CREADA PARA PEDIR DATOS Y OPERARLAS
    os.system("cls")
    print("\t\t\t *** SUMA *** \n") #TITULO O BANNER DE SUMA
    num1 = int(input("Ingrese primer dato -> "))#PEDIMOS PRIMER DATO A SUMAR
    num2 = int(input("Ingrese segundo dato -> "))#PEDIMOS SEGUNDO DATO A SUMAR
    res = suma(num1, num2)#CREAMOS UNA VARIABLE LA CUAL LE METEREMOS LA FUNCION SUMA Y POCISIONAMOS LOS VALORS QUE EL USUARIO DIGITE EN LOS PARAMETROS
    print("EL resultado de la suma es -> ",res,"\n")

def pedirdatos2():
    os.system("cls")
    print("\t\t\t *** RESTA *** \n")
    num1 = int(input("Ingrese primer dato -> "))
    num2 = int(input("Ingrese segundo dato -> "))
    res = resta(num1, num2)
    print("EL resultado de la resta es -> ",res,"\n")

def pedirdatos3():
    os.system("cls")
    print("\t\t\t *** MULTIPLICACION *** \n")
    num1 = int(input("Ingrese primer dato -> "))
    num2 = int(input("Ingrese segundo dato -> "))
    res = multiplicar(num1, num2)
    print("EL resultado de la multiplicar es -> ",res)

def pedirdatos4():
    os.system("cls")
    print("\t\t\t *** DIVIDIR *** \n")
    num1 = int(input("Ingrese primer dato -> "))
    num2 = int(input("Ingrese segundo dato -> "))
    res = dividir(num1, num2)
    print("EL resultado de la division es -> ",res)

credenciales()# AQUI SIMPLEMENTE LLAMAMOS A LA FUNCION CREDENCIALES QUE NOS PERMITIRA EJECUTAR TODO LO HECHO ANTERIORMENTE
