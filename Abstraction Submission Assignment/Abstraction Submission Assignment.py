# Abstraction Submission Assignment


from abc import ABC, abstractmethod

#class of Piaaz
class Pizza(ABC):
    #First, you must open the pizza packaging
    def openContainer(self):
        print("You pull the frozen pizza out of the packaging and place it on the counter.\n")
    #Now you must read the instructions to see how to heat the pizza
    def  readHeatInst(self):
        print("You read the options on how to heat the pizza.  You can use the oven, the microwave, or a toaster oven\n")
    #Since there are multiple options on heating the pizza, this method is left as abstract and defined below
    @abstractmethod
    def heatPizza(self):
        pass
    #Child class of Pizza with the heating method of toaster oven
class ToasterOven(Pizza):
    #Instructions on how to use the toaster oven to heat the pizza
    def heatPizza(self):
        print("You place the pizza in the toaster oven, turn it on, and 20 minutes later you have a hot pizza ready to slice and eat")

#instantiation of heating up a pizza
obj = ToasterOven()
obj.openContainer()
obj.readHeatInst()
obj.heatPizza()
