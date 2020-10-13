class Map:
    def get_location_variable(self, level_class=None):
        # Looks for variable names that has __location in it, then uses eval to get the location variable data.
        if level_class is None: return None

        for function_name in dir(level_class):
            if 'location' in function_name:
                return eval(f"level_class.{function_name}")

    def get_location(self):
        print(f"    < {self.name} location: {self.current_location}. >")
        return self.current_location

    def get_map(self, location=None):
        print("map")

    def update_location(self, new_location=None):
        if not new_location: return False
        self.current_location = new_location
