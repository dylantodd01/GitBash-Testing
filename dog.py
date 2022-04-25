class Dog:
	"""A Simple Attempt To Model A Dog"""

	def __init__(self, name, age):
		"""Initialise Name And Age Attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate A Dog Sitting In Response To A Command"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate A Rolling Over In Response To A Command"""
		print(f"{self.name} rolled over!")

my_dog_1 = Dog("Amalie", 5)
my_dog_2 = Dog("Hugo", 2)

print(f"My dog's name is {my_dog_1.name}.")
print(f"My dog is {my_dog_1.age} years old.")
my_dog_1.sit()
my_dog_1.roll_over()

print(f"My other dog's name is {my_dog_2.name}.")
print(f"My other dog is {my_dog_2.age} years old.")
my_dog_2.sit()