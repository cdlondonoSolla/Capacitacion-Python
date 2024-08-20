from menus import menu_principal, menu_administrador, menu_usuario
from funciones import *
from base_datos import lista_de_cuentas


while True:
    print(menu_principal)
    try:
        opcion_principal = int(input("Selecciona una opción: "))
    except:
        print("Seleccione una opción correcta")
        continue
    
    match opcion_principal:
        case 0:
            print("Aplicación finalizada")
            break
        case 1:
            while True:
                print(menu_administrador)
                try:
                    opcion_administrador = int(input("Selecciona una opción: "))
                except:
                    print("Seleccione una opción correcta")
                    continue
        
                match opcion_administrador:
                    case 0:
                        print("Aplicación finalizada")
                        break
                    case 1:
                        cuenta = crear_cuenta()
                        lista_de_cuentas.append(cuenta)
                        print("Cuenta creada correctamente")
                    case 2:
                        quitar_cuenta(lista_de_cuentas)
                    case 3:
                        modificar_cuenta(lista_de_cuentas)
                    case 4:
                        for cuenta in lista_de_cuentas:
                            imprimir_cuenta(cuenta=cuenta)
        case 2:
            while True:
                print(menu_usuario)
                try:
                    opcion_usuario = int(input("Selecciona una opción: "))
                except:
                    print("Seleccione una opción correcta")
                    continue
                
                match opcion_usuario:
                    case 0:
                        print("Aplicación finalizada")
                        break
                    case 1:
                        informacion_cuenta(lista_de_cuentas)