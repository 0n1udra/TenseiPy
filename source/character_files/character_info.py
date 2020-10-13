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
        game_object = self.get_object(game_object, mimic=True)
        if game_object: print(game_object.info)

    def update_info(self):
        """Updates character information."""

        # Sets ranking according to level
        ranking = ['F', 'E', 'D', 'C', 'B', 'A-', 'A', 'A+', 'Special A', 'S', 'Special S']
        self.rank = ranking[self.level - 1]

        self.info = f"""
        Name: {self.name} {self.family_name}
        Title: {self.title}
        Species: {self.species}
        Rank: {self.rank}
        Divine Protection: {self.blessing}
        Canon Name: {self.canon_name}

        Description:
            {self.description}

        Appearance:
            {self.appearance}
            """

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
        print(f"    < {self.name} leveled up to {level} >")

    def show_acquired_msg(self):
        """Shows acquired message."""

        print(f'\n    {self.acquired_msg}')

    def check_if_player(self):
        """Checks if you're interacting with the player object (Rimuru)."""

        if self.__class__.__name__ == 'Rimuru_Tempest': return True

