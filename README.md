# Reto_6
***
Hecho por Lucas García
## Punto 1
```
import math

def Volumen (r1: float, r2: float, h: float) -> float:
    volumen = ((4*math.pi * r1**3)/3) + ((math.pi * r2**2 * h)/3)
    return volumen

def Area_superficial (r1: float, r2: float, h: float) -> float:
    h_inclinada = (r2**2 + h **2)**0.5
    area_superf = (4*math.pi * r1**2) + (math.pi * r2**2 + math.pi * r2 * h_inclinada)
    return area_superf

if __name__ == "__main__":

    volumen_total: float
    area_superficial: float
    
    print("Por favor utilice datos en centímetros")
    r1 = float(input("Ingrese radio de la esfera: "))
    r2 = float(input("Ingrese radio del cono: "))
    h = float (input("Ingrese h del cono: "))

    volumen_total = Volumen(r1, r2, h)
    area_superficial = Area_superficial(r1, r2, h)

    print("De la figura mostrada el volumen es:", str(volumen_total),"cm^3")
    print("De la figura mostrada el área superficial es:", str(area_superficial),"cm^2")
```

## Punto 2
```
import math

def perimetro (r: float, b: float, a: float) -> float:
    perimetro = (b*2 + a*2) + (r * 2 * math.pi)*2
    return perimetro

def area (r: float, b: float, a: float) -> float:
    area = (b * a) + (math.pi * r**2)*2
    return area

if __name__ == "__main__":
    
    perimetro_figura: float
    area_figura: float

    print("Por favor utilice datos en centímetros")
    r = float(input("Ingrese el radio de las circunferencias: "))
    b = float(input("Ingrese la base del rectángulo: "))
    a = float(input("Ingrese la altura del rectágnulo"))

    perimetro_figura = perimetro(r,b,a)
    area_figura = area(r,b,a)

    print("De la figura mostrada el perimetro es:", str(perimetro_figura),"cm")
    print("De la figura mostrada el área es:", str(area_figura),"cm^2")
```

## Punto 3
```
def masa (N: int, M: int, K: int) -> int:
    cantidad_kilos = (N*6) + (M*7) + K
    return cantidad_kilos

if __name__ == "__main__":
    kilos: int
    print("Ingrese la cantidad de los siguientes animales que se tiene:")
    N = int(input("Gallinas:"))
    M = int(input("Gallos:"))
    K = int(input("Pollitos:"))

    kilos = masa(N,M,K)
    print("La cantidad de carne es de:", kilos,"kg")
```

## Punto 4
```
def cambio (P: int, M: int, H: int, B: int) -> float:
    residuo = B - (P*300 + M*3300 + H*350)
    return residuo

if __name__ == "__main__":
    restante: float
    print("Ingrese el número de unidades que comprará de:")
    P = int(input("Panes:"))
    M = int(input("Bolsas de leche:"))
    H = int(input("Huevos:"))
    B = int(input("Y de igual forma el billete usado (sin puntos)"))

    restante = cambio(P,M,H,B)
    if restante < 0:
        valor_absoluto = restante * -1
        print("Quedaste debiendo:", str(valor_absoluto), "pesos")
    else:
        print("Recibiste de vuelto:", str(restante), "pesos")
```

## Punto 5
```

```
