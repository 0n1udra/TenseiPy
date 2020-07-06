

def ssprint(Msg):
    print(f'    {Msg}\n')


class Info:
    def __init__(self):
        self.name = 'N/A'
        self.family_name = ''
        self.title = 'N/A'
        self.species = 'N/A'
        self.rank = 'N/A'
        self.level = 1
        self.blessing = 'N/A'
        self.shared_blessing = 'N/A'
        self.info = 'N/A'
        self.appearance = 'N/A'
        self.description = 'N/A'
        self.alive = True
        self.evolution = ''
        self.info = ''

    def get_name(self):
        """Returns object name attribute in lowercase."""

        return self.name.lower()

    def update_info(self):
        """Updates character information."""

        self.info = f"""
        Name: {self.name} {self.family_name}
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

    def show_info(self, game_object):
        """
        Shows corresponding information for object.

        Args:
            game_object: Game object that you want to get information on.

        Usage:
            > info predator
            > info tempest serpent
        """

        try:
            print(self.get_object(game_object).info)
        except:
            ssprint("<No available data.>")

    def update_ranking(self, character, level):
        """
        Updates character ranking.

        Args:
            character: Character to level up.
            level: New level for character.

        Usage:
            .update_ranking('rimuru', 'A+')
        """

        char = self.get_object(character)
        if char:
            char.level = level
            self.Data.update_info()
            ssprint(f"<{char} rank up to {level}>")
