from time import sleep

class Restaurant:

	def __init__(self, restaurant_name, cuisine_type, opening_time):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.opening_time = opening_time

	def describe_restaurant(self):
		print(f"\nThis restaurant is called {self.restaurant_name}. It serves {self.cuisine_type} cuisine.\nIt opens at {self.opening_time}pm.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
	"""Creating a child class"""
	
	def __init__(self, restaurant_name, cuisine_type, opening_time, flavours):
		super().__init__(restaurant_name, cuisine_type, opening_time)
		self.flavours = flavours

	def describe_flavours(self):
		print("\nOur flavours:\n")
		for flavour in self.flavours:
			print(flavour)

nandos = Restaurant("Nando's", "Portuguese", 6)
pizza_express = Restaurant("Pizza Express", "Italian", 4)
mcdonalds = Restaurant("McDonalds", "Fast Food", 2)
nandos.describe_restaurant()
pizza_express.describe_restaurant()
mcdonalds.describe_restaurant()

benjis = IceCreamStand("Benji's", "Ice Cream", 3, ["Mint", "Chocolate", "Vanilla"])
benjis.describe_restaurant()
benjis.describe_flavours()


for time in range(1, 10):
	print(f"\nIt's {time}pm")
	if time == nandos.opening_time:
		nandos.open_restaurant()
	if time == pizza_express.opening_time:
		pizza_express.open_restaurant()
	if time == mcdonalds.opening_time:
		mcdonalds.open_restaurant()
	if time == benjis.opening_time:
		benjis.open_restaurant()
	sleep(2)