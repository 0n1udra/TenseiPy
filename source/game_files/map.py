class Map:
    @staticmethod
    def get_location_variable(self, level_class=None):
        """
        Gets location name from __location var in current level's class object.
        Args:
            level_class obj: Class object that contains __location variable.

        Returns:
            None: If no location found.
            str: location name.
        """

        if level_class is None: return None

        # Looks for variable names that has __location in it, then uses eval to get the location variable data.
        for function_name in dir(level_class):
            if 'location' in function_name:
                return eval(f"level_class.{function_name}")

    def get_location(self, *args):
        """
        Prints and returns character's current location.

        Returns
            str: Name of location or N/A if unknown.

        """

        # TODO Separate this function into two.
        print(f"\n    < {self.name} location: {self.current_location} >\n")
        return self.current_location

    def get_map(self, level):
        pass

    def update_location(self, new_location=None):
        """
        Updates character current_location variable.

        Args:
            new_location str: Location name
        """

        if not new_location: return False
        self.current_location = new_location
