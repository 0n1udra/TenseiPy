class Skill:
    def __init__(self):
        self.name = ''
        self.skillLevel = ''

        self.description = ''
        self.abilities = ''
        self.acquredMsg = ''

        self.skillPower = 0
        self.energy = 0

        self.active = True
        # Able to predate
        self.predate = True


        self.subSkills = {}

    def AcquiredMsg(self):
        return(self.acquiredMsg)

    def __str__(self):
        return(self.name)

class Resistance(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.skillLevel = 'Resistance'


# ===== Manas =====
class Ciel_Skill(Skill):
    def __init__(self):
        Skill__init__(self)
        self.name = 'Ciel'
        self.skillLevel = 'Manas'
        self.acquiredMsg = "<<Ulitamte Skill Core Manas [Ciel] Acquired!>>"
        self.info = """
    Name: [Ciel]
    Type: Ultimate Skill Core Manas

    Description:
        Evolved from Wisdom King Raphael

    Abilities:
        Auto Battle Mode 
            - Great sage can battle on behalf of user of permission granted

    Evolution:
        Sage > Great Sage > Raphael > Ciel
    """


# ===== Ultimate Skill=====
class Raphael_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Great Sage'
        self.skillLevel = 'Unique Skill'
        self.acquiredMsg = "<<Unique Skill [Great Sage] Acquired.>>"
        self.info = """
    Name: [Wisdom King Raphael]
    Type: Ultimate Skill

    Description:
        Evolved version of Great Sage

    Abilities:
        Auto Battle Mode 
            - Great sage can battle on behalf of user of permission granted

    Evolution:
        Sage > Great Sage > Raphael > Ciel
        """


# ===== Unique Skills =====
class Predator_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Predator'
        self.skillLevel = 'Unique Skill'
        self.acquiredMsg = "<<Unique Skill [Predator] successfully Acquired.>>"
        self.info = """
    Name: [Predator]
    Type: Unique Skill

    Description:
        Once target is in [Predators]'s Stomach, user can now use Analysis, Micmicry, and Isolation.

    Abilities:
        Predation   
            - Absorbs the target into the body. However, if the target is conscious, the success rate greatly decreases. 
              The affected targets include, but isn't limited to: organic matter, inorganic matter, skills, and magic.
        Analysis    
            - The absorbed target is studied and analyzed. Craftable items can then be produced. 
              If the required materials are present, duplicates can be produced. 
              In the case of successful skill or magic analysis, the same technique can be acquired.
        Stomach     
            - The target can be stored. Items produced via Analysis can also be stored. There is no storage time limit.
              However, there is a capacity limit.
        Mimicry     
            - Replicate the target's appearance. The skills and abilities used by the target can also be used. 
              However, this depends on the successful analysis and acquisition of relative information regarding the target.
        Isolation   
            - Materials harmful or unnecessary for analysis can also be stored. They will be used to replace magic energy.


    Evolution:
        Predator > Gluttony > Gluttonous King Beelzebub > Void God Azathoth
        """


class Great_Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Great Sage'
        self.skillLevel = 'Unique Skill'
        self.acquiredMsg = "<<Unique Skill [Great Sage] Acquired.>>"
        self.info = """
    Name: [Great Sage]
    Type: Extra Skill

    Description:
        A Conceptual Intelligence that has a heartless and emotionless personality 
        and is solely driven by purely logical computations. It cares for nobody but the benefit 
        of its master, even going so far as to hide things from master if it deems it beneficial in the long run.

    Abilities:
        Thought Acceleration
            - Raises thought-processing speed by a thousand times.

        Analytical Appraisal
            - The ability to analyze and appraise a target.

        Parallel Processing
            - The ability to detach thoughts and analysis of phenomena. 
            - Detached thoughts are also under the effects of Thought Acceleration.

        Chant Annulment
            - When using magic, the chant is no longer necessary.

        All of Creation
            - The ability to comprehend any non-concealed phenomenon in this world. 
              Depending on the things the user understands and the information the user knows about, additional information can be inferred. 
              In other words, the user needs to see it (the phenomenon) at least once.

        Analysis
            - The absorbed target is studied and analyzed. Craftable items can then be produced. 
              If the required materials are present, duplicates can be produced. 
              In the case of successful skill or magic analysis, the same technique can be acquired. 
            - Originally a part of Unique Skill [Predator] was transferred over to [Great Sage] when [Predator] evolved into Unique Skill Gluttony.

        Auto Battle Mode
            - By giving permission to [Great Sage], The master can let it control his body temporarily


    Evolution:
        Sage > Great Sage > Raphael > Ciel
        """

# ===== Extra Skills =====
class Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Sage'
        self.skillLevel = 'Extra Skill'
        self.acquiredMsg = "<<Extra Skill: [Sage] has been successfully Acquired.>>"

class Magic_Perception_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Magic Perception'
        self.skillLevel = 'Extra Skill'
        self.acquiredMsg = "<<Extra Skill: [Magic Perception] Acquired.>>"

        self = """
        Name: [Magic Perception], [Magic Sense]
        Type: Extra Skill

        Description: 
            One can perceive the surrounding magical energy. It's not a major skill, and acquiring 
            the skill is rather simple.

            With this skill, one can see 360 degrees around them, without a single blind-spot. With this, 
            even if one's eyes and ears are crushed, one can continue combat. 
            Ambushes become nearly impossible. It's an indispensable skill.
        """

class Water_Manipulation_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = "Water Manipulation"
        self.skillLevel = 'Extra Skill'
        self.acauiredMsg = '<<Extra Skill [Water Manipulation] acquired.>>'
        self.info = """
        Name: Water Manipulation
        Type: Extra Skill

        Description:
            learned Hydraulic Propulsion, Water Current Control, and Water Blade, the three Skills were fused and evolved into Water Manipulation.
        """


# ===== Common Skills =====
class Hydraulic_Propulsion(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Hydraulic Propulsion'
        self.skillLevel = 'Common Skill'
        self.acquiredMsg = '<<Common Skill [Hydraulic Propulsion] Acquired.>>'  
        self.info = """
    Name: [Hydraulic Propulsion]
    Type: Common Skill

    Description:
        Uses pressure to create a powerful water jet that can propel its user through vast distances.

    Evolution:
        ??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation
        > Law Manipulation
        """

# ===== Intrinsic Skills =====
class Absorb_Dissolve_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Absorb/Dissolve'
        self.skillLevel = 'Intrinsic Skill'
        self.info = """
    Name: Absorb and Dissolve
    Type: Intrinsic Skill

    Description:
        Slime-species intrinsic Skills that are inferior versions of Unique Skills Predator and Glutton.
        """

class Self_Regeneration_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Self-Regeneration'
        self.skillLevel = 'Intrinsic Skill'
        self.info = """
    Name: Self-Regeneration
    Type: Intrinsic Skill

    Description:
        Restores the user's damaged body. 
        It can restore even lost limbs as long as it's not a situation where the limbs get continuously chopped off or crushed. 
        The Skill's performance can be enhanced by other Skills.
        """


# ========== Resistances ==========
class Resist_Pain(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Pain Resist'
        self.acquiredMsg = "<<[Pain Resist] acquired.>>"
        self.info = """
    Name: Pain Resist
    Type: Resistance

    Description:
        Tolerance-type Skill that grants immunity to physical pain sensation. However, you still take damage
        """

class Resist_Melee(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Melee Resist'
        self.acquiredMsg = "<<[Melee Resist] acquired.>>"
        self.info = """
    Name: Pain Resist
    Type: Resistance

    Description:
        Tolerance-type Skill that grants immunity to physical pain sensation. However, you still take damage
        """

class Resist_Electricity(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Electricity Resist'
        self.acquiredMsg = "<<[Electricity Resist] acquired.>>"
        self.info = """
    Name: Electricity Resist
    Type: Resistance

    Description:
        Tolerance-type Skill that grants resistance to electricity-types of attacks. Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
        """

class Resist_Temperature(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Temperature Resist'
        self.acquiredMsg = "<<[Temperature Resist] acquired.>>"
        self.info = """
    Name: Temperature Resist
    Type: Resistance

    Description:
        Tolerance-type Skill that grants extraordinary high resistance to fire, ice, heat and cold types of attacks. Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
        """


