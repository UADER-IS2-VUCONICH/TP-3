#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}\n"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""

class Factura(Product):
    @abstractmethod
    def calcular_impuestos(self):
        pass

    def generar_factura(self):
        impuestos = self.calcular_impuestos()
        total_factura = self.importe + impuestos
        return f"Factura: Total: {total_factura}, Importe: {self.importe}, Impuestos: {impuestos}, Tipo: {self.operation()}"


class FacturaIVAResponsable(Factura):
    def __init__(self, importe):
        self.importe = importe

    def calcular_impuestos(self):
        return self.importe * 0.21

    def operation(self) -> str:
        return "Factura IVA Responsable"

class FacturaIVANoInscripto(Factura):
    def __init__(self, importe):
        self.importe = importe

    def calcular_impuestos(self):
        return 0

    def operation(self) -> str:
        return "Factura IVA No Inscripto"

class FacturaIVAExento(Factura):
    def __init__(self, importe):
        self.importe = importe

    def calcular_impuestos(self):
        return self.importe * 0.1

    def operation(self) -> str:
        return "Factura IVA Exento"



