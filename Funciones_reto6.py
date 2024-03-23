def promedio (a: float, b: float, c: float, d: float, e: float) -> float:
    media = (a + b + c + d + e) / 5
    return media

def mediana (a: float, b: float, c: float, d: float, e: float) -> float:
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if a > d:
        a, d = d, a
    if a > e:
        a, e = e, a
    if b > c:
        b, c = c, b
    if b > d:
        b, d = d, b
    if b > e:
        b, e = e, b
    if c > d:
        c, d = d, c
    if c > e:
        c, e = e, c
    if d > e:
        d, e = e, d
    return c

def prom_multi (a: float, b: float, c: float, d: float, e: float) -> float:
    multiplicacion = a * b * c * d * e
    promedio_multiplicativo = multiplicacion**(1/5)
    return promedio_multiplicativo
 
def ascender (a: float, b: float, c: float, d: float, e: float) -> float:
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if a > d:
        a, d = d, a
    if a > e:
        a, e = e, a
    if b > c:
        b, c = c, b
    if b > d:
        b, d = d, b
    if b > e:
        b, e = e, b
    if c > d:
        c, d = d, c
    if c > e:
        c, e = e, c
    if d > e:
        d, e = e, d
    arriba = a,b,c,d,e
    return arriba

def descender (a: float, b: float, c: float, d: float, e: float) -> float:
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if a > d:
        a, d = d, a
    if a > e:
        a, e = e, a
    if b > c:
        b, c = c, b
    if b > d:
        b, d = d, b
    if b > e:
        b, e = e, b
    if c > d:
        c, d = d, c
    if c > e:
        c, e = e, c
    if d > e:
        d, e = e, d
    abajo = e,d,c,b,a
    return abajo

def potencia (a: float, b: float, c: float, d: float, e: float) -> float:
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if a > d:
        a, d = d, a
    if a > e:
        a, e = e, a
    if b > c:
        b, c = c, b
    if b > d:
        b, d = d, b
    if b > e:
        b, e = e, b
    if c > d:
        c, d = d, c
    if c > e:
        c, e = e, c
    if d > e:
        d, e = e, d
    gran_potencia = e**a
    return gran_potencia

def root (a: float, b: float, c: float, d: float, e: float) -> float:
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if a > d:
        a, d = d, a
    if a > e:
        a, e = e, a
    if b > c:
        b, c = c, b
    if b > d:
        b, d = d, b
    if b > e:
        b, e = e, b
    if c > d:
        c, d = d, c
    if c > e:
        c, e = e, c
    if d > e:
        d, e = e, d
    cubo_r = a**(1/3)
    return cubo_r

