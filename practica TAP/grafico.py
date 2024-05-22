import pygame
from funciones import *

def seleccionar_color():
    diccionario_colores = {"azul": (0, 0, 255), "verde": (0, 255, 0), "amarillo": (255, 255, 0)}
    print("Seleccione un color:")
    for key in diccionario_colores:
        print(key)
    opcion = input("Ingrese el nombre del color deseado: ")
    return diccionario_colores.get(opcion, (0, 0, 255))

def calcular_figura(figura):
    pygame.init()
    ANCHO, ALTO = 800, 600
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Figuras Geométricas")
    fuente = pygame.font.Font(None, 30)
    
    ventana.fill((255, 255, 255))
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        if figura["tipo"] == "rectángulo":
            base, altura = figura["dimensiones"]
            area = calcular_area_rectangulo(base, altura)
            perimetro = calcular_perimetro_rectangulo(base, altura)
            pygame.draw.rect(ventana, pygame.Color(figura["color"]), (50, 50, base, altura))
            texto_area = fuente.render(f"Área: {area}", True, (0, 0, 0))
            texto_perimetro = fuente.render(f"Perímetro: {perimetro}", True, (0, 0, 0))
            ventana.blit(texto_area, (50, 50 + altura + 10))
            ventana.blit(texto_perimetro, (50, 50 + altura + 40))
        elif figura["tipo"] == "circulo":
            radio = figura["dimensiones"][0]
            area = calcular_area_circulo(radio)
            perimetro = calcular_perimetro_circulo(radio)
            pygame.draw.circle(ventana, pygame.Color(figura["color"]), (400, 300), radio)
            texto_area = fuente.render(f"Área: {area}", True, (0, 0, 0))
            texto_perimetro = fuente.render(f"Perímetro: {perimetro}", True, (0, 0, 0))
            ventana.blit(texto_area, (50, 50 + radio + 10))
            ventana.blit(texto_perimetro, (50, 50 + radio + 40))
        elif figura["tipo"] == "triangulo":
            base, altura = figura["dimensiones"]
            area = calcular_area_triangulo_rectangulo(base, altura)
            perimetro = calcular_perimetro_triangulo_rectangulo(base, altura)
            puntos = [(50, 50), (50 + base, 50), (50, 50 + altura)]
            pygame.draw.polygon(ventana, pygame.Color(figura["color"]), puntos)
            texto_area = fuente.render(f"Área: {area}", True, (0, 0, 0))
            texto_perimetro = fuente.render(f"Perímetro: {perimetro}", True, (0, 0, 0))
            ventana.blit(texto_area, (50, 50 + altura + 10))
            ventana.blit(texto_perimetro, (50, 50 + altura + 40))
        else:
            print("Figura no reconocida")
        
        pygame.display.update()
        break

def seleccionar_figura():
    print("Seleccione una figura:")
    print("1. Rectángulo")
    print("2. Círculo")
    print("3. Triángulo")
    opcion = input("Ingrese el número de la figura deseada: ")

    if opcion == "1":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        return {"tipo": "rectángulo", "dimensiones": (base, altura)}
    elif opcion == "2":
        radio = float(input("Ingrese el radio del círculo: "))
        return {"tipo": "circulo", "dimensiones": (radio,)}
    elif opcion == "3":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        return {"tipo": "triangulo", "dimensiones": (base, altura)}
    else:
        print("Opción inválida. Selecciona una figura válida.")
        return seleccionar_figura()