import skills, items

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

        generators = [*self.get_attributes(), *self.get_inventory(), *self.subordinate_generator()]



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
            generators.extend(self.get_attributes(rimuru.mimicObject))
        
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

    def add_sub(self, name, character):
        '''
        Naming subordinates and give blessing.

        Args:
            name (str):
                Set name to new subordinates.

            character (str):
                Character name or object to be named.

        Usage:
            add_sub('Tempest Wolf', 'Ranga')

        '''

        char = self.get_object(character, sub=True)
        char.name = name
        char.blessing = self.giveBlessing
        if char.species in self.subs:
            self.subs[char.species].append(char)
        else:
            self.subs[char.species] = list([char])

    def run_start_state(self):
        '''Adds corresponding starter attributes and items to character.'''

        for i in self.startState:
            self.add_attributes(i, showInfo=False, output=False)

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
            update_ranking('rimuru', 'A+')
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
            check_mob_has('rimuru', 'resist poison')
            > rimuru has resist melee
            >>True
        '''
        try:
            self.get_object(character).

    def use_skill(self, character, skill):
        '''
        Use skill that character has.

        Args:
            character (str):
                Character to use specified skill.

            skill (str):
                Skill to use by specified character.

        Usage:
            use_skill('rimuru', 'magic perception')
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
    def check_resistance(self, character, attack):
        # Checks if character has resistance attribute
        for resistName, resistObject in character.attributes['Resistance'].items():
            for resist in resistObject.resistTypes:
                if resist.lower() == attack.lower():
                    return True
                    break

    def can_attack(self, usrInput, rimuru=False):
        targets, attacks = self.focusTargets, []
        try:
            splitInput = usrInput.split(',')
        except:
            splitInput = usrInput

        for i in self.currentMobs:
            if i.get_name() in usrInput and i.alive:
                targets.add(i)
                self.focusTargets.add(i)

        for i in splitInput:
            skill = self.get_object(i)
            if skill:
                if skill.GetName() in i.lower() and skill.objectType == 'skill':
                    attacks.append(self.get_object(skill))

        if 'rimuru' in usrInput:
            targets.add(rimuru)

        attacked = attackSuccess = False

        for currentTarget in targets:
            for currentAttack in attacks:
                if not self.check_resistance(currentTarget, currentAttack.damageType):
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
    def get_attributes(self, target=None, output=False):
        character = self.attributes
        if target:
            character = target.attributes  # If no specified character

        for skillType, skills in character.items():
            if output and skills:
                yield f'{skillType}:'  # If output=True prints out skillType
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
        if not character:
            character, showMimic = rimuru, True
        else:
            showMimic = False
            # Get stats for other monsters
            try:
                character = self.get_object(character, True)
            except: pass

        print(f"""
-----Attributes/Skills-----
Name: {character.name} {character.familyName}
""")
        for i in self.get_attributes(character, output=True):
            print(i)

        # Only shows mimicry info when not looking at stats of other monsters or in mimicry
        if self.mimicObject and showMimic:
            print("\n\t-----Mimicry-----")
            print(f"\tMimicking: {self.mimicking}\n")
            for j in self.get_attributes(self.mimicObject, True):
                print(f'\t{j}')

    def add_attributes(self, item, showInfo=False, output=True):
        item = self.get_object(item, new=True)
        try:
            self.attributes[item.skillLevel][item.name]
        except:
            if item:
                self.attributes[item.skillLevel][item.name] = item
                if output:
                    try:
                        ssprint(item.acquiredMsg)
                    except: pass
                if showInfo: 
                    self.show_info(item.name)  # Shows skill info

    def remove_attributes(self, skill):
        print(skill)
        try:
            skill = self.get_object(skill)
            del self.attributes[skill.skillLevel][skill.name]
        except:
            print("ERROR Deleting attribute. If you're seeing this message, please let developer know")

    def skill_upgrade(self, skillFrom, skillTo):
        try:
            skillFrom = self.get_object(skillFrom)
            skillTo = self.get_object(skillTo, new=True)
            self.remove_attributes(skillFrom)
            ssprint(f'<<{skillFrom.skillLevel} [{skillFrom}] evolving to {skillTo.skillLevel} [{skillTo}]...>>')
            self.add_attributes(skillTo)
        except:
            ssprint("<Error upgrading skill>")

    # ========== Inventory Functions
    def get_inventory(self, output=False):
        for itemType, items in self.inventory.items():
            if output and items:
                yield f'{itemType}:'  # If output=True prints out itemType also
            for itemName, itemObject in items.items():
                if output:
                    yield f'\t{self.inventory[itemType][itemName].amount}x {itemObject.name}'
                else:
                    yield itemObject

    def show_inventory(self, character=None):
        print('\n-----Inventory-----')
        print(f'Capacity: {self.inventoryCapacity}%\n')
        for i in self.get_inventory(True): print(i)  # Prints out inventory items

    def add_inventory(self, item):
            #item = self.get_object(item)
            #self.inventory[item.itemType][item.name].amount += item.addAmount
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
        try:
            self.inventory[item.itemType].remove(item)
        except:
            ssprint(f'<Error deleting {item.name} from inventory>')


# ========== Rimuru
rimuru = None
def update_character(character):
    global rimuru
    rimuru = character
    return rimuru
