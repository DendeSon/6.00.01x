#Problem 6

class ArrogantProfessor(Professor): 
    def lecture(self, stuff): 
        return 'It is obvious that ' + self.name + " says: " + stuff
    def say(self, stuff):
        return self.name + " says: " + "It is obvious that " + self.name + " says: " + stuff