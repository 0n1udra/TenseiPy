class Map:
    def get_location(self, character=None, level_class=None):
        character = self.get_object(character)
        if not character: character = self

        # Looks for variable names that has __location_name in it, then uses eval to get the location variable data.
        try:
            location_name_index = [i for i, s in enumerate(dir(level_class)) if 'location_name' in s][0]
        except:
            location = 'N/A'
        else:
            location = eval(f'level_class.{dir(level_class)[location_name_index]}')

        if character:
            print(f"    < {character.name} location: {location}. >")
            character.update_location(location)


    def get_map(self, location=None):
        print("map")

    def update_location(self, new_location=None, character=None):
        character = self.get_object(character)

        if not character: character = self
        if character: character.current_location = new_location
