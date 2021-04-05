from game_files.extra import format_info

class Skill:
    name = 'N/A'
    type = 'Activatable Skill'
    skill_level = 'Skill'
    damage_level = 1
    damage_type = ''
    info_page = ''
    description = ''
    evolution = ''
    abilities = ''
    acquired_msg = ''
    status = ''
    use_requirements = {}
    quantity = 0
    predate_copy = True  # Able to copy ability by using analysis, predate, etc.
    sub_skills = {}
    game_object_type = 'attribute'
    initialized = False

    def __init__(self):
        self.use_requirements, self.sub_skills = self.use_requirements, self.use_requirements
        self.initialized = True
        self.update_info()

    def __str__(self):
        return self.name.lower()

    def meet_requirements(self, user):
        if self.use_requirements:
            # Check if user meets requirement or own prerequisites before using skill.
            for k, v in self.use_requirements.items():
                if not user.check_acquired(k, v):
                    print(f"    < Skill Requires: {v}x {k} >")
                    return False

    def expend_requirements(self, user):
        # If skill need specific requirements to be used.
        self.meet_requirements(user)
        # TODO Make it so skill can use up items or just need to own them but don't use them up (remove them).
        for k, v in self.use_requirements.items():
            user.remove_inventory(k, v)

    def use_action(self, user, *args):
        """
        Use skill, by default it'll just return True to signal player has used the skill.

        Args:
            user obj: Game character object of skill activator.

        Returns:
            bool: By default will return True to signal usage, if function not overwritten.
        """

        self.expend_requirements(user)
        return True

    def activate_skill(self, state='Active'):
        """Activates skill, then updates relevant variables."""

        if state.lower() in self.status: return  # If skill is already at that state.

        print(f"    < {self.skill_level} {self.name}: {state} >")
        self.status = state
        self.update_info()

    def deactivate_skill(self, state=''):
        """Deactivates skill, then updates relevant variables."""

        print(f"    < {self.skill_level} {self.name}: Deactivated >")
        self.status = state
        self.update_info()

    def show_acquired_msg(self):
        """Print skill's acquired message."""

        print(f"    {self.acquired_msg}")

    def update_info(self):
        """Updates skills info_page depending on what object variables has been set."""

        self.acquired_msg = f"<< Acquired {self.skill_level} [{self.name}] successfully. >>"

        self.info_page = f'    Name: [{self.name}] {"(" + self.status + ")" if self.status else ""}\n'

        # Only show fields that have set data.
        info_dict = {'Type': self.type, 'Level': self.skill_level, 'Damage': self.damage_level, 'Damage Type': self.damage_type,
                     'Evolution': self.evolution, '*Description': self.description, '*Abilities': self.abilities}

        for k, v in info_dict.items():
            if formatted_info := format_info(k, v):
                self.info_page += f"    {formatted_info}\n"

        if self.use_requirements:
            self.info_page += "\n    Use Requirements:\n"
            for item, amount in self.use_requirements.items():
                self.info_page += f"        {amount}x [{item}]\n"

class Manas:
    skill_level = 'Manas'

class Ultimate:
    skill_level = 'Ultimate Skill'

class Unique:
    skill_level = 'Unique Skill'

class Extra:
    skill_level = 'Extra Skill'

class Common:
    skill_level = 'Common Skill'

class Intrinsic:
    skill_level = 'Intrinsic Skill'

class Resistance:
    skill_level = 'Resistance'
    type = 'Passive'
    passive = True
    resist_types = []


#                    ========== Manas ==========
class Ciel_Skill(Manas, Skill):
    name = 'Ciel'
    description = "Evolved from Wisdom King Raphael."
    abilities = """Auto Battle Mode 
        - Great sage can battle on behalf of user of permission granted
    """
    evolution = "Sage > Great Sage > Raphael > Ciel"
    acquired_msg = "<< Ultimate Skill Core Manas [Ciel] Acquired! >>"


#                    ========== Ultimate Skill ==========
class Raphael_Skill(Ultimate, Skill):
    name = 'Wisdom King Raphael'
    description = 'Evolved version of Great Sage.'
    abilities = """
    Auto Battle Mode 
        - Great sage can battle on behalf of user of permission granted
    """
    evolution = "Sage > Great Sage > Wisdom King Raphael > Ciel"


#                    ========== Unique Skills ==========
class Mimicry_Skill(Unique, Skill):
    name = 'Mimic'
    description = """Reproduces the form and Skills of absorbed targets.
        Only available once the target has been Analyzed.
    """

class Predator_Skill(Unique, Skill):
    name = 'Predator'
    description = "Once target is in [Predators]'s Stomach, user can now use Analysis, Micmicry, and/or Isolation."
    abilities = """Predation   
            - Absorbs the target into the body. However, if the target is conscious, the success rate greatly decreases. 
              The affected targets include, but isn't limited to: organic matter, inorganic matter, skills, and magic.
              Usage:
              > eat
              > predate
              
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
    evolution = 'Predator > Gluttony > Gluttonous King Beelzebub > Void God Azathoth'

class Great_Sage_Skill(Unique, Skill):
    name = 'Great Sage'
    description = '''A Conceptual Intelligence that has a heartless and emotionless personality 
        and is solely driven by purely logical computations. It cares for nobody but the benefit 
        of its master, even going so far as to hide things from master if it deems it beneficial in the long run.
    '''
    abilities = '''Thought Acceleration
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
    evolution = 'Sage > Great Sage > Raphael > Ciel'


#                    ========== Extra Skills ==========
class Sage_Skill(Extra, Skill):
    name = 'Sage'

class Magic_Perception(Extra, Skill):
    name = 'Magic Perception'
    description = '''One can perceive the surrounding magical energy. It's not a major skill, and acquiring 
        the skill is rather simple.

        With this skill, one can see 360 degrees around them, without a single blind-spot. With this, 
        even if one's eyes and ears are crushed, one can continue combat. 
        Ambushes become nearly impossible. It's an indispensable skill.
    '''

    def use_action(self, user=None, *args):
        if not user: return False
        self.activate_skill()
        return True

class Water_Manipulation(Extra, Skill):
    name = "Water Manipulation"
    description = '''After learned Hydraulic Propulsion, Water Current Control, and Water Blade. 
        The three Skills are fused and evolved into Water Manipulation.
    '''
    evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'

class Vampirism(Extra, Skill):
    name = 'Vampirism'
    skill_level = 'Intrinsic Skill'
    damage_type = 'Melee'
    damage_level = 4
    description = "By sucking the target's blood the user can temporarily gain its Skills."


#                    ========== Intrinsic Skills ==========
class Absorb_Dissolve(Intrinsic, Skill):
    name = 'Absorb/Dissolve'
    description = 'Slime-species intrinsic Skills that are inferior versions of Unique Skills Predator and Glutton.'

class Self_Regeneration(Intrinsic, Skill):
    name = 'Self-Regeneration'
    status = 'Passive'
    description = '''Restores the user's damaged body. 
              It can restore even lost limbs as long as it's not a situation where the limbs get continuously chopped off or crushed. 
              The Skill's performance can be enhanced by other Skills.
              '''
    evolution = 'Self-Regeneration > Ultraspeed Regeneration > Endless Regeneration'

class Sticky_Thread(Extra, Skill):
    name = 'Sticky Thread'
    damage_type = 'Melee'
    damage_level = 2
    description = "A thin sticky thread that traps enemies and prevent them from moving."

class Steel_Thread(Extra, Skill):
    name = 'Steel Thread'
    damage_type = 'Melee'
    damage_level = 5
    description = "A strong thin steel thread used to defend against enemy attacks or when making a nest."

class Sense_Heat_Source(Extra, Skill):
    name = 'Sense Heat Source'
    description = '''Identifies any heat reactions in the local area. 
        Not affected by any concealing effects.
    '''

    def use_action(self, user=None, *args):
        if not user: return False
        user.show_nearby(valid_usage=True)
        return True


#                    ========== Common Skills ==========
class Hydraulic_Propulsion(Common, Skill):
    name = 'Hydraulic Propulsion'
    description = 'Uses pressure to create a powerful water jet that can propel its user through vast distances.'
    evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
    use_requirements = {'Water': 1}

class Water_Blade(Common, Skill):
    name = 'Water Blade'
    damage_type = 'Melee'
    damage_level = 6
    description = 'Shoot out a thin water blade with tremendous cutting power.'
    evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
    use_requirements = {'Water': 1}

class Water_Bullet(Common, Skill):
    name = 'Water Bullet'
    damage_type = 'Melee'
    damage_level = 6
    description = "Shoot out a small powerful water bullet."
    evolution = '??? > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
    use_requirements = {'Water': 1}

class Poisonous_Breath(Common, Skill):
    name = 'Poisonous Breath'
    damage_type = 'Poison'
    damage_level = 8
    description = '''A powerful breath-type poison (corrosion) attack. 
        Affects an area seven meters in front of the user in a 120-degree radius.
    '''

class Paralyzing_Breath(Common, Skill):
    name = 'Paralyzing Breath'
    damage_type = 'Poison'
    damage_level = 5
    description = "The ability to release a powerful paralyzing breath. A good skill to use during an ambush."

class Ultrasound_Waves(Common, Skill):
    name = 'Ultrasound Waves'
    damage_type = 'Melee'
    damage_level = 3
    description = "Used bewilder the enemy or causing him to faint. The Skill can also pinpoint one's location"


#                    ========== Resistances ==========
class Resist_Pain(Resistance, Skill):
    name = 'Resist Pain'
    resist_types = ['Pain']
    description = '''Tolerance-type Skill that grants immunity to physical pain sensation. 
        However, you still take damage.
    '''

class Resist_Melee(Resistance, Skill):
    name = 'Resist Melee'
    resist_types = ['Melee']
    description = 'Tolerance-type Skill that grants immunity to melee attacks.'

class Resist_Electricity(Resistance, Skill):
    name = 'Resist Electricity'
    resist_types = ['Electricity']
    description = '''Tolerance-type Skill that grants resistance to electricity-types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
    '''

class Resist_Temperature(Resistance, Skill):
    name = 'Resist Temperature'
    resist_types = ['hot', 'cold', 'temperature']
    description = '''Tolerance-type Skill that grants extraordinary high resistance to fire, ice, heat and cold types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
    '''

class Resist_Poison(Resistance, Skill):
    name = 'Resist Poison'
    resist_types = ['Poison']
    description = '''Tolerance-type Skill that grants resistance to poison-types of attacks. 
        Imbued into a layer of Multilayer Barrier, doubling the resistance effect.
    '''
