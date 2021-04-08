from game_files.extra import format_info, get_any

class Info:
    def show_info(self, game_object):
        """
        Shows corresponding information for object.

        Args:
            game_object: Game object that you want to get information on.

        Usage:
            > info predator
            > info tempest serpent
        """

        # Need this so player can get the info page on itself.
        if get_any(game_object, ['me', 'self', 'player', self.name]):
            print(self.info_page)
            return True

        if game_object := self.get_object(game_object, mimic_pool=True):
            # Some skills or objects have special info pages, I couldn't get @property method working...
            if hasattr(game_object, 'show_info_page'):
                print(game_object.show_info_page(self))
            else:
                print(game_object.info_page)

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
                     'Location': self.current_location, '*Description': self.description, '*Appearance': self.appearance}

        for k, v in info_dict.items():
            if formatted_info := format_info(k, v):
                self.info_page += f"    {formatted_info}\n"

    def update_name(self, name):
        """Updates name of character."""

        self.name = name
        self.update_info()

    def update_lname(self, name):
        """Update character's family name (last name)."""

        self.family_name = name
        self.update_info()

    def update_level(self, level):
        """
        Updates character level.

        Args:
            level int: New level for character.

        Usage:
            character_object.update_level(10)
        """

        self.level = level
        self.update_info()
        print(f"    < [{self.name}] Level Up: {level} >\n")

    def add_protection(self, divine_protection):
        """
        Adds divine protection to character.

        List:
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

    def show_standings(self):
        print("-----Standings-----")
        for k, v in self.standings.items():
            print(f"{k}: {v}")
        print()

    def update_standing(self, match, new_value=1):
        """
        Updates player standing/reputation.

        Args:
            match str: Character/faction/etc to update.
            new_value int(1): Increase or decrease standing. Pass in either positive or negative integer.

        Usage:
            rimuru.update_standing('veldora', 2)
            rimuru.update_standing('gobta', -1)
        """

        match = match.capitalize()
        for k, v in self.standings.items():
            if k in match:
                self.standings[k] += new_value

        # Create dictionary item if for loop found no match.
        self.standings[match] = new_value
        print(f"    < {match} Standing: {self.standings[match]} >")

    def get_standing(self, match, value=1):
        """
        Returns integer value of standing that player has with a character/faction/etc.

        Args:
            match str: Name of character/faction/etc to check standing with.

        Returns:
            int: Returns integer denoting reputation player has with specified.
        """

        for k, v in self.standings.items():
            if k in match.capitalize():
                return self.standings[k]

    def check_if_player(self):
        """Checks if you're interacting with the player object (Rimuru)."""

        if self.__class__.__name__ == 'Rimuru_Tempest': return True
