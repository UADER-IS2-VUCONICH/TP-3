from factory import Creator, Factura, FacturaIVAResponsable, FacturaIVANoInscripto, FacturaIVAExento

def client_code(creator: Creator) -> None:
    factura = creator.factory_method()
    print(factura.generar_factura())

class ConcreteCreator1(Creator):
    def factory_method(self) -> Factura:
        return FacturaIVAResponsable(importe=1000)

class ConcreteCreator2(Creator):
    def factory_method(self) -> Factura:
        return FacturaIVANoInscripto(importe=1000)

class ConcreteCreator3(Creator):
    def factory_method(self) -> Factura:
        return FacturaIVAExento(importe=1000)

if __name__ == "__main__":
    creator1 = ConcreteCreator1()
    creator2 = ConcreteCreator2()
    creator3 = ConcreteCreator3()

    client_code(creator1)
    client_code(creator2)
    client_code(creator3)


