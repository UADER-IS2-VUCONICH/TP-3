import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getPlane(self):
      plane = Plane()
      
      # Primero las (2) turbinas
      i = 0
      while i < 2:
         turbine = self.__builder.getTurbine()
         plane.attachTurbine(turbine)
         i += 1
      
      # Luego el tren de aterrizaje
      undercarriage = self.__builder.getUndercarriage()
      plane.setUndercarriage(undercarriage)
      
      # Finalmente (2) alas
      i = 0
      while i < 2:
         wings = self.__builder.getWings()
         plane.attachWings(wings)
         i += 1

      # Retorna el vehiculo completo
      return plane

#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Plane:
   def __init__(self):
      self.__wings = list()
      self.__turbine = list()
      self.__undercarriage = None

   def setUndercarriage(self, undercarriage):
      self.__undercarriage = undercarriage

   def attachWings(self, wings):
      self.__wings.append(wings)

   def attachTurbine(self, turbine):
      self.__turbine.append(turbine)

   def specification(self):
      print ("Tren de aterrizage: %s" % (self.__undercarriage.shape))
      print ("Turbinas: %d\'" % (self.__turbine[0].horsepower))
      print ("Alas: %d\'" % (self.__wings[0].size))

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
	
      def getWings(self): pass
      def getTurbine(self): pass
      def getUndercarriage(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un avion
#* Establece instancias para tomar alas, turbinas y tren de aterrizaje
#*-------------------------------------------------------
class PlaneBuilder(Builder):
   
   def getWings(self):
      wings = Wings()
      wings.size = 22
      return wings
   
   def getTurbine(self):
      turbine = Turbine()
      turbine.horsepower = 400
      return turbine
   
   def getUndercarriage(self):
      undercarriage = Undercarriage()
      undercarriage.shape = "Retractable"
      return undercarriage

#*----------------------------------------------------------------
#* Define partes genéricas para un avion (sin inicializar)
#*----------------------------------------------------------------
class Wings:
   size = None

class Turbine:
   horsepower = None

class Undercarriage:
   shape = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   planeBuilder = PlaneBuilder() # initializing the class
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Jeep
#*----------------------------------------------------------------   
   director.setBuilder(planeBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Jeep según
#* la hoja de ruta
#*----------------------------------------------------------------
   plane = director.getPlane()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   plane.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avion\n")

   main()
