class Info:
    def __init__(self):
        self.name = 'N/A'
        self.family_name = ''
        self.canon_name = 'N/A'
        self.title = 'N/A'
        self.blessing = 'N/A'
        self.shared_blessing = 'N/A'
        self.species = 'N/A'
        self.rank = 'N/A'
        self.level = 1
        self.info = 'N/A'
        self.description = 'N/A'
        self.appearance = 'N/A'
        self.evolution = ''
        self.acquired_msg = ''
        self.alive = True

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
        for i in self.mimic_generator():
            try:
                print(i.get_object(game_object).info)
            except:
                pass
        try:
            print(self.get_object(game_object, mimic=True).info)
        except:
            pass


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

    def update_ranking(self, level, character=None):
        """
        Updates character ranking.

        Args:
            character: Character to level up.
            level: New level for character.

        Usage:
            .update_ranking('A+')
            .update_ranking('A+', 'ranga')
        """

        character = self
        if character:
            character.level = level
            self.update_info()
            print(f"    <{character.name} leveled up to {level}>")

    def show_acquired_msg(self):
        """Shows acquired message."""

        print(f'    {self.acquired_msg}')
