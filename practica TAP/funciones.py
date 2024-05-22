def calcular_area_rectangulo(base, altura):
    try:
        area = base * altura
        return area
    except ValueError:
        print("Error, ingrese solo números")

def calcular_perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def calcular_area_circulo(radio):
    pi = 3.1416
    try:
        area = pi * (radio ** 2)
        return area
    except ValueError:
        print("Ingrese solo números")

def calcular_perimetro_circulo(radio):
    pi = 3.1416
    return 2 * pi * radio

def calcular_area_triangulo_rectangulo(base, altura):
    try:
        area = (base * altura) / 2
        return area
    except ValueError:
        print("Error, ingrese solo números")

def calcular_perimetro_triangulo_rectangulo(base, altura):
    return base + altura + (base ** 2 + altura ** 2) ** 0.5

