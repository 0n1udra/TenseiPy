from game_files.extra import format_info, get_any

class Info:
    def get_name(self):
        """Returns object name attribute in lowercase."""

        return self.name.lower()

    def show_info(self, game_object):
        """
        Shows corresponding information for object.

        Args:
            game_object: Game object that you want to get information on.

        Usage:
            > info predator
            > info tempest serpent
        """

        if get_any(game_object, ['me', 'self', 'player', self.name]):
            print(self.info_page)
            return True

        # Checks to see if any acquired mimics has inputted ability to get info on.
        if game_object := self.get_object(game_object):
            # Some skills or objects have special info pages, I couldn't get @property method working...
            try:
                print(game_object.show_info_page())
                return
            except: pass
            print(game_object.info_page)

    def update_info(self):
        """Updates character information."""

        # Sets ranking according to level
        ranking = ['F', 'E', 'D', 'C', 'B', 'A-', 'A', 'A+', 'Special A', 'S', 'Special S']
        self.rank = ranking[self.level - 1]

        self.info_page = f'    Name: [{self.name}{" " + self.family_name if self.family_name else ""}] {"(" + self.status + ")" if self.status else ""}\n'

        info_dict = {'Title': self.title, 'Species': self.species, 'Rank': self.rank, 'Divine Protections': self.protections,
                     'Affiliations': self.affiliations, 'Occupations': self.occupations, 'Abilities': self.abilities,
                     'Location': self.current_location, '*Description': self.description, '*Appearance': self.appearance}
        for k, v in info_dict.items():
            if formatted_info := format_info(k, v):
                self.info_page += f"    {formatted_info}\n"

    def update_name(self, name):
        self.name = name
        self.update_info()

    def update_lname(self, name):
        self.family_name = name
        self.update_info()

    def update_level(self, level):
        """
        Updates character level

        Args:
            level: New level for character.

        Usage:
            character_object.update_level(10)
        """

        self.level = level
        self.update_info()
        print(f"    < [{self.name}] Level Up: {level} >\n")

    def add_protection(self, divine_protection):
        """Adds divine protection to character.

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
        print(f'    < [{self.name}] Acquired Protection: [{divine_protection}] >')

    def check_if_player(self):
        """Checks if you're interacting with the player object (Rimuru)."""

        if self.__class__.__name__ == 'Rimuru_Tempest': return True
