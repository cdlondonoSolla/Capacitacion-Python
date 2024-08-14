# Empleado

nombre = "María"
apellido = "Romero"
cargo = "Analista de QA"
salario = "3.000.000 COP"
edad = "39 Años"
ciudad = "Bogotá"

#print(len(nombre))

dato_completo = nombre + " " + apellido + " " + cargo + " " + salario + " " + edad
dato_completo2 = f"{nombre} {apellido} {cargo} {salario} {edad} {ciudad}"
dato_completo3 = "%s %s %s %s %s %s" % (
    nombre, apellido, cargo, salario, edad, ciudad
)
dato_completo4 = "{} {} {} {} {} {}".format(
    nombre, apellido, cargo, salario, edad, ciudad
)

print(dato_completo)