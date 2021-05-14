from game_files.output import gprint, print_header

class Subordinates:
    def subordinates_generator(self, output=False):
        """
        Yields the subordinates under specified character.

        Usage:
            .subordinates_generator('milim')
        """

        for level, sub_list in self.subordinates.items():
            if output and sub_list: yield f'    {level}:'

            for subordinate in sub_list:
                if output:
                    yield f'        {subordinate.name}'
                else: yield subordinate

    def show_subordinates(self, *args):

        print_header('Subordinates')
        print(f'    Master: {self.name}\n')
        for i in self.subordinates_generator(output=True): print(i)

    def add_subordinate(self, new_subordinate, canon_name=None, new_name=None):
        """
        Naming subordinates and give protections.

        Args:
            new_subordinate str: Character name or game object to be named.
            canon_name str(None): Allow user press enter once to use default name from story.
            new_name str(None): Set name to new subordinates.

        Usage:
            .add_subordinates('Tempest Wolf', 'Ranga')
        """

        # Asks player to set name, if nothing, uses canon name (story accurate name).
        if not new_name:
            while True:
                if new_name := str(input(f"\nChoose name or Enter for default ({canon_name}) > " if canon_name else "Set name > ")).strip():
                    if new_name.isalnum(): break
                # If passed in canon_name, if user doesn't type in some alpha-numeric, will use canon_name.
                elif canon_name:
                    new_name = canon_name
                    break

        # Get's game character object, initializes it, sets name, then adds protection(s) (blessing).
        new_subordinate = self.get_object(new_subordinate, new=True)(new_name)
        new_subordinate.protections.append(self.shared_protection)

        if new_subordinate.species in self.subordinates:
            self.subordinates[new_subordinate.species].append(new_subordinate)
        else: self.subordinates[new_subordinate.species] = [new_subordinate]

        gprint(f"\n< New Subordinate: {new_name} >\n")
