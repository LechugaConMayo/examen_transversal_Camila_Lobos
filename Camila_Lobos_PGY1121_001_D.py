import datetime

entradas_platinum = [True] * 20
entradas_gold = [True] * 30
entradas_silver = [True] * 50
lista_asistentes = []
ganancias_platinum = 0
ganancias_gold = 0
ganancias_silver = 0

def validar_run(run):
    if len(run) == 9 and run[:-2].isdigit() and run[-1].isdigit() or run[-2].upper == "K":
        return True
    return False

def comprar_entradas():
    global entradas_platinum, entradas_gold, entradas_silver, lista_asistentes, ganancias_platinum, ganancias_gold, ganancias_silver
    
    cantidad = int(input("Ingrese la cantidad de entradas que va a comprar (entre 1 y 3): "))
    if cantidad < 1 or cantidad > 3:
        print("Cantidad inválida")
        return
    
    def mostrar_ubicaciones_disponibles():
        print("Estado actual de la venta de entradas:")
        print("*******ESCENARIO*******")
    
    for i in range(0, 20, 10):
        print(f"Platinum: {' '.join(['X' if not entradas_platinum[j] else str(j + 1) for j in range(i, i + 10)])}")
    
    for i in range(0, 30, 10):
        print(f"Gold: {' '.join(['X' if not entradas_gold[j] else str(j + 21) for j in range(i, i + 10)])}")
    
    for i in range(0, 50, 10):
        print(f"Silver: {' '.join(['X' if not entradas_silver[j] else str(j + 51) for j in range(i, i + 10)])}")
    
    total = 0
    for _ in range(cantidad):
        ubicacion = int(input("Ingrese la ubicación: "))
        
        if ubicacion < 1 or ubicacion > 100:
            print("Ubicación inválida")
            return
        
        if ubicacion <= 20:
            if not entradas_platinum[ubicacion - 1]:
                print("Ubicación no está disponible")
                return
            entradas_platinum[ubicacion - 1] = False
            total += 120000
        elif ubicacion <= 50:
            if not entradas_gold[ubicacion - 21]:
                print("Ubicación no está disponible")
                return
            entradas_gold[ubicacion - 21] = False
            total += 80000
        else:
            if not entradas_silver[ubicacion - 51]:
                print("Ubicación no está disponible")
                return
            entradas_silver[ubicacion - 51] = False
            total += 50000
    
    run = input("Ingrese el RUN del asistente: ")
    if not validar_run(run):
        print("RUN inválido")
        return
    
    lista_asistentes.append((run, total))
    if ubicacion <= 20:
        ganancias_platinum += total
    elif ubicacion <= 50:
        ganancias_gold += total
    else:
        ganancias_silver += total
    
    print("La operación se realizó correctamente")

def mostrar_ubicaciones_disponibles():
    print("Estado actual de la venta de entradas:")
    print("***ESCENARIO***")
    print(f"Platinum: {', '.join([str(i + 1) for i in range(20) if entradas_platinum[i]])}")
    print(f"Gold: {', '.join([str(i + 21) for i in range(30) if entradas_gold[i]])}")
    print(f"Silver: {', '.join([str(i + 51) for i in range(50) if entradas_silver[i]])}")

def mostrar_listado_asistentes():
    lista_asistentes.sort(key=lambda x: x[0])
    print("Listado de asistentes:")
    for asistente in lista_asistentes:
        print(asistente[0])

def mostrar_ganancias_totales():
    print("Ganancias totales:")
    print("Tipo Entrada | Cantidad  | Total")
    print(f"Platinum     | {entradas_platinum.count(False)}         | {ganancias_platinum}")
    print(f"Gold         | {entradas_gold.count(False)}         | {ganancias_gold}")
    print(f"Silver       | {entradas_silver.count(False)}         | {ganancias_silver}")
    print(f"TOTAL        | {entradas_platinum.count(False) + entradas_gold.count(False) + entradas_silver.count(False)}         | {ganancias_platinum + ganancias_gold + ganancias_silver}")

def salir():
    fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Gracias por utilizar la aplicación Creativos")
    print(f"Fecha y hora: {fecha_actual}")
    print("¡Nos vemos pronto!")

def main():
    while True:
        print("MENÚ")
        print("1. Comprar entradas")
        print("2. Mostrar ubicaciones disponibles")
        print("3. Ver listado de asistentes")
        print("4. Mostrar ganancias totales")
        print("5. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            comprar_entradas()
        elif opcion == "2":
            mostrar_ubicaciones_disponibles()
        elif opcion == "3":
            mostrar_listado_asistentes()
        elif opcion == "4":
            mostrar_ganancias_totales()
        elif opcion == "5":
            salir()
            break
        else:
            print("Opción inválida")

main()