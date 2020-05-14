class Skill:
    def __init__(self):
        self.name = ''
        self.skillLevel = ''

        self.description = ''
        self.abilities = ''
        self.acquredMsg = ''

        self.skillPower = 0
        self.energy = 0

        self.subSkills = {}

        self.predate = True

    def AcquiredMsg(self):
        return(self.AcquiredMsgMsg)

    def __str__(self):
        return(self.name)


##### Unique Skills #####

class Predator_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Predator'
        self.skillLevel = 'Unique Skill'
        self.AcquiredMsgMsg = "<<Unique skill [Predator] successfully Acquired.>>"
        self.abilities = """
    Predation   -- Aborts target
    Analysis    -- Analysis absorbed target
    Stomach     -- Stores absorbed target
    Mimicry     -- Mimics targets appearance. Use targets abilities if analysis was successful
    Isolation   -- Isolates harmful objects
        """

        stomach = {
                "Organic": {},
                "Material": {},
                "Isolation": {},
                }

    def Predation(self):
        print("USE PREDATOR")

    def Mimicry(self):
        print("USE MIMICRY")

    def Stomach(self):
        print("USE STOMACH")

    def Mimicry(self):
        print("USE MIMICRY")

    def Analysis(self):
        print("USE ANALYSIS")

    def Isolation(self):
        print("USE ISOLATION")


class Great_Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Great Sage'
        self.skillLevel = 'Unique Skill'
        self.AcquiredMsgMsg = "<<Unique skill [Great Sage] Acquired.>>"
        self.description = "GREAT SAGE DESCRIPTION"
        self.abilities = """
    Auto Battle Mode -- Great sage can battle on behalf of user of permission granted

    Thought Acceleration, Analytical Appraisal, Parallel Processing, Chant Annulment, All of Creation, Analysis

        """

##### Extra Skills #####

class Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Sage'
        self.skillLevel = 'Extra Skill'
        self.AcquiredMsgMsg = "<<Extra skill: [Sage] has been successfully Acquired.>>"

class Magic_Perception_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Magic Perception'
        self.skillLevel = 'Extra Skill'
        self.AcquiredMsgMsg = "<<Extra skill: [Magic Perception] Acquired.>>"

##### Common Skills #####

class Hydraulic_Propulsion(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Hydraulic Propulsion'
        self.skillLevel = 'Common Skill'
        self.AcquiredMsgMsg = '<<Skill [Hydraulic Propulsion] Acquired.>>'

