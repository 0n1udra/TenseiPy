from game_files.extra import format_info

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

        # Checks to see if any acquired mimics has inputted ability to get info on.
        if game_object := self.get_object(game_object):
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

        info_dict = {'Title': self.title, 'Species': self.species, 'Rank': self.rank, 'Divine Protection': self.blessing,
                     'Affiliations': self.affiliations, 'Occupations': self.occupations, 'Abilities': self.abilities,
                     '*Description': self.description, '*Appearance': self.appearance}
        for k, v in info_dict.items():
            if formatted_info := format_info(k, v):
                self.info_page += f"    {formatted_info}\n"

    def update_ranking(self, level):
        """
        Updates character ranking.

        Args:
            level: New level for character.

        Usage:
            character_object.update_ranking('A+')
        """

        self.level = level
        self.update_info()
        print(f"    < Leveled Up {self.name} >>> {level} >")

    def check_if_player(self):
        """Checks if you're interacting with the player object (Rimuru)."""

        if self.__class__.__name__ == 'Rimuru_Tempest': return True
