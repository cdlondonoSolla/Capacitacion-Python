# Validación de estados de cuentas

def crear_cuenta() -> dict:
    """Crea una cuenta y la retorna"""
    nro = input("Nro de cuenta: ")
    username = input("Username: ")
    nombre_completo = input("Nombre completo: ")
    correo = input("Correo: ")
    ping = input("Ping: ")
    
    cuenta = {
        "Nro": nro,
        "esta_activa": True,
        "username": username,
        "nombre_completo": nombre_completo,
        "correo": correo,
        "ping": ping,
        "fondos": "0 COP"
    }
    return cuenta

def quitar_cuenta() -> None:
    """Quita una cuenta de la lista"""
    contador = 1
    for cuenta in lista_de_cuentas:
        print(f"{contador} - {cuenta["correo"]}")
        contador += 1
        
    index = int(input("¿Cual cuenta desea quitar?: ")) - 1
    lista_de_cuentas.pop(index)
    print("Cuenta eliminada")
    
def imprimir_cuenta(cuenta: dict) -> None:
    print(
        f"""
        Nro. Cuenta: {cuenta["Nro"]}
        Nombre: {cuenta["nombre_completo"]}
        """
    )

def modificar_cuenta() -> None:
    """Modifica una cuenta"""
    contador = 1
    for cuenta in lista_de_cuentas:
        print(f"{contador} - {cuenta["correo"]}")
        contador += 1
        
    index = int(input("¿Cual cuenta desea modificar?: ")) - 1
    esta_activa = input("activa: ")
    nombre_completo = input("Nombre: ")
    correo = input("correo: ")
    
    if esta_activa:
        esta_activa = bool(esta_activa)
        lista_de_cuentas[index]["esta_activa"] = esta_activa
    if nombre_completo:
        lista_de_cuentas[index]["nombre_completo"] = nombre_completo
    if correo:
        lista_de_cuentas[index]["correo"] = correo
    
    print("Cuenta modificada")

def informacion_cuenta() -> None:
    usuario = input("Por favor, introduce tu usuario: ")
    ping = input("Por favor, introduce tu ping: ")
    
    cuenta = [cuenta for cuenta in lista_de_cuentas if cuenta["username"] == usuario]
    cuenta = cuenta[0]
    if cuenta and cuenta["esta_activa"] and cuenta["ping"] == ping:
        print(f"""
            USERNAME: {cuenta.get("username")}
            NOMBRE COMPLETO: {cuenta.get("nombre_completo")}
            CORREO: {cuenta.get("correo")}
            CUENTA NRO: {cuenta.get("Nro")}
            FONDOS: {cuenta.get("fondos")}
        """)
    elif not cuenta["esta_activa"]:
        print("Cuenta inactiva, contacte a soporte")
    else:
        print("El usuario no existe o constraseña incorrecta")
        
lista_de_cuentas = [
    {
        "Nro": "012-0000145-874",
        "esta_activa": True,
        "username": "fabiovelez00",
        "nombre_completo": "FABIO ALEXANDER VELEZ",
        "correo": "fabio@mail.com",
        "ping": "1238",
        "fondos": "6.000.000 COP"
    },
    {
        "Nro": "012-0000145-874",
        "esta_activa": False,
        "username": "lorenamarquez00",
        "nombre_completo": "LORENA PATRICIA MARQUEZ",
        "correo": "lorena@mail.com",
        "ping": "3398",
        "fondos": "0 COP"
    },
    {
        "Nro": "012-0000145-877",
        "esta_activa": True,
        "username": "pedroyepez",
        "nombre_completo": "PEDRO MAURICIO YEPEZ",
        "correo": "pedro@mail.com",
        "ping": "4157",
        "fondos": "7.001.500 COP"
    },
    {
        "Nro": "013-0000145-874",
        "esta_activa": True,
        "username": "anarodriguez14",
        "nombre_completo": "ANA LUCIA RODRIGUEZ",
        "correo": "ana@mail.com",
        "ping": "8741",
        "fondos": "640.000 COP"
    }
]

encontrado = False

menu_principal = """
1 - Ingresar como administrador
2 - Ingresar como usuario
0 - Salir
"""

menu_administrador = """
1 - Agregar cuenta
2 - Quitar cuenta
3 - Moodificar cuenta
4 - Listar cuentas
0 - Salir
"""

menu_usuario = """
1 - Ver información de cuenta
0 - Salir
"""

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
                        quitar_cuenta()
                    case 3:
                        modificar_cuenta()
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
                        informacion_cuenta()
            