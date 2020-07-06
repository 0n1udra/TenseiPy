
class Skill:
    def __init__(self):
        self.name = 'N/A'
        self.type = 'Activatable Skill'
        self.skill_level = 'Common Skill'
        self.damage_level = 1
        self.damage_type = 'N/A'
        self.description = 'N/A'
        self.acquired_msg = ''
        self.evolution = 'N/A'
        self.abilities = 'N/A'

        self.active = False
        self.passive = False
        self.predate = True
        self.sub_skills = {}

        self.game_object_type = 'skill'

    def get_acquired_msg(self):
        return self.acquired_msg

    def update_skill_info(self):
        self.info = f"""
    Name: {self.name}
    Type: {self.type}
    Level: {self.skill_level}
    Damage: {self.damage_level}
    Damage Type: {self.damage_type}

    Description:
        {self.description}

    Abilities:
        {self.abilities}

    Evolution:
        {self.evolution}
    """

        self.acquired_msg = f"<<{self.skill_level} [{self.name}] Acquired.>>"

    def get_name(self):
        return self.name.lower()

    def __str__(self):
        return self.name


class Resistance(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.skill_level = 'Resistance'
        self.type = 'Passive'
        self.passive = True
        self.resistTypess = []


#                    ========== Manas ==========
class Ciel_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Ciel'
        self.skill_level = 'Manas'
        self.description = "Evolved from Wisdom King Raphael."
        self.abilities = """
        Auto Battle Mode 
            - Great sage can battle on behalf of user of permission granted
        """
        self. evolution = "Sage > Great Sage > Raphael > Ciel"
        self.update_skill_info()
        self.acquired_msg = "<<Ulitamte Skill Core Manas [Ciel] Acquired!>>"


# ===== Ultimate Skill=====
class Raphael_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Wisdom King Raphael'
        self.skill_level = 'Ultimate Skill'
        self.description = 'Evolved version of Great Sage.'
        self.abilities = """
        Auto Battle Mode 
            - Great sage can battle on behalf of user of permission granted
        """
        self.evolution = "Sage > Great Sage > Wisdom King Raphael > Ciel"
        self.update_skill_info()


#                    ========== Unique Skills ==========
class Predator_Mimicry_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Mimic'
        self.skill_level = 'Unique Skill'

    @property
    def info(self):
        print("\t-----Available Mimicries-----")
        for level, mob_list in self.acquired_mimics.items():
            print(f'\t{level} :')
            for mob in mob_list:
                print(f'\t\t{mob.name}')
        print("\n\t'mimic reset' to reset mimicry. use 'info predator' for more info on mimicry.")
    
class Predator_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Predator'
        self.skill_level = 'Unique Skill'
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
        self.update_skill_info()
        self.acquired_msg = "<<Unique Skill [Predator] successfully Acquired.>>"


class Great_Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Great Sage'
        self.skill_level = 'Unique Skill'
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
        self.update_skill_info()
        self.acquired_msg = f'<<Unique Skill [Great Sage] Successfully Acquired!>>'


#                    ========== Extra Skills ==========
class Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Sage'
        self.skill_level = 'Extra Skill'
        self.update_skill_info()

class Magic_Perception(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Magic Perception'
        self.skill_level = 'Extra Skill'
        self.description = '''
        One can perceive the surrounding magical energy. It's not a major skill, and acquiring 
        the skill is rather simple.

        With this skill, one can see 360 degrees around them, without a single blind-spot. With this, 
        even if one's eyes and ears are crushed, one can continue combat. 
        Ambushes become nearly impossible. It's an indispensable skill.
        '''
        self.update_skill_info()

    def UseSkill(self):
        print("\t<Activated Extra Skill [Magic Perception].>")
        self.active = True
        return True


class Water_Manipulation(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = "Water Manipulation"
        self.skill_level = 'Extra Skill'
        self.description = '''
        After learned Hydraulic Propulsion, Water Current Control, and Water Blade. 
        The three Skills are fused and evolved into Water Manipulation.
        '''
        self.evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
        self.update_skill_info()


#                    ========== Common Skills ==========
class Hydraulic_Propulsion(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Hydraulic Propulsion'
        self.escription = 'Uses pressure to create a powerful water jet that can propel its user through vast distances.'
        self.evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
        self.update_skill_info()

class Water_Blade(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Water Blade'
        self.damage_type = 'Melee'
        self.damage_level = 9
        self.description = 'Shoot out a thin water blade with tremendous cutting power.'
        self.evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
        self.update_skill_info()

class Water_Bullet(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Water Bullet'
        self.damage_type = 'Melee'
        self.damage_level = 9
        self.description = "Shoot out a small powerful water bullet."
        self.evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
        self.update_skill_info()


#                    ========== Intrinsic Skills ==========
class Absorb_Dissolve(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Absorb/Dissolve'
        self.skill_level = 'Intrinsic Skill'
        self.description = 'Slime-species intrinsic Skills that are inferior versions of Unique Skills Predator and Glutton.'
        self.update_skill_info()

class Self_Regeneration(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Self-Regeneration'
        self.skill_level = 'Intrinsic Skill'
        self.description = '''
        Restores the user's damaged body. 
        It can restore even lost limbs as long as it's not a situation where the limbs get continuously chopped off or crushed. 
        The Skill's performance can be enhanced by other Skills.
        '''
        self.evolution = 'Self-Regeneration > Ultraspeed Regeneration > Endless Regeneration'
        self.update_skill_info()

# ========== Tempest Serpent
class Sense_Heat_Source(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Sense Heat Source'
        self.skill_level = 'Intrinsic Skill'
        self.description = '''
        Identifies any heat reactions in the local area. 
        Not affected by any concealing effects.
        '''
        self.update_skill_info()

    def UseSkill(self):
        try:
            print("\t-----Nearby Heat Sources-----")
            for i in rimuru.current_level_characters:
                if i.alive:
                    print(f'\t{i.name}')
            return True
        except: pass

class Poisonous_Breath(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Poisonous Breath'
        self.skill_level = 'Intrinsic Skill'
        self.damage_type = 'Poison'
        self.damage_level = 8
        self.description = '''
        A powerful breath-type poison (corrosion) attack. 
        Affects an area seven meters in front of the user in a 120-degree radius.
        '''
        self.update_skill_info()

# ========== Giant Bat
class Vampirism_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Vampirism'
        self.skill_level = 'Intrinsic Skill'
        self.damage_type = 'Melee'
        self.damage_level = 4
        self.description = "By sucking the target's blood the user can temporarily gain its Skills."
        self.update_skill_info()

class Ultrasound_Waves(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Ultrasound Waves'
        self.skill_level = 'Intrinsic Skill'
        self.damage_type = 'Melee'
        self.damage_level = 3
        self.description = "Used bewilder the enemy or causing him to faint. The Skill can also pinpoint one's location"
        self.update_skill_info()

# ========== Evil Centipede
class Paralyzing_Breath(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Paralyzing Breath'
        self.skill_level = 'Intrinsic Skill'
        self.damage_type = 'Poison'
        self.damage_level = 5
        self.description = "The ability to release a powerful paralyzing breath. A good skill to use during an ambush."
        self.update_skill_info()

# ========== Black Spider
class Sticky_Thread(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Sticky Thread'
        self.skill_level = 'Intrinsic Skill'
        self.damage_type = 'Melee'
        self.damage_level = 2
        self.description = "A thin sticky thread that traps enemies and prevent them from moving."
        self.update_skill_info()

    def UseSkill(self):
        try:
            rimuru.target.movement = False
            return True
        except: pass


class Steel_Thread(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Steel Thread'
        self.skill_level = 'Intrinsic Skill'
        self.damage_type = 'Melee'
        self.damage_level = 5
        self.description = "A strong thin steel thread used to defend against enemy attacks or when making a nest."
        self.update_skill_info()


#                    ========== Resistances ==========
class Resist_Pain(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Resist Pain'
        self.resistTypes = ['Pain']
        self.description = '''
        Tolerance-type Skill that grants immunity to physical pain sensation. 
        However, you still take damage.
        '''
        self.update_skill_info()

class Resist_Melee(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Resist Melee'
        self.resistTypes = ['Melee']
        self.description = 'Tolerance-type Skill that grants immunity to melee attacks.'
        self.update_skill_info()

class Resist_Electricity(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Resist Electricity'
        self.resistTypes = ['Electricity']
        self.description = '''
        Tolerance-type Skill that grants resistance to electricity-types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
        '''
        self.update_skill_info()

class Resist_Temperature(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Resist Temperature'
        self.resistTypes = ['hot', 'cold', 'temperature']
        self.description = '''
        Tolerance-type Skill that grants extraordinary high resistance to fire, ice, heat and cold types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
        '''
        self.update_skill_info()

class Resist_Poison(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Resist Poison'
        self.resistTypes = ['Poison']
        self.description = '''
        Tolerance-type Skill that grants resistance to poison-types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
        '''
        self.update_skill_info()
