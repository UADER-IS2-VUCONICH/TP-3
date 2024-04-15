from singleton import Singleton

if __name__ == "__main__":
    calculator = Singleton()
    base_imponible = 1000
    impuestos_totales = calculator.calcular_impuestos(base_imponible)
    print(f"Impuestos totales para una base imponible de {base_imponible}: {impuestos_totales}")
