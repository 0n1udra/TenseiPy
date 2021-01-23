class Skill:
    def __init__(self):
        self.name = 'N/A'
        self.type = 'Activatable Skill'
        self.skill_level = 'Common Skill'
        self.damage_level = 1
        self.info_page = 'N/A'
        self.damage_type = 'N/A'
        self.description = 'N/A'
        self.evolution = 'N/A'
        self.abilities = 'N/A'
        self.acquired_msg = ''
        self.status = ''
        self.use_requirements = {}

        self.eat = True
        self.sub_skills = {}

        self.game_object_type = 'attribute'

    def get_name(self):
        return self.name.lower()

    def __str__(self):
        return self.name.lower()

    def show_acquired_msg(self):
        print(f"    {self.acquired_msg}\n")

    def update_info(self):
        if self.status:
            self.info_page = f'    Name: [{self.name}] ({self.status})'
        else:
            self.info_page = f'    Name: [{self.name}]'

        self.info_page += f"""
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

        if self.use_requirements:
            self.info_page += "\n    Use Requirements:\n"
            for item, amount in self.use_requirements.items():
                self.info_page += f"        {amount}x [{item}]\n"

        self.acquired_msg = f"<< Acquired {self.skill_level} [{self.name}] successfully. >>"

class Resistance(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.skill_level = 'Resistance'
        self.type = 'Passive'
        self.passive = True
        self.resist_types = []


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
        self.evolution = "Sage > Great Sage > Raphael > Ciel"
        self.acquired_msg = "<< Ultimate Skill Core Manas [Ciel] Acquired! >>"
        self.update_info()


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
        self.update_info()


#                    ========== Unique Skills ==========
class Predator_Mimicry_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Mimic'
        self.skill_level = 'Unique Skill'

        self.acquired_mimicries = {'Special S': {}, 'S': {}, 'Special A': {}, 'A+': {}, 'A': {},
                                   'A-': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, 'Other': {}}

    def show_info_page(self):
        data = "\n    -----Available Mimicries-----\n"
        for mob_level, mobs in self.acquired_mimicries.items():
            data += f'    {mob_level}:\n'
            for mob_name, mob in mobs.items():
                data += f'        {mob_name}\n'
        data += "\n    Note: To reset mimicry use 'mimic reset'. use 'info predator' for more info on mimicry.\n"
        return data

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
              
              Usage:
              > eat
              
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
              
            Usage:
            > mimic tempest serpent
              
        Isolation   
            - Materials harmful or unnecessary for analysis can also be stored. They will be used to replace magic energy.
        """
        self.evolution = 'Predator > Gluttony > Gluttonous King Beelzebub > Void God Azathoth'
        self.update_info()

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
        self.update_info()


#                    ========== Extra Skills ==========
class Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Sage'
        self.skill_level = 'Extra Skill'
        self.update_info()

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
        self.update_info()

    def use_skill(self, user):
        print("    < Activated: Extra Skill [Magic Perception] >")
        user.update_status('magic perception', 'Active')
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
        self.update_info()


#                    ========== Common Skills ==========
class Hydraulic_Propulsion(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Hydraulic Propulsion'
        self.description = 'Uses pressure to create a powerful water jet that can propel its user through vast distances.'
        self.evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
        self.use_requirements = {'Water': 1}
        self.update_info()

    def use_skill(self, user):
        if user.check_acquired("water", 1):
            user.remove_inventory('water', 1)
            return True
        else:
            print("\n    < Skill Requires: 1x [Water] >")
            return False

class Water_Blade(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Water Blade'
        self.damage_type = 'Melee'
        self.damage_level = 6
        self.description = 'Shoot out a thin water blade with tremendous cutting power.'
        self.evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
        self.update_info()

class Water_Bullet(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Water Bullet'
        self.damage_type = 'Melee'
        self.damage_level = 6
        self.description = "Shoot out a small powerful water bullet."
        self.evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
        self.update_info()


#                    ========== Intrinsic Skills ==========
class Absorb_Dissolve(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Absorb/Dissolve'
        self.skill_level = 'Intrinsic Skill'
        self.description = 'Slime-species intrinsic Skills that are inferior versions of Unique Skills Predator and Glutton.'
        self.update_info()

class Self_Regeneration(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Self-Regeneration'
        self.status = 'Passive'
        self.skill_level = 'Intrinsic Skill'
        self.description = '''
        Restores the user's damaged body. 
        It can restore even lost limbs as long as it's not a situation where the limbs get continuously chopped off or crushed. 
        The Skill's performance can be enhanced by other Skills.
        '''
        self.evolution = 'Self-Regeneration > Ultraspeed Regeneration > Endless Regeneration'
        self.update_info()


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
        self.update_info()

    def use_skill(self, user):
        print("    -----Nearby Heat Sources-----")
        for mob in user.active_mobs:
            if mob[0].is_alive:
                print(f'    {mob[1]}x {mob[0].name}')
        return True

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
        self.update_info()


# ========== Giant Bat
class Vampirism(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Vampirism'
        self.skill_level = 'Intrinsic Skill'
        self.damage_type = 'Melee'
        self.damage_level = 4
        self.description = "By sucking the target's blood the user can temporarily gain its Skills."
        self.update_info()

class Ultrasound_Waves(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Ultrasound Waves'
        self.skill_level = 'Intrinsic Skill'
        self.damage_type = 'Melee'
        self.damage_level = 3
        self.description = "Used bewilder the enemy or causing him to faint. The Skill can also pinpoint one's location"
        self.update_info()


# ========== Evil Centipede
class Paralyzing_Breath(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Paralyzing Breath'
        self.skill_level = 'Intrinsic Skill'
        self.damage_type = 'Poison'
        self.damage_level = 5
        self.description = "The ability to release a powerful paralyzing breath. A good skill to use during an ambush."
        self.update_info()


# ========== Black Spider
class Sticky_Thread(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Sticky Thread'
        self.skill_level = 'Intrinsic Skill'
        self.damage_type = 'Melee'
        self.damage_level = 2
        self.description = "A thin sticky thread that traps enemies and prevent them from moving."
        self.update_info()

    def use_thread(self):
        pass

class Steel_Thread(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.name = 'Steel Thread'
        self.skill_level = 'Intrinsic Skill'
        self.damage_type = 'Melee'
        self.damage_level = 5
        self.description = "A strong thin steel thread used to defend against enemy attacks or when making a nest."
        self.update_info()


#                    ========== Resistances ==========
class Resist_Pain(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Resist Pain'
        self.resist_types = ['Pain']
        self.description = '''
        Tolerance-type Skill that grants immunity to physical pain sensation. 
        However, you still take damage.
        '''
        self.update_info()

class Resist_Melee(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Resist Melee'
        self.resist_types = ['Melee']
        self.description = 'Tolerance-type Skill that grants immunity to melee attacks.'
        self.update_info()

class Resist_Electricity(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Resist Electricity'
        self.resist_types = ['Electricity']
        self.description = '''
        Tolerance-type Skill that grants resistance to electricity-types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
        '''
        self.update_info()

class Resist_Temperature(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Resist Temperature'
        self.resist_types = ['hot', 'cold', 'temperature']
        self.description = '''
        Tolerance-type Skill that grants extraordinary high resistance to fire, ice, heat and cold types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
        '''
        self.update_info()

class Resist_Poison(Resistance):
    def __init__(self):
        Resistance.__init__(self)
        self.name = 'Resist Poison'
        self.resist_types = ['Poison']
        self.description = '''
        Tolerance-type Skill that grants resistance to poison-types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
        '''
        self.update_info()
