import skills, items, mobs

def ssprint(Msg):
    print(f'    {Msg}\n')

class Character:
    def __init__(self):
        self.name = 'N/A'
        self.familyName = ''
        self.title = 'N/A'
        self.species = 'N/A'
        self.rank = 'N/A'
        self.level = 1
        self.blessing = 'N/A'
        self.giveBlessing = 'N/A'
        self.info = 'N/A'
        self.appearance = 'N/A'
        self.description = 'N/A'
        self.alive = True
        self.invisible = False
        self.movement = False 
        self.evolution = ''

        # Game variables.
        self.storyProgress = [None]
        self.savePath = ''
        self.textDelay = True
        self.lastCommand = ''
        self.currentMobs = []
        self.focusTargets = set()

        # Predator ability variables.
        self.amount = 0
        self.addAmount = 1
        self.capacityUse = 0
        self.inventoryCapacity = 0
        self.objectType = 'character'

        self.subordinates = {'Special S': [], 'S': [], 'Special A': [], 'A+': [], 'A': [],
            'A-': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'Other': [],
            }

        self.friends = {'Special S': [], 'S': [], 'Special A': [], 'A+': [], 'A': [],
            'A-': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'Other': [],
            }
    
        self.attributes = {
            'Ultimate Skill': {},
            'Unique Skill': {},
            'Special Skill': {},
            'Extra Skill': {},
            'Intrinsic Skill': {},
            'Common Skill': {},
            'Daily Skill': {},
            'Composite Skill': {},
            'Resistance': {},
            'Attribute': {},
            'Manas': {},
        }

        self.inventory = {'Items': {}, 'Material': {}, 'Potions': {}, 'Misc': {}}


    # ========== Info
    def get_object(self, inp, mimic=False, new=False):
        '''
        Can take in either a str or obj, then returns object (initialized if not already in inventory).


        Args:
            inp (str):
                Either string or object instance of the object you want. If object, will get objects .name attribute.

            mimic (bool=False):
                If currently using Mimic ability, will also include mimicked mob attributes.

            new (bool=False):
                If first time adding a new object to inventory.

        Returns:
            Corresponding object, will initialize if one hasn't been already in inventory.
        '''

        # If input is an objects, gets objects name (str).
        try: 
            inp = inp.name
        except: pass

        generators = [*self.attributes_generator(), *self.inventory_generator(), *self.subordinate_generator()]



        try: 
            generators.extend(*self.MimicGenerator())
        except: pass

        # If object not in inventory. Will need to use __subclasses__ method to find, initialize and add to inventory.
        if new:
            generators = [ 
                *items.Item.__subclasses__(), 
                *skills.Skill.__subclasses__(), 
                *Character.__subclasses__() 
            ]

        # If currently using Mimic ability.
        if mimic:
            generators = [self.mimic_generator()]
        # Adds mimicked monster abilities if currently using mimic.
        if rimuru.mimicObject:
            generators.extend(self.attributes_generator(rimuru.mimicObject))
        
        for i in generators:
            try:
                if new:
                    i = i()
                if i.GetName() in inp.lower():
                    return i
                    break
                else:
                    del i
            except: pass

    def get_name(self):
        '''Returns object name attribute in lowercase.'''

        return self.name.lower()

    def run_start_state(self):
        '''Adds corresponding starter attributes and items to character.'''

        for i in self.startState:
            self.add_attributes(i, show_msg=False)

    def update_info(self):
        '''Updates character information.'''

        self.info = f"""
    Name: {self.name} {self.familyName}
    Title: {self.title}
    Species: {self.species}
    Rank: {self.rank}
    Alive: {self.alive}
    Divine Protection: {self.blessing}

    Description:
        {self.description}

    Appearance:
        {self.appearance}
        """

        # Sets ranking according to level
        ranking = ['Special S', 'S', 'Special A', 'A+', 'A', 'A-', 'B', 'C', 'D', 'E', 'F']
        self.rank = ranking[self.level - 1]

    def show_info(self, gameObject):
        '''
        Shows corresponding information for object.

        Args:
            GameObject (str):
                Game object that you want to get information on.

        Usage:
            > info predator
            > info tempest serpent
        '''
            
        try:
            print(self.get_object(gameObject).info)
        except:
            ssprint("<No available data.>")

    def update_ranking(self, character, level):
        '''
        Updates character ranking.

        Args:
            character (str):
                Character to level up.

            level (str):
                New level for character.

        Usage:
            .update_ranking('rimuru', 'A+')
        '''

        try:
            char = self.get_object(character)
        except:
            ssprint("<Error leveling up.>")
        else:
            char.level = level
            self.update_info()
            ssprint(f"<{char} rank up to {level}>")

    def check_mob_has(self, character, check_object):
        '''
        Checks to see if character has object/attribute/item/etc.

        Args:
            character (str):
                Check if character has the object.

            check_object (str):
                Object to check if specified character has item, attribute, skill, etc.

        Usage:
            .check_mob_has('rimuru', 'resist poison')

            > rimuru has resist melee
            >>True
        '''

        try:
            character = self.get_object(character)
            check_object = self.get_object(check_object)
        except:
            ssprint("<Error checking.>")

        if character and check_object:
            if character.get_object(check_object):
                return True:

    def check_resistance(self, character, damage_type):
        '''
        Checks if character has resistance.

        Args:
            character (str):
                Check if specified character has resistance.

            damage_type (str):
                Damage type to check resistance to.

        Usage:
            .check_resistance('rimuru', 'resist pain')
        '''
        
        # Checks if character has resistance attribute
        for resistName, resistObject in character.attributes['Resistance'].items():
            for resist in resistObject.resistTypes:
                if resist.lower() == attack.lower():
                    return True
                    break

    def use_skill(self, character, skill):
        '''
        Use skill that character has.

        Args:
            character (str):
                Character to use specified skill.

            skill (str):
                Skill to use by specified character.

        Usage:
            .use_skill('rimuru', 'magic perception')

            > use magic perception
            > ranga use spatial travel

        Returns:
            Boolean True/False if skill worked.
        '''

        try:
            char = self.get_object(character)
            skill = self.get_object(skill)
        except:
            ssprint("<Failed to use skill.>")
        else:
            if 
            try:
                if char.use_skill(skill):
                    return True
            except: pass


    # ========== Attack
    def set_target(self, targets):
        '''
        Adds mobs to focusTargets list from user input.

        Separates user inputted targets via ',' then checks to see if mob is in currentMobs list.
        If so, adds to setTargets list.

        Args:
            targets (str):
                String of target(s) to add to focusTargets (list)

        Usage:
            > target tempest serpent, giant bat
        '''

        if 'reset' in targets:
            self.focusTargets.clear()
        else:
            for target in targets.split(','):
                for i in self.currentMobs:
                    if i.get_name() in target:
                        self.focusTargets.add(i)
                        break

    def can_attack(self, targets_and_attacks):
        '''
        Checks if can attack, and if it was successful.

        First separates the targets and attacks via splitting up targets_and_attacks by commas ','.
        Then Adds the targets and attacks to corresponding lists.
        Checks if target is not too high of a level for attack and doesn't have resistance to said attack.
        Will return booleans for if attack was attempted and if attack was successful.

        Args:
            targets (str):
                Targets to attack, if multiple, separated by comma ','.

        Returns:
            attacked (bool=False):
                If attack was attempted.

            attackSuccess (bool=False):
                If attack was successful.

        Usage:
            .can_attack('tempest serpent')
            .can_attack('tempest serpent, giant bat')

            > attack tempest serpent
            > attack tempest serpent, giant bat
        '''

        targets = self.focusTargets
        targets_and_attacks = []

        # Tries to split targets and attacks if there are multiples separated by commas ','.
        try:
            current_targets = targets.split(',')
        except:
            current_targets = targets

        # If mob is in currentMobs list and is alive, adds to focusTarget list.
        for i in self.currentMobs:
            if i.get_name() in targets and i.alive:
                targets.add(i)
                self.focusTargets.add(i)

        # Checks if there are skills in targets_and_attacks list then adds skill object to attacks list.
        for i in current_targets:
            skill = self.get_object(i)
            if skill:
                if skill.GetName() in i.lower() and skill.objectType == 'skill':
                    targets_and_attacks.append(self.get_object(skill))


        attacked = attackSuccess = False

        for currentTarget in targets:
            for currentAttack in targets_and_attacks:
                # Checks if target has resistance to current attack.
                if not self.check_resistance(currentTarget, currentAttack.damageType):
                    # Checks if target is lower level than current attack.
                    if currentTarget.level <= currentAttack.damageLevel:
                        currentTarget.alive = False
                        attackSuccess = attacked = True
                        ssprint(f'<Eliminated {currentTarget.name}.>')
                    else:
                        ssprint(f"<{currentTarget.name} level too for that attack.>")
                        attacked = True
                else:
                    ssprint(f'<<Warning,{currentTarget.name} has resistance to {currentAttack.damageType}.>>')
                    attacked = True

        return attacked, attackSuccess


    # ========== Attribute Functions
    def attributes_generator(self, character=None, output=False):
        '''
        Yields character's attributes (skills/resistances).

        Args:
            character (bool=None):
                Specifies character to get attributes from, default is Rimuru (player).

            output (bool=False):
                Yields friendly string for in game printing.

        Usage:
            .attributes_generator('ranga', True)
        '''

        character = self.attributes

        # Specify character other than Rimuru.
        if target:
            character = target.attributes

        for skillType, skills in character.items():
            if output and skills: 
                # Prints out skill category (Ultimate, Unique, etc) type also for printing in game.
                yield f'{skillType}:' 
            for skillName, skillObject in skills.items():
                if output:
                    if skillObject.active:
                        yield f'\t{skillName} (Active)'
                    elif skillObject.passive:
                        yield f'\t{skillName} (Passive)'
                    else:
                        yield f'\t{skillName}'
                else:
                    yield skillObject

    def show_attributes(self, character=None):
        '''
        Shows character's attributes if data is available.

        Args:
            character (str=None):
                Character's attributes to show.

        Usage:
            .show_attributes('tempest serpent')

            > stats
            > stats tempest serpent
        '''

        # If no character was specified, use rimuru (player)
        if not character:
            character = rimuru
            # If currently using Mimic, will show mimicked character's attributes also.
            showMimic = True
        else:
            showMimic = False
            try:
                character = self.get_object(character, mimic=True)
            except: pass

        print(f"""
-----Attributes/Skills-----
Name: {character.name} {character.familyName}
""")
        for i in self.attributes_generator(character, output=True):
            print(i)

        # Only shows mimicry info when not looking at stats of other monsters and is currently using mimicry
        if self.mimicObject and showMimic:
            print("\n\t-----Mimicry-----")
            print(f"\tMimicking: {self.mimicking}\n")
            for j in self.attributes_generator(self.mimicObject, True):
                print(f'\t{j}')

    def add_attributes(self, attribute, show_msg=True):
        '''
        Adds attribute to character.

        Args:
            attribute (str):
                Attribute to add to character.

            show_msg (bool=True):
                Shows attribute's info and acquired msg.

        Usage:
            .add_attributes('rimuru', 'water blade')
        '''

        attribute = self.get_object(attribute, new=True)
        if attribute:
            if not check_mob_has(attribute):
                self.attributes[attribute.skillLevel][attribute.name] = attribute
                if show_acquired_msg:
                    try:
                        ssprint(attribute.acquiredMsg)
                    except: pass
                if show_info: 
                    self.show_info(attribute.name)  # Shows skill info

    def remove_attributes(self, attribute):
        '''
        Removes attribute.
        
        Args:
            attribute (str):
                Attribute to remove.

        Usage:
            .remove_attribute('resist poison')
        '''

        try:
            attribute = self.get_object(attribute)
            del self.attributes[attribute.attributeLevel][attribute.name]
        except:
            print("ERROR Deleting attribute. If you're seeing this message, please let developer know")

    def skill_upgrade(self, skill_from, skill_to):
        '''
        Upgrades skill.

        Args:
            skill_from (str):

            skill_to (str):

        Usage:
            .skill_upgrade(skill_from, skill_to)
        '''

        try:
            skill_from = self.get_object(skill_from)
            skill_to = self.get_object(skill_to, new=True)
            self.remove_attributes(skill_from)
            ssprint(f'<<{skill_from.skillLevel} [{skill_from}] evolving to {skill_to.skillLevel} [{skill_to}]...>>')
            self.add_attributes(skill_to)
        except:
            ssprint("<Error upgrading skill>")


    # ========== Inventory Functions
    def inventory_generator(self, output=False):
        '''
        Yields all items in character's inventory (Currently only Rimuru).

        Args:
            output (bool=False):
                Yields a friendly string for printing in game purposes.

        Usage:
            .inventory_generator(output=True)
        '''
        for itemType, items in self.inventory.items():
            if output and items:
                yield f'{itemType}:'  # If output=True prints out itemType also
            for itemName, itemObject in items.items():
                if output:
                    yield f'\t{self.inventory[itemType][itemName].amount}x {itemObject.name}'
                else:
                    yield itemObject

    def show_inventory(self, character=None):
        '''
        Prints out inventory items, corresponding category, and capacity.

        Args:
            character (str):
                Specify which character's inventory to show.

        Usage:
            .show_inventory('gobta')

            > inv
        '''

        print('\n-----Inventory-----')
        print(f'Capacity: {self.inventoryCapacity}%\n')
        for i in self.inventory_generator(output=True): 
            print(i)  # Prints out inventory items

    def add_inventory(self, item):
        '''
        Adds item to character (currently only Rimuru) inventory.

        Args:
            item (str):
                Item to add to inventory.

        Usage:
            .add_inventory('hipokte grass')
        '''

        item = self.get_object(item, new=True)
        if item:
            self.inventory[item.itemType][item.name] = item
            self.inventory[item.itemType][item.name].amount += item.addAmount
            ssprint(f'<<Analysis on {item.name} successful.>>')
            self.show_info(item)

            self.inventoryCapacity += item.capacityUse
            ssprint(item.AcquiredMsg() + f' | Total: {self.inventory[item.itemType][item.name].amount}>')
            ssprint(f'<Inventory Capacity: {self.inventoryCapacity:.2f}%>')

    def remove_inventory(self, item):
        '''
        Remove item from inventory (Currently only Rimuru).

        Args:
            item (str):
                Item to remove from inventory.

        Usage:
            .remove_inventory('hipokte grass')
        '''

        try:
            self.inventory[item.itemType].remove(item)
        except:
            ssprint('<Failed removing item from inventory.>')


    # ========== Subordinates
    def subordinates_generator(self, character):
        '''
        Yields the subordinates under specified character.
        '''
        pass

    def add_sub(self, name, character):
        '''
        Naming subordinates and give blessing.

        Args:
            name (str):
                Set name to new subordinates.

            character (str):
                Character name or object to be named.

        Usage:
            .add_sub('Tempest Wolf', 'Ranga')
        '''

        char = self.get_object(character, sub=True)
        char.name = name
        char.blessing = self.giveBlessing
        if char.species in self.subs:
            self.subs[char.species].append(char)
        else:
            self.subs[char.species] = list([char])

# ========== Rimuru
rimuru = None
def update_character(character):
    global rimuru
    rimuru = character
    return rimuru
