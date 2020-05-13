class Skill:
    def __init__(self):
        self.name = ''
        self.skillLevel = ''
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
        self.AcquiredMsgMsg = "<<Unqiue skill [Predator] successfully AcquiredMsg.>>"

class Great_Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Great Sage'
        self.skillLevel = 'Unique Skill'
        self.AcquiredMsgMsg = "<<Unqiue skill [Great Sage] AcquiredMsg.>>"

##### Extra Skills #####

class Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Sage'
        self.skillLevel = 'Extra Skill'
        self.AcquiredMsgMsg = "<<Extra skill: [Sage] has been successfully AcquiredMsg.>>"

class Magic_Perception_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Magic Perception'
        self.skillLevel = 'Extra Skill'
        self.AcquiredMsgMsg = "<<Extra skill: [Magic Perception] AcquiredMsg.>>"

##### Common Skills #####

class Hydraulic_Propulsion(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Hydraulic Propulsion'
        self.skillLevel = 'Common Skill'
        self.AcquiredMsgMsg = '<<Skill [Hydraulic Propulsion] AcquiredMsg.>>'

