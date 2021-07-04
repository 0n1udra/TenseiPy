from game_files.extra import format_info, get_any
from game_files.output import print_header

class Info:
    def show_info(self, game_object):
        """
        Shows info page.

        Args:
            game_object str: skill/item/mob/etc.

        Usage:
            > info predator
            > info hipokte grass
            > info tempest serpent
            > info gobta
        """

        # Need this so player can get the info page on itself.
        if get_any(game_object, ['me', 'self', 'player', self.name]):
            print(self.info_page)
            return True

        if game_object := self.get_object(game_object, mimic_pool=True, sub_pool=True):
            # Some skills or objects have special info pages, I couldn't get @property method working...
            if hasattr(game_object, 'show_info_page'):
                print(game_object.show_info_page(self))
            else: print(game_object.info_page)

    def update_info(self):
        """Updates character information."""

        # Sets ranking according to level.
        ranking = ['F', 'E', 'D', 'C', 'B', 'A-', 'A', 'A+', 'Special A', 'S', 'Special S']
        self.rank = ranking[self.level - 1]

        # Need this complex line because I don't want a weird space or formatting if character doesnt have a last name.
        self.info_page = f'    Name: [{self.name}{" " + self.family_name if self.family_name else ""}] {"(" + self.status + ")" if self.status else ""}\n'

        # Only show fields that have set data.
        info_dict = {'Title': self.title, 'Species': self.species, 'Rank': self.rank, 'Level': self.level, 'Blessing': self.protections,
                     'Affiliations': self.affiliations, 'Occupations': self.occupations, 'Abilities': self.abilities,
                     'Location': self.current_location, '*Description': self.description, '*Appearance': self.appearance, '*Evolution': self.evolution}

        for k, v in info_dict.items():
            if formatted_info := format_info(k, v):
                self.info_page += f"    {formatted_info}\n"

    def set_name(self, name):
        """Updates name of character."""

        self.name = name
        self.update_info()  # Need this to update the info in info_page variable.

    def set_lname(self, name):
        """Update character's family name (last name)."""

        self.family_name = name
        self.update_info()

    def add_level(self, add_amount=1):
        """
        Add x levels to character's level.

        Args:
            add_amount int(1): To be added to current level.
        """

        print(f"    < [{self.name}] Level Up: {self.level} to {self.level + add_amount}>\n")
        self.level += add_amount
        self.update_info()

    def set_level(self, level):
        """
        Set character level.

        Args:
            level int: New level for character.

        Usage:
            character_object.update_level(10)
        """

        self.level = level
        self.update_info()
        print(f"    < [{self.name}] Level: {level} >\n")

    def add_protection(self, divine_protection):
        """
        Adds divine protection to character.

        Protections:
        Storm Crest: Veldora to Rimuru
        Protection of Tempest: Rimuru to subs
        Protection of the Storm: True Dragons, Veldora, etc
        Divine Protection of the Labyrinth: Ramiris to subs
        Divine Protection of the Great Demon Lord: Demon Lord to subs
        Protection of The White Ice: Velzado
        """

        self.protections.append(divine_protection)
        self.update_info()
        print(f'    < [{self.name}] Acquired Blessing: [{divine_protection}] >')

    def show_reputations(self, *args):
        """Shows player's reputation (standing) with factions/characters."""

        print_header('Reputation')
        for k, v in self.reputations.items(): print(f"    {k}: {v}")

    def add_reputation(self, faction_name, add_value=1):
        """
        Adds to player standing/reputation.

        Args:
            faction_name str: Character/faction/etc to update.
            add_value int(1): Increase or decrease reputations. Pass in either positive or negative integer.

        Usage:
            rimuru.add_reputation('veldora', 2)
            rimuru.add_reputation('gobta', -1)
        """

        faction_name = faction_name.capitalize()
        # Checks if already have repudiation with faction.
        for k, v in self.reputations.items():
            if k in faction_name:
                print(f"\n    < [{faction_name}] Reputation Update: {self.reputations[k]} to {self.reputations[k] + add_value} >\n")
                self.reputations[k] += add_value
                return self.reputations[k]  # Returns new value of reputation standing.

        # Adds new faction to reputations list.
        self.reputations[faction_name] = add_value
        print(f"\n    < [{faction_name}] New Reputation: {self.reputations[faction_name]} >")

    def get_reputations(self, faction_name):
        """
        Returns integer value of reputation that player has with a character/faction/etc.

        Args:
            faction_name str: Name of character/faction/etc to check reputation with.

        Returns:
            int: Returns integer denoting reputation player has with specified.
        """

        for k, v in self.reputations.items():
            if k in faction_name.capitalize(): return self.reputations[k]

    def check_if_player(self):
        """Checks if you're interacting with the player object (Rimuru)."""

        if self.__class__.__name__ == 'Rimuru_Tempest': return True
