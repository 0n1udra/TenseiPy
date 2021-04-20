from game_files.output import gprint

class Map:
    def show_nearby(self, *args, valid_usage=False):
        # Either you have to own [Magic Perception] or change the valid_usage boolean to use this funtion.
        if not valid_usage and not self.check_acquired('magic perception'): return

        print("    ----- Nearby -----")
        for mob in self.active_mobs:
            print(f"    {mob[1]}x {mob[0].name} {'(Dead)' if mob[0].status else ''}")

    def add_played_action(self,  played_action):
        """
        Able to check what actions player has taken so far by adding action's class name to tuple.

        Args:
            played_action str: String parsed from game_action function.
        """

        if played_action in self.played_actions:
            self.played_actions[played_action] += 1
        else: self.played_actions[played_action] = 1

    @staticmethod
    def get_location_variable(level_class=None):
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
        gprint(f"\n< {self.name} location: {self.current_location} >\n")
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
