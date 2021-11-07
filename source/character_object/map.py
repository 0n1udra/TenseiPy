from game_files.output import gprint, print_header

class Map:
    def show_nearby(self, *args, force_usage=False):
        """
        Prints out nearby mobs.

        Args:
            *args: Catch all.
            force_usage bool(False): Usually this can only be used through specific in-game [Skills], this can bypass that.
        """

        # Either you have to own [Magic Sense] skill or change the force_usage boolean to use this function.
        if not force_usage and not self.check_acquired('magic sense'): return

        print_header('NEARBY', 10)
        for mob in self.active_mobs:
            print(f"    {mob[1]}x {mob[0].name} (lvl {mob[0].level}) {'(Dead)' if mob[0].status else ''}")

    def add_action_played(self,  action_played):
        """
        Able to check what actions player has taken so far by adding action's class name to tuple.

        Args:
            action_played str: String parsed from game_action function.
        """

        if action_played in self.actions_played:
            self.actions_played[action_played][0] += 1
        else: self.actions_played[action_played] = [1, None]

    @staticmethod
    def get_location_variable(level_class=None):
        """
        Gets location name from __location var in current level's class object.
        Args:
            level_class obj(None): Class object that contains __location variable.

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
        Prints and returns player's current location.

        Returns
            str: Name of location or N/A if unknown.
        """

        gprint(f"< {self.name} location: {self.current_location} >\n")
        return self.current_location

    def update_location(self, new_location=None):
        """
        Updates character's current_location variable.

        Args:
            new_location str(None): Location name
        """

        if not new_location: return False
        self.current_location = new_location
