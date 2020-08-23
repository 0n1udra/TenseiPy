
class Subordinates:
    def subordinates_generator(self, character=None):
        """
        Yields the subordinates under specified character.

        Args:
            character: Character to get subordinates from.

        Usage:
            .subordinates_generator('milim')
        """

        for level, sub_list in self.subordinates.items():
            for subordinate in sub_list:
                yield subordinate

    def add_subordinate(self, new_subordinate, new_name):
        """
        Naming subordinates and give blessing.

        Args:
            new_subordinate: Character name or object to be named.
            new_name: Set name to new subordinates.

        Usage:
            .add_subordinates('Tempest Wolf', 'Ranga')
        """

        new_subordinate = self.get_object(new_subordinate, sub=True)
        new_subordinate.name = new_name

        new_subordinate.blessing = self.shared_blessing
        if new_subordinate.species in self.subordinates:
            self.subordinates[new_subordinate.species].append(new_subordinate)
        else:
            self.subordinates[new_subordinate.species] = list([new_subordinate])
