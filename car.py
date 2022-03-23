"""A class used to describe a car"""

class Car:
	"""A simple attempt to represent a car"""

	def __init__(self, make, model, year):
		"""Initialise car attributes"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def car_name(self):
		"""Return a formatted car name"""
		name = f"{self.year} {self.make} {self.model}"
		print(name.title())

	def read_odometer(self):
		"""Print the car's milage"""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, milage):
		"""Set the milage to the inputted value"""
		if milage >= self.odometer_reading:
			self.odometer_reading = milage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add value to the current milage"""
		self.odometer_reading += miles

	def fuel_up(self):
		"""Print message when filling with fuel"""
		print("Filling up with fuel!")

class Battery:
	"""Modelling an electric car's battery"""

	def __init__(self, battery_size=75):
		"""Initialise the battery attributes"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print battery size"""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the battery range"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		"""Upgrade battery if not already upgraded"""
		if self.battery_size == 75:
			self.battery_size = 100
			print(f"Your battery has been upgraded!")
		else:
			print("Your battery is already fully upgraded!")


class ElectricCar(Car):
	"""Represents electric car specific aspects"""

	def __init__(self, make, model, year):
		"""
		Initialise attributes of parent class
		Also initialising electric car attributes
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

	def fuel_up(self):
		"""Electic cars don't need fuel"""
		print("Electric cars don't use fuel!")
