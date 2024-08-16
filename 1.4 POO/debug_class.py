class Coche:
    def __init__(self, modelo, puertas, color, motor, traccion, transmision, vel_max, velocidades):  
        self.modelo = modelo
        self.puertas = puertas
        self.color = color
        self.motor = motor
        self.traccion = traccion
        self.transmision = transmision
        self.vel_maxima = vel_max
        self.encendido = False
        self.velocidades = velocidades
        
    def __str__(self):
        return f"""
        modelo: {self.modelo}
        puertas: {self.puertas}
        color: {self.color}
        motor: {self.motor}
        traccion: {self.traccion}
        transmision: {self.transmision}
    """
    
    def acelerar(self):
        aceleracion = 0
        intervalo_cambio = 0
        match self.motor:
            case "1.4L":
                aceleracion = 6
                intervalo_cambio = 35
            case "1.6L":
                aceleracion = 11
                intervalo_cambio = 40
                
        aceleracion_total = 0
        velocidad_actual = 0
        
        for velocidad in range(1, self.velocidades + 1):
            print(f"cambio {velocidad}")
            while aceleracion_total < self.vel_maxima:
                print(f"{aceleracion_total} Km/h")
                aceleracion_total += aceleracion
                
                if aceleracion_total >= velocidad_actual + intervalo_cambio:
                    velocidad_actual = aceleracion_total
                    break
                
        
        print("Alcanzó la velocidad máxima")
    
    def encender(self):
        self.encendido = True
        
    def apagar(self):
        self.encendido = False
        
toyota_corolla = Coche(
    modelo="Toyota Corolla", 
    puertas=4, 
    color="Amarillo", 
    motor="1.6L", 
    traccion="4x2", 
    transmision="automático",
    vel_max=210,
    velocidades=6
)

chev_aveo = Coche(
    modelo="Chevrolet Aveo", 
    puertas=4, 
    color="Negro", 
    motor="1.4L",
    traccion="4x2", 
    transmision="automático",
    vel_max=160,
    velocidades=5
)

chev_aveo.acelerar()