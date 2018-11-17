class Car:
	"""docstring for Car"""

	def __init__(self, name = "General", model = "GM", vehicle_type = None, parked_speed = 0):
		super(Car, self).__init__()
		self.name = name
		self.model = model
		self.vehicle_type = vehicle_type
		self.speed = parked_speed

		if self.vehicle_type is not "trailer":
			self.vehicle_type = "saloon"

		if self.name in ['Porshe', 'Koenigsegg']:
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

	
		if self.vehicle_type is "trailer":
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4

	def is_saloon(self):
		if self.vehicle_type is "trailer":
			return False
		else:
			return True

	def drive(self, moving_speed):
		if moving_speed == 3:
			self.speed = 1000
			self.name = "Mercedes" 
			self.model = "SLR500"
		elif moving_speed == 7:
			self.speed = 77

		return self
		
honda = Car("Honda")
toyota = Car('Toyota', 'Corolla')
opel = Car('Opel', 'Omega 3')
porshe = Car('Porshe', '911 Turbo')
koenigsegg = Car('Koenigsegg', 'Agera R')
man = Car('MAN', 'Truck', 'trailer')




