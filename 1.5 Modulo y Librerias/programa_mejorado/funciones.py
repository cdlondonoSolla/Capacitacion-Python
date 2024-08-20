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

def quitar_cuenta(lista_de_cuentas) -> None:
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

def modificar_cuenta(lista_de_cuentas) -> None:
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

def informacion_cuenta(lista_de_cuentas) -> None:
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