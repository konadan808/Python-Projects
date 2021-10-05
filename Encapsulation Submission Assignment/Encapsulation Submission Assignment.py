# Encapsulation Submission Assignment

# Class Color with private variable
class Color:
    def __init__(self):
        self.__fColor = "Green"
# Protected method of getPrivate
    def _getPrivate(self):
        print(self.__fColor)
# Protected method of setPrivate
    def _setPrivate(self, private):
        self.__fColor = private
#Object instantiation of color class
obj = Color()
obj._getPrivate()
obj._setPrivate("Blue")
obj._getPrivate()

