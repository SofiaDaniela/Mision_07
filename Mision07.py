# Autor: Sofía Daniela Méndez Sandoval, AO1242259
# Descripción: Ciclos While

def main():

    print("\nMisión 07. Ciclos While: ")
    print("Autor: Sofía Daniela Méndez Sandoval")
    print("Matrícula: A01242259")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opc = int(input("¿Qué desea hacer? "))

    while opc >= 1 or opc <= 1:

        if opc == 1:

            dividendo = int(input("\n¿Cuál es el dividendo? "))
            divisor = int(input("¿Cuál es el divisor? "))

            dividir(dividendo, divisor)
            print("\nMisión 07. Ciclos While: ")
            print("Autor: Sofía Daniela Méndez Sandoval")
            print("Matrícula: A01242259")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")
            opc = int(input("¿Qué desea hacer? "))

        elif opc == 2:
            encuentraMayor()
            print("\nMisión 07. Ciclos While: ")
            print("Autor: Sofía Daniela Méndez Sandoval")
            print("Matrícula: A01242259")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")
            opc = int(input("¿Qué desea hacer? "))

        elif opc == 3:
            print("\nAdiós, gracias por usar este programa.")
            quit()

        else:

            print("\nERROR. Teclea 1, 2 o 3.")
            print("\nMisión 07. Ciclos While: ")
            print("Autor: Sofía Daniela Méndez Sandoval")
            print("Matrícula: A01242259")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")
            opc = int(input("¿Qué desea hacer? "))


def dividir(dividendo, divisor):

    nveces = 0
    sobra = dividendo

    while sobra >= divisor:
        valor = (sobra-divisor)
        sobra = valor
        nveces += 1

    print(dividendo, "/", divisor, "=", nveces, ", sobra ", sobra)


def encuentraMayor():

    nn = int(input("\nTeclea un número [-1 para salir]: "))
    ng = 0

    if nn == -1:
        print("\nNo hay valor mayor.")

    else:

        while nn != -1:

            if nn > ng:

                ng = nn
                nn = int(input("Teclea un número [-1 para salir]: "))

            else:

                nn = int(input("Teclea un número [-1 para salir]: "))


        print("\nEl número mayor es: ", ng)


main()