class Subordinates:
    def subordinates_generator(self):
        """
        Yields the subordinates under specified character.

        Usage:
            .subordinates_generator('milim')
        """

        for level, sub_list in self.subordinates.items():
            for subordinate in sub_list: yield subordinate

    def add_subordinate(self, new_subordinate, new_name):
        """
        Naming subordinates and give protections.

        Args:
            new_subordinate str: Character name or object to be named.
            new_name str: Set name to new subordinates.

        Usage:
            .add_subordinates('Tempest Wolf', 'Ranga')
        """

        new_subordinate = self.get_object(new_subordinate, sub=True)
        new_subordinate(new_name)
        new_subordinate.protections += self.shared_protection

        if new_subordinate.species in self.subordinates:
            self.subordinates[new_subordinate.species].append(new_subordinate)
        else: self.subordinates[new_subordinate.species] = [new_subordinate]
