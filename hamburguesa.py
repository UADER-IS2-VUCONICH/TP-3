from factory import Creator, Product


class Hamburguesa(Product):
    def operation(self) -> str:
        return "Hamburguesa"


class HamburguesaParaMostrador(Hamburguesa):
    def operation(self) -> str:
        return "Hamburguesa para mostrador."


class HamburguesaParaRetirar(Hamburguesa):
    def operation(self) -> str:
        return "Hamburguesa para retirar."


class HamburguesaParaDelivery(Hamburguesa):
    def operation(self) -> str:
        return "Hamburguesa para delivery."


class HamburguesaFactory1(Creator):
    def factory_method(self) -> Product:
        return HamburguesaParaMostrador()


class HamburguesaFactory2(Creator):
    def factory_method(self) -> Product:
        return HamburguesaParaRetirar()


class HamburguesaFactory3(Creator):
    def factory_method(self) -> Product:
        return HamburguesaParaDelivery()


if __name__ == "__main__":
    factory1 = HamburguesaFactory1()
    product1 = factory1.factory_method()
    print(factory1.some_operation())

    factory2 = HamburguesaFactory2()
    product2 = factory2.factory_method()
    print(factory2.some_operation())

    factory3 = HamburguesaFactory3()
    product3 = factory3.factory_method()
    print(factory3.some_operation())
