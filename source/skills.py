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


# ===== Manas =====
class Ciel_Skill(Skill):
    def __init__(self):
        Skill__init__(self)
        self.name = 'Ciel'
        self.skillLevel = 'Manas'
        self.AcquiredMsg = "<<Ulitamte Skill Core Manas [Ciel] Acquired!>>"
        self.info = """
    Name: [Ciel]
    Type: Ultimate Skill Core Manas

    Description:
        Evolved from Wisdom King Raphael

    Abilities:
        Auto Battle Mode 
            - Great sage can battle on behalf of user of permission granted

        Thought Acceleration(1m), Analytical Appraisal, Parallel Processing, Chant Discarded, 
        All of Creation, Analysis Expert, Synthesis/Separation, Skill Modification, Future Attack Prediction,
        Fusion, Food Chain, Soul Corridor

    Evolution:
        Sage > Great Sage > Raphael > Ciel
    """


# ===== Ultimate Skill=====
class Raphael_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Great Sage'
        self.skillLevel = 'Unique Skill'
        self.AcquiredMsgMsg = "<<Unique skill [Great Sage] Acquired.>>"
        self.info = """
    Name: [Wisdom King Raphael]
    Type: Ultimate Skill

    Description:
        Evolved version of Great Sage

    Abilities:
        Auto Battle Mode 
            - Great sage can battle on behalf of user of permission granted

        Thought Acceleration(1m), Analytical Appraisal, Parallel Processing, Chant Annulment, 
        All of Creation, Analysis, Synthesis/Separation, Skill Modification, Future Attack Prediction

    Evolution:
        Sage > Great Sage > Raphael > Ciel
        """


# ===== Unique Skills =====

class Predator_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Predator'
        self.skillLevel = 'Unique Skill'
        self.AcquiredMsgMsg = "<<Unique skill [Predator] successfully Acquired.>>"
        self.info = """
    Name: [Predator]
    Type: Unique Skill

    Description:
        ???

    Abilities:
        Predation   
            - Aborts target
        Analysis    
            - Analysis absorbed target
        Stomach     
            - Stores absorbed target
        Mimicry     
            - Mimics targets appearance. Use targets abilities if analysis was successful
        Isolation   
            - Isolates harmful objects

    Evolution:
        Predator > Gluttony > Gluttonous King Beelzebuth > Void God Azathoth
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
        self.info = """
    Name: [Great Sage]
    Type: Extra Skill

    Description:
        Great Sage is a Conceptual Intelligence that has a heartless and emotionless personality 
        and is solely driven by purely logical computations. It cares for nobody but the benefit 
        of its master, Rimuru, even going so far as to hide things from Rimuru if it deems it 
        beneficial to him in the long run.

    Abilities:
        Auto Battle Mode 
            - Great sage can battle on behalf of user of permission granted

        Thought Acceleration(1k), Analytical Appraisal, Parallel Processing, Chant Annulment, 
        All of Creation, Analysis

    Evolution:
        Sage > Great Sage > Raphael > Ciel
        """

# ===== Extra Skills =====

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

        self = """
        Name: [Magic Perception], [Magic Sense]
        Type: Extra Skill

        Description: 
            One can perceive the surrounding magical energy. It's not a major skill, and acquiring 
            the skill is rather simple.

            With this skill, one can see 360 degrees around them, without a single blind-spot. With this, 
            even if one's eyes and ears are crushed, one can continue combat. Ambushes become impossible. It's an indispensable skill.
        """

# ===== Common Skills =====

class Hydraulic_Propulsion(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Hydraulic Propulsion'
        self.skillLevel = 'Common Skill'
        self.AcquiredMsgMsg = '<<Skill [Hydraulic Propulsion] Acquired.>>'  
        self.info = """
    Name: [Hydraulic Propulsion]
    Type: Common Skill

    Description:
        ???

    Abilities:
        ???

    Evolution:
        ??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation
        > Law Manipulation
        """

