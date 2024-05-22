from grafico import seleccionar_color, calcular_figura, seleccionar_figura



def inicio_programa():
    print("Bienvenido al Menú de Figuras Geométricas")
    figura = None
    while True:
        print("\nOpciones:")
        print("1. Seleccionar figura y cargar valores")
        print("2. Visualizar resultados")
        print("3. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            figura = seleccionar_figura()
            figura["color"] = seleccionar_color()
        elif opcion == "2":
            if figura:
                calcular_figura(figura)
            else:
                print("Primero seleccione una figura y cargue los valores.")
        elif opcion == "3":
            print("Adios")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    inicio_programa()