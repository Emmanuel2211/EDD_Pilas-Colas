from picola_pkg.pila import Pila
from picola_pkg.cola import Cola


def main():
    p = Pila[int]()
    p2 = Pila[int]()
    c = Cola[int]()

    print(f"Pila: {p}")
    p.meter(1)
    print(f"Pila: {p}")
    p.meter(7)
    print(f"Pila: {p}")
    p.meter(-9)
    print(f"Pila: {p}")
    p.meter(23)
    print(f"Pila: {p}")
    p.meter(0)
    print(f"Pila: {p}")
    print(f"Tam: {p.devolver_tamanio()}")
    print(p.sacar())
    print(f"Pila: {p}")
    print(f"Tam: {p.devolver_tamanio()}")
    print(p.mira())
    print(p.esta_vacia())
    print(f"Pila: {p2}")
    p2.meter(1)
    print(f"Pila: {p2}")
    p2.meter(7)
    print(f"Pila: {p2}")
    p2.meter(-9)
    print(f"Pila: {p2}")
    p2.meter(23)
    print(f"Pila: {p2}")
    print(p.__eq__(p2))

    print(f"Cola: {c}")
    c.meter(2)
    print(f"Cola: {c}")
    c.meter(2)
    print(f"Cola: {c}")
    c.meter(2)
    print(f"Cola: {c}")
    c.meter(2)
    print(f"Cola: {c}")
    c.meter(2)
    print(f"Cola: {c}")
    print(f"Tam: {c.devolver_tamanio()}")


if __name__ == "__main__":
    main()
