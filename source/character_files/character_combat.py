class Combat:

	def __init__(self):
		self.current_level_characters = []
		self.focused_targets = set()

	def set_targets(self, targets):
		"""
		Adds c to focused_targets list from user input.

		Separates user inputted targets via ',' then checks to see if mob is in current_level_characters list.
		If so, adds to setTargets list.

		Args:
			targets; String of target(s) to add to focused_targets (list)

		Usage:
			> target tempest serpent, giant bat
		"""

		if 'reset' in targets:
			self.focused_targets.clear()
		else:
			for target in targets.split(','):
				for i in self.current_level_characters:
					if i.get_name() in target:
						self.focused_targets.add(i)
						break

	def attack(self, user_input):
		"""
		Checks if can attack, and if it was successful.

		First separates the targets and attacks via splitting up targets_and_attacks by commas ','.
		Then Adds the targets and attacks to corresponding lists.
		Checks if target is not too high of a level for attack and doesn't have resistance to said attack.
		Will return booleans for if attack was attempted and if attack was successful.

		Args:
			targets_and_attacks: Targets to attack, if multiple, separated by comma ','.

		Returns:
			attacked: If attack was attempted.
			attack_success: If attack was successful.

		Usage:
			.attack('tempest serpent')
			.attack('tempest serpent, giant bat')

			> attack tempest serpent
			> attack tempest serpent, giant bat with water blade
		"""


		attacks = []
		try:
			attacks.append(attacks.split(','))
		except:
			attacks.append(user_input)
		targets = self.focused_targets
		skills = []

		# If mob is in current_level_characters list and is alive, adds to focusTarget list.
		for j in attacks:
			j = self.get_object(j)
			if j != None:
				skills.append(j)

		attack_success = False

		for current_target in targets:
			for current_skill in skills:
				# Checks if target has resistance to current attack.
				if not self.check_resistance(current_skill, current_target):
					# Checks if target is lower level than current attack.
					if current_target.level <= current_skill.damage_level:
						current_target.alive = False
						attack_success = True
						print(f'    <Eliminated {current_target.name}.>\n')
					else:
						print(f"    <{current_target.name} level too for that attack.>")
						attacked = True
				else:
					print(f'    <<Warning,{current_target.name} has resistance to {current_skill.damage_type}.>>')
					attacked = True

		return attack_success
