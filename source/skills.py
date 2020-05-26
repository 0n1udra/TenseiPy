class Skill:
    def __init__(self):
        self.name = 'N/A'
        self.type = 'Skill'
        self.level = 'Common Skill'
        self.damageLevel = 0
        self.description = 'N/A'
        self.acquredMsg = ''
        self.evolution = 'N/A'
        self.abilities = 'N/A'

        self.active = False
        self.passive = False
        self.predate = True

        self.subSkills = {}

    def AcquiredMsg(self):
        return(self.acquiredMsg)

    def UpdateInfo(self):
        self.info = f"""
    Name: {self.name}
    Type: {self.type}
    Level: {self.level}
    Damage: {self.damageLevel}

    Description:
        {self.description}

    Abilities:
        {self.abilities}

    Evolution:
        {self.evolution}
    """

        self.acquiredMsg = f"<<{self.level} [{self.name}] Acquired.>>"

    def __str__(self):
        return(self.name)

class Resistance(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.level = 'Resistance'
        self.type = 'Passive'
        self.passive = True
        self.resistTypess = []


#                    ========== Manas ==========
class Ciel_Skill(Skill):
    def __init__(self):
        Skill__init__(self)
        self.name = 'Ciel'
        self.level = 'Manas'
        self.description = "Evolved from Wisdom King Raphael."
        self.abilities = """
        Auto Battle Mode 
            - Great sage can battle on behalf of user of permission granted
        """
        self. evolution = "Sage > Great Sage > Raphael > Ciel"
        self.UpdateInfo()
        self.acquiredMsg = "<<Ulitamte Skill Core Manas [Ciel] Acquired!>>"


# ===== Ultimate Skill=====
class Raphael_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Wisdom King Raphael'
        self.level = 'Ultimate Skill'
        self.description = 'Evolved version of Great Sage.'
        self.abilities = """
        Auto Battle Mode 
            - Great sage can battle on behalf of user of permission granted
        """
        self.evolution = "Sage > Great Sage > Wisdom King Raphael > Ciel"
        self.UpdateInfo()


#                    ========== Unique Skills ==========
class Predator_Mimicry_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Mimic'
        self.level = 'Unique Skill'
        self.mimics = {
                'A+': [],
                'A': [],
                'A-': [],
                'B+': [],
                'Special': [],
                }

    def AddMimicy(self, character):
        self.mimics.append(character)

    @property
    def info(self):
        print("\t-----Available Mimicry-----")
        for lvl, lvlList in self.mimics.items():
            print(f'\t{lvl} :')
            for name in lvlList:
                print(f'\t\t{name.name}')
        print("\n\t'mimic reset' to reset mimicry. use 'info predator' for more info on mimicry.")
    
class Predator_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Predator'
        self.level = 'Unique Skill'
        self.description = "Once target is in [Predators]'s Stomach, user can now use Analysis, Micmicry, and/or Isolation."
        self.abilities = """
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
        """
        self.evolution = 'Predator > Gluttony > Gluttonous King Beelzebub > Void God Azathoth'
        self.UpdateInfo()
        self.acquiredMsg = "<<Unique Skill [Predator] successfully Acquired.>>"


class Great_Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Great Sage'
        self.level = 'Unique Skill'
        self.description = '''
        A Conceptual Intelligence that has a heartless and emotionless personality 
        and is solely driven by purely logical computations. It cares for nobody but the benefit 
        of its master, even going so far as to hide things from master if it deems it beneficial in the long run.
        '''
        self.abilities = '''
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
        '''
        self.evolution = 'Sage > Great Sage > Raphael > Ciel'
        self.UpdateInfo()
        self.acquiredMsg = f'<<Unique Skill [Great Sage] Successfully Acquired!>>'


#                    ========== Extra Skills ==========
class Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Sage'
        self.level = 'Extra Skill'
        self.UpdateInfo()

class Magic_Perception(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Magic Perception'
        self.level = 'Extra Skill'
        self.description = '''
        One can perceive the surrounding magical energy. It's not a major skill, and acquiring 
        the skill is rather simple.

        With this skill, one can see 360 degrees around them, without a single blind-spot. With this, 
        even if one's eyes and ears are crushed, one can continue combat. 
        Ambushes become nearly impossible. It's an indispensable skill.
        '''
        self.UpdateInfo()

class Water_Manipulation(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = "Water Manipulation"
        self.level = 'Extra Skill'
        self.description = '''
        After learned Hydraulic Propulsion, Water Current Control, and Water Blade. 
        The three Skills are fused and evolved into Water Manipulation.
        '''
        self.evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
        self.UpdateInfo()


#                    ========== Common Skills ==========
class Hydraulic_Propulsion(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Hydraulic Propulsion'
        self.escription = 'Uses pressure to create a powerful water jet that can propel its user through vast distances.'
        self.evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
        self.UpdateInfo()

class Water_Blade(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Water Blade'
        self.type = 'Melee'
        self.damageLevel = 3
        self.description = "Shoot out a small powerful water bullet."
        self.evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
        self.UpdateInfo()

class Water_Bullet(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Water Bullet'
        self.type = 'Melee'
        self.damageLevel = 3
        self.description = 'Shoot out a thin water blade with tremendous cutting power.'
        self.evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
        self.UpdateInfo()


#                    ========== Intrinsic Skills ==========
class Absorb_Dissolve(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Absorb/Dissolve'
        self.level = 'Intrinsic Skill'
        self.description = 'Slime-species intrinsic Skills that are inferior versions of Unique Skills Predator and Glutton.'
        self.UpdateInfo()

class Self_Regeneration(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Self-Regeneration'
        self.level = 'Intrinsic Skill'
        self.description = '''
        Restores the user's damaged body. 
        It can restore even lost limbs as long as it's not a situation where the limbs get continuously chopped off or crushed. 
        The Skill's performance can be enhanced by other Skills.
        '''
        self.evolution = 'Self-Regeneration > Ultraspeed Regeneration > Endless Regeneration'
        self.UpdateInfo()


# ========== Tempest Serpent
class Sense_Heat_Source(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Sense Heat Source'
        self.level = 'Intrinsic Skill'
        self.description = '''
        Identifies any heat reactions in the local area. 
        Not affected by any concealing effects.
        '''
        self.UpdateInfo()

class Poisonous_Breath(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Poisonous Breath'
        self.level = 'Intrinsic Skill'
        self.type = 'Poison'
        self.damageLevel = 2
        self.description = '''
        A powerful breath-type poison (corrosion) attack. 
        Affects an area seven meters in front of the user in a 120-degree radius.
        '''
        self.UpdateInfo()


#                    ========== Resistances ==========
class Resist_Pain(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Pain Resist'
        self.resistTypes = ['Pain']
        self.description = '''
        Tolerance-type Skill that grants immunity to physical pain sensation. 
        However, you still take damage.
        '''
        self.UpdateInfo()

class Resist_Melee(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Melee Resist'
        self.resistTypes = ['Melee']
        self.description = 'Tolerance-type Skill that grants immunity to melee attacks.'
        self.UpdateInfo()

class Resist_Electricity(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Electricity Resist'
        self.resistTypes = ['Electricity']
        self.description = '''
        Tolerance-type Skill that grants resistance to electricity-types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
        '''
        self.UpdateInfo()

class Resist_Temperature(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Temperature Resist'
        self.resistTypes = ['hot', 'cold', 'temperature']
        self.description = '''
        Tolerance-type Skill that grants extraordinary high resistance to fire, ice, heat and cold types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
        '''
        self.UpdateInfo()

class Resist_Poison(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Poison Resist'
        self.resistTypes = ['Poison']
        self.description = '''
        Tolerance-type Skill that grants resistance to poison-types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
        '''
        self.UpdateInfo()
