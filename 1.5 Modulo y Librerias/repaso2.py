def resta(a: int, b: int) -> int:
    return a - b


class Alimento:
    def __init__(self, nombre, gramos, calorias) -> None:
        self.nombre = nombre
        self.gramos = gramos
        self.calorias = calorias
        
    def __str__(self) -> str:
        return f"{self.nombre} {self.gramos} {self.calorias}"

class NutriCanSolla(Alimento):
    def __init__(self, nombre, gramos, calorias) -> None:
        super().__init__(nombre, gramos, calorias)
        self.stock = 7000
        self.precio = 20000
        
    def incrementar_stock(self, cant):
        self.stock = self.stock + cant
        
    def calcular_precio_dolares(self, cambio):
        return self.precio / cambio
        
nutri_can = NutriCanSolla(
    nombre="Nutri Can Solla",
    gramos=250,
    calorias=80,
)

precio_nutri_can_usd = nutri_can.calcular_precio_dolares(4100)




  
jamonada_ds = Alimento(
    nombre="Jamonada DS",
    gramos=250,
    calorias=100
)


lista_de_productos_solla = ["NutreCan Senior", "Quida Cat", "Solla leche", "Maná", "Conejos"]

productos_solla = [{"producto": producto} for producto in lista_de_productos_solla]

productos_solla_2 = []

for producto in lista_de_productos_solla:
    dicc = {"producto": producto}
    productos_solla_2.append(dicc)

print(round(precio_nutri_can_usd, ndigits=4))
print(f"{precio_nutri_can_usd:.3f}")