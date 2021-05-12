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

        print('    <<<<<<<<<< Subordinates >>>>>>>>>>\n')
        print(f'    Leader: {self.name}\n')
        for i in self.subordinates_generator(output=True): print(i)
        print('\n    <<<<<<<<<< Subordinates >>>>>>>>>>')

    def add_subordinate(self, new_subordinate, new_name):
        """
        Naming subordinates and give protections.

        Args:
            new_subordinate str: Character name or object to be named.
            new_name str: Set name to new subordinates.

        Usage:
            .add_subordinates('Tempest Wolf', 'Ranga')
        """

        # Get's game character object, initializes it, sets name, then adds protection(s) (blessing).
        new_subordinate = self.get_object(new_subordinate, new=True)(new_name)
        new_subordinate.protections.append(self.shared_protection)

        if new_subordinate.species in self.subordinates:
            self.subordinates[new_subordinate.species].append(new_subordinate)
        else: self.subordinates[new_subordinate.species] = [new_subordinate]
