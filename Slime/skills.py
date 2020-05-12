class Skill:
    def __init__(self):
        self.name = ''
        self.skillLevel = 0
        self.acquredMsg = ''

        self.skillPower = 0
        self.energy = 0

        self.predate = True

    def acquired(self):
        return(self.acquiredMsg)

    def __str__(self):
        return(self.name)



##### Extra Skills #####

class Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Sage'
        self.skillLevel = 'Extra Skill'
        self.acquiredMsg = "<<Extra skill: [Sage] has been successfully acquired>>"



##### Unique Skills #####

class Predator_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Predator'
        self.skillLevel = 'Unique Skill'
        self.acquiredMsg = "<<Unqiue skill [Predator] successfully acquired>>"



class Great_Sage_Skill(Skill):
    def init(self):
        pass

    def acquireSkill(self):
        self.playerInventory['Unique Skill'].append(Great_Sage_Skill)
        print("<<Unqiue skill [Great Sage] successfully acquired>>")

    def __str__(self):
        return("Great Sage")
