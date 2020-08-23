
class Map:

    def __init__(self):
        self.available_locations = []
        self.current_location = None

    def get_location(self, character=None):
        character = self.get_object(character)

        if not character:
            character = self

        if hasattr(character, 'current_location'):
            if hasattr(character.current_location, '__locaton_name'):
                print(f"    < {character.name} located at {character.current_location.__location_name}. >")

    def get_map(self, location=None):
        print("map")

    def update_location(self,new_location=None, character=None):
        character = self.get_object(character)

        if not character:
            character = self

        if character:
            character.current_location = new_location
