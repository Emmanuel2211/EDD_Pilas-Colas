from picola_pkg.pila import Pila
from picola_pkg.cola import Cola


def main():
    print("=" * 50)
    print("  SISTEMA INTERACTIVO DE PILAS Y COLAS (PiCola)  ")
    print("=" * 50)

    while True:
        print("\nSeleccione la estructura de datos que desea utilizar:")
        print("1. Pila (LIFO)")
        print("2. Cola (FIFO)")
        print("3. Salir del programa")

        opcion_est = input("Opción: ").strip()
        if opcion_est == "3":
            print("\nFinalizando la ejecución. ¡Hasta luego!")
            break
        elif opcion_est not in ["1", "2"]:
            print("Opción inválida. Intente de nuevo.")
            continue

        print("\nSeleccione el tipo de datos que almacenará la estructura:")
        print("1. Enteros (int)")
        print("2. Cadenas de texto (str)")

        opcion_tipo = input("Opción: ").strip()
        if opcion_tipo not in ["1", "2"]:
            print("Opción inválida. Intente de nuevo.")
            continue

        # Inicialización genérica basada en la decisión del usuario
        tipo_dato = int if opcion_tipo == "1" else str
        nombre_estructura = "Pila" if opcion_est == "1" else "Cola"

        if opcion_est == "1":
            estructura = Pila[tipo_dato]()
        else:
            estructura = Cola[tipo_dato]()

        print(
            f"\n--- Se ha inicializado una {nombre_estructura} de tipo {tipo_dato.__name__} ---"
        )

        while True:
            print(f"\nOperaciones disponibles para {nombre_estructura}:")
            print("1. meter(elemento)")
            print("2. sacar()")
            print("3. mira()")
            print("4. esta_vacia()")
            print("5. devolver_tamanio()")
            print("6. Atrás (Cambiar de estructura o Salir)")

            operacion = input("Seleccione una operación a realizar: ").strip()

            if operacion == "6":
                break

            try:
                if operacion == "1":
                    valor = input(
                        f"Ingrese el elemento a meter (tipo {tipo_dato.__name__}): "
                    )
                    valor_casteado = tipo_dato(valor)
                    estructura.meter(valor_casteado)
                    print(f"\nResultado: Se insertó '{valor_casteado}' exitosamente.")

                elif operacion == "2":
                    if estructura.esta_vacia():
                        print(
                            "\nResultado: Operación denegada. La estructura está vacía."
                        )
                    else:
                        sacado = estructura.sacar()
                        print(f"\nResultado: El elemento retirado es '{sacado}'.")

                elif operacion == "3":
                    if estructura.esta_vacia():
                        print(
                            "\nResultado: Operación denegada. La estructura está vacía."
                        )
                    else:
                        frente = estructura.mira()
                        print(f"\nResultado: El elemento accesible es '{frente}'.")

                elif operacion == "4":
                    vacia = estructura.esta_vacia()
                    print(f"\nResultado: ¿Está vacía? -> {vacia}")

                elif operacion == "5":
                    tamanio = estructura.devolver_tamanio()
                    print(f"\nResultado: El tamaño actual es {tamanio}.")

                else:
                    print("\nOpción no reconocida.")
                    continue

                print(f"Estado actual de la {nombre_estructura}: {estructura}")

            except ValueError:
                print(
                    f"\nError de tipo: Por favor ingrese un valor válido de tipo {tipo_dato.__name__}."
                )
            except Exception as e:
                print(f"\nError inesperado: {e}")


if __name__ == "__main__":
    main()
