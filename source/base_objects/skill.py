from game_files.extra import format_info
from game_files.output import gprint

class Skill:
    name = 'N/A'
    type = 'Activatable Skill'
    skill_level = 'Skill'
    damage_level = 1
    damage_type = ''
    info_page = ''
    description = ''
    evolution = ''
    abilities = ''
    acquired_msg = ''
    status = ''
    use_requirements = {}
    quantity = 0
    predate_copy = True  # Able to copy ability by using analysis, predate, etc.
    sub_skills = {}
    object_type = 'attribute'
    initialized = False

    def __init__(self, quantity=0):
        self.use_requirements, self.sub_skills = self.use_requirements, self.use_requirements
        self.quantity = quantity
        self.initialized = True
        self.update_info()

    def __str__(self):
        return self.name.lower()

    def meet_requirements(self, user):
        """
        Checks if user meets prerequisite requirements to use skill.

        Args:
            user obj: Character object that is using skill.

        Returns:
            bool: If user meets requirements or not.
        """

        if self.use_requirements:
            # Check if user meets requirement or own prerequisites before using skill.
            for k, v in self.use_requirements.items():
                if not user.check_acquired(k, v):
                    gprint(f"< Skill Requires: {v}x {k} >")
                    return False
        return True

    def expend_requirements(self, user):
        """
        Expends (uses up) items/etc to activate skill.

        Args:
            user obj: Character object that is using skill.

        Returns:
            bool: If successfully expended requirements.
        """

        if not self.meet_requirements(user): return False

        # TODO Make it so skill can use up items or just need to own them but don't use them up (remove them).
        for k, v in self.use_requirements.items():
            user.remove_inventory(k, v)
        return True

    def use(self, user, *args):
        """
        Use skill, by default it'll just return True to signal player has used the skill.

        Args:
            user obj: Game character object of skill activator.

        Returns:
            bool: By default will return True to signal usage, if function not overwritten.
        """

        self.expend_requirements(user)
        return True

    def activate_skill(self, state='Active'):
        """Activates skill, then updates relevant variables."""

        if state.lower() in self.status: return  # If skill is already at that state.

        gprint(f"< {self.skill_level} {self.name}: {state} >")
        self.status = state
        self.update_info()

    def deactivate_skill(self, state=''):
        """Deactivates skill, then updates relevant variables."""

        gprint(f"< {self.skill_level} {self.name}: Deactivated >")
        self.status = state
        self.update_info()

    def show_acquired_msg(self):
        """Print skill's acquired message."""

        print(f"    {self.acquired_msg}")

    def update_info(self):
        """Updates skills info_page depending on what object variables has been set."""

        self.acquired_msg = f"<< Acquired {self.skill_level} [{self.name}] successfully. >>"

        self.info_page = f'    Name: [{self.name}] {"(" + self.status + ")" if self.status else ""}\n'

        # Only show fields that have set data.
        info_dict = {'Type': self.type, 'Level': self.skill_level, 'Damage': self.damage_level, 'Damage Type': self.damage_type,
                     'Evolution': self.evolution, '*Description': self.description, '*Abilities': self.abilities}

        for k, v in info_dict.items():
            if formatted_info := format_info(k, v):
                self.info_page += f"    {formatted_info}\n"

        if self.use_requirements:
            self.info_page += "\n    Use Requirements:\n"
            for item, amount in self.use_requirements.items():
                self.info_page += f"        {amount}x [{item}]\n"

