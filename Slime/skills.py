class Skill:
    def __init__(self):
        self.skillLevel = None
        self.skillPower = 0

        self.predate = True
        self.energy = 0

    def acquireSkill(self):
        pass


class Unique_Skill(Skill):
    def init(self):
        self.skillLevel = 'Unique Skill'

class Extra_Skill(Skill):
    pass


##### Extra Skills #####

class Sage_Skill(Extra_Skill):
    def __str__(self):
        return("Sage")

    def acquireSkill(self):
        self.playerInventory['Extra Skills'].append(Sage_Skill)
        print("<<Extra skill [Sage] successfully acquired>>")

##### Unique Skills #####

class Predator_Skill(Unique_Skill):
    

    def acquireSkill(self):
        self.playerInventory['Unique Skills'].append(Predator_Skill)
        print("<<Unqiue skill [Predator] successfully acquired>>")

    def __str__(self):
        return("Predator")


class Great_Sage_Skill(Sage_Skill, Unique_Skill):

    def acquireSkill(self):
        self.playerInventory['Unique Skills'].append(Great_Sage_Skill)
        print("<<Unqiue skill [Great Sage] successfully acquired>>")

    def __str__(self):
        return("Great Sage")
