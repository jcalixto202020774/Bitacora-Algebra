#Calculadora de ecuaciones 2x2 y 3x3 por pasos
#Autor j.calixto@uniandes.edu.co

def ejecutar_2x2():
    evaluando = True
    x = "x"
    y = "y"

    print("\nSegún el siguiente formato:\nax + by = c")
    print("Escriba los digitos de la [primer] ecuación")
    a1 = float(input("a: "))
    b1 = float(input("b: "))
    c1 = float(input("c: "))

    print("Escriba los digitos de la [segunda] ecuación")
    a2 = float(input("a: "))
    b2 = float(input("b: "))
    c2 = float(input("c: "))

    print("El sistema está de la siguiente forma:\n")

    print(f" {a1}{x} {b1:+}{y} = {c1}")
    print(f" {a2}{x} {b2:+}{y} = {c2}")

    #Evaluar la pendiente para identificar si hay infinitas soluciones/ ninguna/ o una
    m1 = (a1*-1)/b1
    m2 = (a2*-1)/b2
    i1 = c1/b1
    i2 = c2/b2

    if m1 == m2 and i1 == i2:
        print("\nLas dos ecuaciones representan la misma recta, hay infinitas soluciones")
    elif m1 == m2:
        print("\nLas dos ecucaciones tienen la misma pendiente, nunca se interceptarán, no hay solución")
    else: 
        while evaluando == True:
            print("\n>> Con que método desea resolver la ecuación <<")
            print("> (1) Igualación <")
            print("> (2) Sustitución <")
            print("> (3) Eliminación <")
            print("> (0) Volver al menú")
            metodo = int(input(": "))
            if metodo == 1:
                igualacion(a1,b1,c1,a2,b2,c2)
            elif metodo == 2:
                sustitucion(a1,b1,c1,a2,b2,c2)
            elif metodo == 3:
                eliminacion(a1,b1,c1,a2,b2,c2)
            elif metodo == 0:
                evaluando = False
            else:
                print("Seleccione un método válido")

def igualacion(a1,b1,c1,a2,b2,c2):
    print("\n### IGUALACAION ###")
    x = "x"
    y = "y"

    #PASO 1, despejar la variable b1 y b2
    c1 /= b1
    a1 /= -b1
    b1 = 1

    c2 /= b2
    a2 /= -b2
    b2 = 1

    eq_c1 = c1
    eq_a1 = a1

    print("\n[PASO 1] en ambas ecuaciones se despeja y")
    print(f" {y} = {round(a1,2)}{x} {round(c1,2):+}")
    print(f" {y} = {round(a2,2)}{x} {round(c2,2):+}")

    #PASO 2, igualar las ecuaciones
    print("\n[PASO 2] se igualan ambas ecuaciones")
    print(f" {round(a1,2)}{x} {round(c1,2):+} = {round(a2,2)}{x} {round(c2,2):+}")

    #PASO 3, dejar las x a un lado
    a2 *= -1
    c1 *= -1
    print("\n[PASO 3] se dejan las x del lado izquierdo")
    print(f" {round(a1,2)}{x} {round(a2,2):+5}{x} = {round(c2,2)} {round(c1,2):+}")

    #PASO 4, sumar
    a1 += a2
    c2 += c1
    print("\n[PASO 4] se opera")
    print(f" {round(a1,2)}{x} = {round(c2,2)}")

    #PASO 5, despejar
    c2 /= a1
    eq_x = c2
    print("\n[PASO 5] se despeja la x")
    print(f" {x} = {round(c2,2)}")

    #PASO 6, reemplazar en ecuación
    print("\n[PASO 6] se reemplaza el x encontrado en la ecuacion 1")
    print(f" {y} ={round(eq_a1,2)} * ({round(eq_x,2)}) {round(eq_c1,2):+}")

    #PASO 7. evaluar
    eq_y = eq_a1*eq_x + eq_c1
    print("\n[PASO 7] se opera")
    print(f" {y} = {round(eq_y,2)}")

    print(f"\n Respuesta = ({round(eq_x,2)},{round(eq_y,2)})")

def sustitucion(a1,b1,c1,a2,b2,c2):
    print("\n### SUSTITUCION ###")
    x = "x"
    y = "y"

    #PASO 1, despejar x de ecuacion 1
    c1 /= a1
    b1 /= -a1
    a1 = 1
    eq_c1 = c1
    eq_b1 = b1
    print("\n[PASO 1] se despeja x de la ecuacion 1")
    print(f" {x} = {round(c1,2)} {round(b1,2):+}{y}")

    #PASO 2, reemplazar x en ecuacion 2
    print("\n[PASO 2] se reemplaza x en la ecuacion 2")
    print(f" {a2} * ({round(c1,2)} {round(b1,2):+}{y}) {b2:+}{y} = {c2}")

    #PASO 3, distribuir en el parentesis
    c1 *= a2
    b1 *= a2
    print("\n[PASO 3] se distribuye en el parentesis")
    print(f"{round(c1,2)} {round(b1,2):+}{y} {b2:+}{y} = {c2}")

    #PASO 4, juntar terminos semenjantes
    c1 *= -1
    print("\n[PASO 4] se dejan las y del lado izquierdo")
    print(f" {round(b1,2)}{y} {b2:+}{y} = {c2}  {round(c1,2):+}")

    #PASO 5, sumar
    b1 += b2
    c2 += c1
    print("\n[PASO 5] se opera")
    print(f" {round(b1,2)}{y} = {c2}")

    #PASO 6, despejar
    c2 /= b1
    eq_y = c2
    print("\n[PASO 6] se despeja y")
    print(f" {y} = {round(eq_y,2)}")

    #PASO 7, reemplazar en ecuacion de x despejada
    print("\n[PASO 7] se reemplaza el y encontrado en la ecuacion 1")
    print(f" {x} = {round(eq_c1,2)} {round(eq_b1,2):+} * ({round(eq_y,2)})")

    #PASO 8, evaluar
    eq_x = eq_c1 + (eq_b1*eq_y)
    print("\n[PASO 8] se opera")
    print(f" {x} = {round(eq_x,2)}")

    print(f"\n Respuesta = ({round(eq_x,2)},{round(eq_y,2)})")

def eliminacion(a1,b1,c1,a2,b2,c2):
    print("\n### ELIMINACION ###")
    x = "x"
    y = "y"
    eq_a1 = a1
    eq_b1 = b1
    eq_c1 = c1

    #PASO 1, Hallar el coeficiente que al multiplicar resta las x
    co = -(a1/a2)
    print("\n[PASO 1] se halla el coeficiente que al multiplicar en la ecuacion 2 cancela las x")
    print(f" {a1}/{a2} => {co}")
    print(f" {round(a1,2)}{x} {round(b1,2):+}{y} = {round(c1,2)}")
    print(f" {round(co,2)} * ({round(a2,2)}{x} {round(b2,2):+}{y} = {round(c2,2)})")

    #PASO 2, Multiplicar el coeficiente por la ecuacion 2 
    a2 *= co
    b2 *= co
    c2 *= co
    print("\n[PASO 2] se multiplica el coeficiente por la ecuacion 2")
    print(f" {round(a1,2)}{x} {round(b1,2):+}{y} = {round(c1,2)}")
    print(f" {round(a2,2)}{x} {round(c2,2):+}{y} = {round(c2,2)}")

    #PASO 3, Sumar
    a1 = 0
    b1 += b2
    c1 += c2
    print("\n[PASO 3] se suman las ecuaciones")
    print(f" {round(b1,2)}{y} = {round(c1,2)}")

    #PASO 4, Despejar
    c1 /= b1
    eq_y = c1
    print("\n[PASO 4] se despeja y")
    print(f" {y} = {round(eq_y,2)}")

    #PASO 5, Reemplazar en ecuacion 1
    print("\n[PASO 5] se reeemplaza el y encontrado en la ecuacion 1")
    print(f" {round(eq_a1,2)}{x} {round(eq_b1,2):+} * ({round(eq_y,2)}) = {eq_c1}")

    #PASO 6, Evaluar y despejar
    eq_b1 *= eq_y
    eq_c1 += -(eq_b1)
    print("\n[PASO 6] se opera")
    print(f" {round(eq_a1,2)}{x} = {round(eq_c1,2)}")

    #PASO 7, Despejar
    eq_c1 /= eq_a1
    eq_x = eq_c1
    print("\n[PASO 7] se despeja x")
    print(f" {x} = {round(eq_x,2)}")

    print(f"\n Respuesta = ({round(eq_x,2)},{round(eq_y,2)})")

def ejecutar_3x3():
    x = "x"
    y = "y"
    z = "z"

    print("\nSegún el siguiente formato:\nax + by + cz= d")
    print("Escriba los digitos de la [primer] ecuación")
    a1 = float(input("a: "))
    b1 = float(input("b: "))
    c1 = float(input("c: "))
    d1 = float(input("d: "))

    print("Escriba los digitos de la [segunda] ecuación")
    a2 = float(input("a: "))
    b2 = float(input("b: "))
    c2 = float(input("c: "))
    d2 = float(input("d: "))

    print("Escriba los digitos de la [tercera] ecuación")
    a3 = float(input("a: "))
    b3 = float(input("b: "))
    c3 = float(input("c: "))
    d3 = float(input("d: "))

    print("El sistema está de la siguiente forma:\n")

    print(f" {a1}{x} {b1:+}{y} {c1:+}{z} = {d1}")
    print(f" {a2}{x} {b2:+}{y} {c2:+}{z} = {d2}")
    print(f" {a3}{x} {b3:+}{y} {c3:+}{z} = {d3}")

    print("\n### GAUSS-JORDAN ###")
    #PASO 1, crear una matriz aumentada
    print("\n[PASO 1] se crea una matriz aumentada")
    print(f"\t{a1}\t{b1}\t{c1}\t| {d1}")
    print(f"\t{a2}\t{b2}\t{c2}\t| {d2}")
    print(f"\t{a3}\t{b3}\t{c3}\t| {d3}")

    #PASO 2, dividir la ecuacion 1 sobre el coeficiente de x para dejarlo igual a 1
    # 1   b1  c1 | d1
    # a2  b2  c2 | d2
    # a3  b3  c3 | d3
    print("\n[PASO 2] se divide sobre el coeficiente de x en la primera ecuacion para dejarlo igual a 1")
    b1 /= a1
    c1 /= a1
    d1 /= a1
    a1 /= a1
    print(f"\t{a1}\t{b1}\t{round(c1,2)}\t| {d1}")
    print(f"\t{a2}\t{b2}\t{round(c2,2)}\t| {d2}")
    print(f"\t{a3}\t{b3}\t{round(c3,2)}\t| {d3}")

    #PASO 3, eliminar terminos de x en la ecuacion 2 y 3
    # 1   b1  c1 | d1
    # 0   b2  c2 | d2
    # 0   b3  c3 | d3
    print("\n[PASO 3] se eliminan las x restandoles su coeficiente multiplicado por la ecuacion 1")
    print(f"\t{a1}\t{b1}\t{round(c1,2)}\t| {d1}")
    print(f"\t{a3} - {a3}({round(a1,2)})\t{b3} - {a3}({b1})\t{c3} - {a3}({round(c1,2)})\t| {d3} - {a3}({round(c1,2)})")
    print(f"\t{a2} - {a2}({round(a1,2)})\t{b2} - {a2}({b1})\t{c2} - {a2}({round(c1,2)})\t| {d2} - {a2}({round(c1,2)})")

    b2 -= a2*b1
    c2 -= a2*c1
    d2 -= a2*d1
    a2 -= a2*a1

    b3 -= a3*b1
    c3 -= a3*c1
    d3 -= a3*d1
    a3 -= a3*a1

    print(f"\n\t{a1}\t{b1}\t{round(c1,2)}\t| {d1}")
    print(f"\t{a2}\t{b2}\t{round(c2,2)}\t| {d2}")
    print(f"\t{a3}\t{b3}\t{round(c3,2)}\t| {d3}")

    #PASO 4, dividir la ecuacion 2 sobre el coeficiente de y para dejarlo igual a 1
    # 1   b1  c1 | d1
    # 0   1   c2 | d2
    # 0   b3  c3 | d3
    print("\n[PASO 4] se divide sobre el coeficiente de y en la segunda ecuacion")
    a2 /= b2
    c2 /= b2
    d2 /= b2
    b2 /= b2
    print(f"\t{round(a1,2)}\t{round(b1,2)}\t{round(c1,2)}\t| {round(d1,2)}")
    print(f"\t{round(a2,2)}\t{round(b2,2)}\t{round(c2,2)}\t| {round(d2,2)}")
    print(f"\t{round(a3,2)}\t{round(b3,2)}\t{round(c3,2)}\t| {round(d3,2)}")

    #PASO 5, eliminar terminos de y en la ecuacion 1 y 3
    # 1   0   c1 | d1
    # 0   1   c2 | d2
    # 0   0   c3 | d3
    print("\n[PASO 5] parecido al PASO 3 se eliminan las y restandoles su coeficiente multiplicado por la ecuacion 2")
    print(f"\t{a1} - {b1}({a2})\t{b1} - {b1}({b2})\t{round(c1,2)} - {b1}({round(c1,2)})\t| {d1} - {a2}({round(c2,2)})")
    print(f"\t{a2}\t{b2}\t{c2}\t| {round(d2,2)}")
    print(f"\t{a3} - {a3}({a2})\t{b3} - {a3}({b2})\t{round(c3,2)} - {a3}({round(c1,2)})\t| {d3} - {a3}({round(c2,2)})")

    a1 -= b1*a2
    c1 -= b1*c2
    d1 -= b1*d2
    b1 -= b1*b2

    a3 -= b3*a2
    c3 -= b3*c2
    d3 -= b3*d2
    b3 -= b3*b2
    
    print(f"\n\t{a1}\t{b1}\t{round(c1,2)}\t| {round(d1,2)}")
    print(f"\t{a2}\t{b2}\t{round(c2,2)}\t| {round(d2,2)}")
    print(f"\t{a3}\t{b3}\t{round(c3,2)}\t| {round(d3,2)}")

    #PASO 6, dividir la ecuacion 3 sobre el coeficiente de z para dejarlo igual a 1
    # 1   0   c1 | d1
    # 0   1   c2 | d2
    # 0   0   1  | d3
    print("\n[PASO 6] se divide sobre el coeficiente de z en la tercera ecuacion")
    a3 /= c3
    b3 /= c3
    d3 /= c3
    c3 /= c3
    print(f"\t{a1}\t{b1}\t{round(c1,2)}\t| {round(d1,2)}")
    print(f"\t{a2}\t{b2}\t{round(c2,2)}\t| {round(d2,2)}")
    print(f"\t{a3}\t{b3}\t{round(c3,2)}\t| {round(d3,2)}")

    #PASO 7, eliminar los terminos de z en la ecuacion 1 y 2
    # 1   0   0 | d1
    # 0   1   0 | d2
    # 0   0   1 | d3
    print("\n[PASO 7] parecido al PASO 3 se eliminan las z restandoles su coeficiente multiplicado por la ecuacion 3")
    print(f"\t{a1} - {round(c1,2)}({a3})\t{b1} - {round(c1,2)}({round(b3,2)})\t{round(c1,2)} - {round(c1,3)}({c3})\t| {round(d1,2)} - {round(c1,2)}({round(d3,2)})")
    print(f"\t{a2} - {round(c2,2)}({a3})\t{b2} - {round(c2,2)}({round(b3,2)})\t{round(c2,2)} - {round(c2,3)}({c3})\t| {round(d2,2)} - {round(c2,2)}({round(d3,2)})")
    print(f"\t{a3}\t{b3}\t{c3}\t| {round(d3,2)}")

    a1 -= c1*a3
    b1 -= c1*b3
    d1 -= c1*d3
    c1 -= c1*c3

    a2 -= c2*a3
    b2 -= c2*b3
    d2 -= c2*d3
    c2 -= c2*c3

    print(f"\n\t{a1}\t{b1}\t{round(c1,2)}\t| {round(d1,2)}")
    print(f"\t{a2}\t{b2}\t{round(c2,2)}\t| {round(d2,2)}")
    print(f"\t{a3}\t{b3}\t{round(c3,2)}\t| {round(d3,2)}")

    #PASO 8, mirar si estan en 0 y dar respuesta
    if (a1 == 1 and b1 == 0 and c1 == 0):
        if (a2 == 0 and b2 == 1 and c2 == 0):
            if (a3 == 0 and b3 == 0 and c3 == 1):
                print(f"\nRespuesta: ({round(d1,2)},{round(d2,2)},{round(d3,2)})")
        elif (a2 == 0 and b2 == 1 and c2 != 0):
            if (a3 == 0 and b3 == 0 and c3 == 1):
                c2 *= d3
                d2 += -(c2)
                print(f"\nRespuesta: ({round(d1,2)},{round(d2,2)},{round(d3,2)})")

def mostrar_menu():
    print("\n>>> Este es un programa para resolver ecuaciones lineales 2x2 o 3x3 <<<")
    print(">> Escriba el número de la opción que desea ejecutar <<")
    print("> (1) Integrantes del grupo <")
    print("> (2) Ecuaciones 2x2 <")
    print("> (3) Ecuaciones 3x3 <")
    print("> (0) Finalizar programa <")

def mostrar_nombres():
    print("(*) Juan Diego Calixto 202020774")
    print("(*) Diego Fernando Ramirez 202116746")
    print("(*) Juan Felipe Olarte 201923605")
    print("(*) Angie Urresty 202014884")
    print("(*) Sebastian Acosta 201921752")
    print("(*) Ronald Andres 201914873")

def iniciar_aplicacion():
    #Ejecuta el programa para el usuario
    continuar = True
    while continuar == True:
        mostrar_menu()
        opcion = int(input(": "))
        if opcion == 1:
            mostrar_nombres()
        elif opcion == 2:
            ejecutar_2x2()
        elif opcion == 3:
            ejecutar_3x3()
        elif opcion == 0:
            continuar = False
        else:
            print("Por favor seleccionar una opció3n valida")

iniciar_aplicacion()