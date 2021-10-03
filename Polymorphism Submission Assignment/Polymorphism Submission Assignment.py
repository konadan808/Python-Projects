# Polymorphism Submission Assignment

# Parent class of Droid
class Droid:
    def __init__(self, name, function, owner, output):
        self.name = name
        self.function = function
        self.owner = owner
        self.output = output

    def information(self):
        specs = "\nName: {}\nFunction: {}\nOwner: {}\nCommunication Method: {}".format(self.name,self.function,self.owner,self.output)
        return specs

    def audioOutput(self):
        msg = "Input Droid speech here"
        return msg
# Child class of protocolDroid
class protocolDroid(Droid):
    def __init__(self, name, function, owner, output, color, language):
        
        self.name = name
        self.function = function
        self.owner = owner
        self.output = output
        self.color = color
        self.language = language
        
    def information(self):
        specs = "\nName: {}\nFunction: {}\nOwner: {}\nCommunication Method: {}\nColor: {}\nLanguages Spoken {}".format(self.name,self.function,self.owner,self.output,self.color,self.language)
        return specs

    def audioOutput(self):
        msg = "\"I am C-3P0, human cyborg relations.\""
        return msg
# Child class of astromech
class astromech(Droid):
    def __init__(self, name, function, owner, output, skills, gadgets):
        
        self.name = name
        self.function = function
        self.owner = owner
        self.output = output
        self.skills = skills
        self.gadgets = gadgets
        
    def information(self):
        specs = "\nName: {}\nFunction: {}\nOwner: {}\nCommunication Method: {}\nSkills: {}\nGadgets {}".format(self.name,self.function,self.owner,self.output,self.skills,self.gadgets)
        return specs

    def audioOutput(self):
        msg = "\"Beeb beeb boop, beep!.\""
        return msg


if __name__ == "__main__":
    
    droid1 = protocolDroid("C-3P0", "Human Relations", "Princess Leia", "Spoken", "Gold", "Over 3 million forms of communication")
    print(droid1.information())
    print(droid1.audioOutput())

    droid2 = astromech("R2-D2", "Astromech", "Luke Skywalker", "Binary, beeps, and whisltes", "Computer interfacing, piloting, hero extraordinaire", "Circular saw, taser, computer interface, jets, comlink")
    print(droid2.information())
    print(droid2.audioOutput())
        
