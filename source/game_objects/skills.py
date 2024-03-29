from base_objects.skill import Skill

class Manas(Skill):
    skill_level = 'Manas'

class Ultimate(Skill):
    skill_level = 'Ultimate Skill'

class Unique(Skill):
    skill_level = 'Unique Skill'

class Extra(Skill):
    skill_level = 'Extra Skill'

class Common(Skill):
    skill_level = 'Common Skill'

class Intrinsic(Skill):
    skill_level = 'Intrinsic Skill'

class Resistance(Skill):
    skill_level = 'Resistance'
    type = 'Passive'
    passive = True
    resist_types = []


#                    ========== Manas ==========
class Ciel(Manas, Skill):
    name = 'Ciel'
    description = "Evolved from Wisdom King Raphael."
    abilities = """Auto Battle Mode 
      - Great sage can battle on behalf of user of permission granted
    """
    evolution = "Sage > Great Sage > Raphael > Ciel"
    acquired_msg = "<< Ultimate Skill Core Manas [Ciel] Acquired! >>"


#                    ========== Ultimate Skill ==========
class Raphael(Ultimate, Skill):
    name = 'Wisdom King Raphael'
    description = 'Evolved version of Great Sage.'
    abilities = """
    Auto Battle Mode 
      - Great sage can battle on behalf of user of permission granted
    """
    evolution = "Sage > Great Sage > Wisdom King Raphael > ???"


#                    ========== Unique Skills ==========
class Mimicry(Unique, Skill):
    name = 'Mimic'
    description = """Reproduces the form and Skills of absorbed targets.
        Only available once the target has been Analyzed.
    """

class Predator(Unique, Skill):
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
    evolution = 'Predator > ???'
    #evolution = 'Predator > Gluttony > Gluttonous King Beelzebub > Void God Azathoth'

    def use(self, user=None, *args):
        if user.check_if_player:
            user.eat_targets()
            return True
        return False

class Great_Sage(Unique, Skill):
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
    evolution = 'Sage > Great Sage > ???'

class Investigator(Unique, Skill):
    name = 'Investigator'
    description = '''A unique skill which allow Veldora to consult a record of the world’s event, 
        giving him the ability to analyze things.'''
    abilities = '''Multiple Barrier
          - An ability which surrounds the user with multiple barriers. Defensive barriers prevent to entry of magic power.
        Magic Sense
          - An ability to perceive the surrounding magical energy.'''

#                    ========== Extra Skills ==========
class Sage(Extra, Skill):
    name = 'Sage'

class Magic_Sense(Extra, Skill):
    name = 'Magic Sense'
    description = '''One can perceive the surrounding magical energy. It's not a major skill, and acquiring 
        the skill is rather simple.

        With this skill, one can see 360 degrees around them, without a single blind-spot. With this, 
        even if one's eyes and ears are crushed, one can continue combat. 
        Ambushes become nearly impossible. It's an indispensable skill.
    '''

    def use(self, user=None, *args):
        if not user: return False
        user.show_nearby(force_usage=True)
        return True

class Water_Manipulation(Extra, Skill):
    name = "Water Manipulation"
    description = '''After learned Hydraulic Propulsion, Water Current Control, and Water Blade. 
        The three Skills are fused and evolved into Water Manipulation.
    '''
    evolution = '* > Hydraulic Propulsion > Water Manipulation > ???'
    #evolution = '* > Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'

class Shadow_step(Extra, Skill):
    name = 'Shadow Step'
    description = '''allows the user to merge into the shadows.
        It also allows the user to appear out of the shadows in another location. Depending on the strength of an individual the range can vary.
        It allows for very fast travel between locations.'''
    evolution = 'Shadow Step > ???'
    #evolution = 'Shadow Step > Spatial Travel > Teleportation'


#                    ========== Intrinsic Skills ==========
# Slime
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
    evolution = 'Self-Regeneration > ???'
    #evolution = 'Self-Regeneration > Ultraspeed Regeneration > Endless Regeneration'

# Tempest Serpent
class Poisonous_Breath(Intrinsic, Skill):
    name = 'Poisonous Breath'
    damage_type = 'Poison'
    damage_level = 8
    description = '''A powerful breath-type poison (corrosion) attack. 
        Affects an area seven meters in front of the user in a 120-degree radius.
    '''

class Sense_Heat_Source(Intrinsic, Skill):
    name = 'Sense Heat Source'
    description = '''Identifies any heat reactions in the local area. 
        Not affected by any concealing effects.
    '''

    def use(self, user=None, *args):
        if not user: return False
        user.show_nearby(force_usage=True)
        return True

# Evil Centipede
class Paralyzing_Breath(Intrinsic, Skill):
    name = 'Paralyzing Breath'
    damage_type = 'Poison'
    damage_level = 5
    description = "The ability to release a powerful paralyzing breath. A good skill to use during an ambush."

# Giant Bat
class Vampirism(Intrinsic, Skill):
    name = 'Vampirism'
    damage_type = 'Melee'
    damage_level = 4
    description = "By sucking the target's blood the user can temporarily gain its Skills."

class Ultrasound_Waves(Intrinsic, Skill):
    name = 'Ultrasound Waves'
    damage_type = 'Melee'
    damage_level = 3
    description = "Used bewilder the enemy or causing him to faint. The Skill can also pinpoint one's location"

# Black Spider
class Sticky_Thread(Intrinsic, Skill):
    name = 'Sticky Thread'
    damage_type = 'Melee'
    damage_level = 2
    description = "A thin sticky thread that traps enemies and prevent them from moving."

class Steel_Thread(Intrinsic, Skill):
    name = 'Steel Thread'
    damage_type = 'Melee'
    damage_level = 5
    description = "A strong thin steel thread used to defend against enemy attacks or when making a nest."

# Direwolf
class Coercion(Intrinsic, Skill):
    name = 'Coercion'
    damage_type = 'Melee'
    damage_level = 1
    description = "Intimidate low level mobs with loud howling, can barely damage anything except very low level beings (like humnas)."

class Keen_smell(Intrinsic, Skill):
    name = 'Keen Smell'

class Thought_Communication(Intrinsic, Skill):
    name = 'Thought Communication'
    description = "Able to transmit thoughts/ideas/feelings to other beings, not just language."


#                    ========== Common Skills ==========
class Hydraulic_Propulsion(Common, Skill):
    name = 'Hydraulic Propulsion'
    description = 'Uses pressure to create a powerful water jet that can propel its user through vast distances.'
    evolution = 'Hydraulic Propulsion > ???'
    #evolution = 'Hydraulic Propulsion > Water Manipulation > Molecular Manipulation > Magic Manipulation > Law Manipulation'
    use_requirements = {'Water': 1}

class Water_Blade(Common, Skill):
    name = 'Water Blade'
    damage_type = 'Melee'
    damage_level = 6
    description = 'Shoot out a thin water blade with tremendous cutting power.'
    evolution = 'Water Blade > ???'
    use_requirements = {'Water': 1}

class Water_Bullet(Common, Skill):
    name = 'Water Bullet'
    damage_type = 'Melee'
    damage_level = 6
    description = "Shoot out a small powerful water bullet."
    evolution = 'Water Bullet > ???'
    use_requirements = {'Water': 1}


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
