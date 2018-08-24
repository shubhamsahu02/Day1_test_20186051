class Clock(object):
    def __init__(self, time):
		self.time = time
    def print_time(self):
		time = '6:30'
		print(self.time)
	def set_time (self, time):
		print(time)
	def tere_maa_ki(self, time):
		self.time = time


clock = Clock('5:30')
clock.print_time()
clock.set_time()
clock.tere_maa_ki('10:30')