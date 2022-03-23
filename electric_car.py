from car import Car, ElectricCar

my_car = Car("VW", "Beetle", 2011)
my_car.car_name()
my_car.update_odometer(2600)
my_car.read_odometer()
my_car.increment_odometer(350)
my_car.read_odometer()
my_car.fuel_up()

print("\n")

my_tesla = ElectricCar('tesla', 'model 3', 2020)
my_tesla.car_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fuel_up()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.battery.describe_battery()

