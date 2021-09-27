from game_files.output import gprint, print_header

class Subordinates:
    def subordinates_generator(self, output_mode=False):
        """
        Yields the subordinates under specified character.

        Usage:
            .subordinates_generator('milim')
        """

        for mob_rank, sub_list in self.subordinates.items():
            if output_mode and sub_list: yield f'    {mob_rank}:'

            for subordinate in sub_list:
                if output_mode:
                    yield f'        {subordinate.name}'
                else: yield subordinate

    def show_subordinates(self, *args):
        """Lists subordinates by species."""

        print_header('Subordinates')
        print(f'    Master: {self.name}\n')
        for i in self.subordinates_generator(output_mode=True): print(i)

    def get_subordinate(self, name, use_canon_name=False):
        """
        Get's character object from subordinates dictionary either from anme or from canon name.

        Args:
            name (str): Name of character.
            use_canon_name (bool

        """

        for mob in self.subordinates_generator():
            if use_canon_name:
                if name.lower() in mob.canon_name.lower(): return mob
            else:
                if name.lower() in mob.name.lower(): return mob

    def add_subordinate(self, game_character, canon_name=None, new_name=None, level=None):
        """
        Naming subordinates and give protections.

        Args:
            new_subordinate str: Character name or game object to be named.
            canon_name str(None): Allow user press enter once to use default name from story.
            new_name str(None): Set name to new subordinates.
            level int(None): Set character's rank status post evolution.

        Usage:
            .add_subordinates('Tempest Wolf', 'Ranga')
        """

        # Asks player to set name, if nothing, uses canon name (story accurate name).
        if not new_name:
            while True:
                if new_name := str(input(f"\nChoose name or Enter for default ({canon_name}) > " if canon_name else "Set name > ")).strip():
                    if new_name.isalnum(): break
                # Let's user use default canon name for new subordinate. Requires canon_name argument.
                elif canon_name:
                    new_name = canon_name
                    break
        new_name = new_name.capitalize()

        # Get's game character object and sets relavant variables.
        new_subordinate = self.get_object(game_character, new=True)(new_name)
        new_subordinate.protections.append(self.shared_protection)
        new_subordinate.canon_name = canon_name
        if level: new_subordinate.level = level

        if new_subordinate.species in self.subordinates:
            self.subordinates[new_subordinate.species].append(new_subordinate)
        else: self.subordinates[new_subordinate.species] = [new_subordinate]

        gprint(f"< New Subordinate: {new_name} >")
