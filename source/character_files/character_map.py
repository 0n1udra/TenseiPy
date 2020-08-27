class Map:
    def get_location_name(self, level_class=None):
        # Looks for variable names that has __location in it, then uses eval to get the location variable data.
        try:
            location_name_index = [i for i, s in enumerate(dir(level_class)) if 'location_name' in s][0]
        except: location = 'N/A'
        else:
            location = eval(f'level_class.{dir(level_class)[location_name_index]}')
        return location


    def show_location(self, character=None):
        character = self.get_object(character)
        if not character: return

        print(f"    < {character.name} location: {character.current_location}. >")

    def get_map(self, location=None):
        print("map")

    def update_location(self, new_location=None, character=None):
        character = self.get_object(character)
        if not character: character = self
        if not character: return

        if new_location in 'N/A': return

        character.current_location = new_location
