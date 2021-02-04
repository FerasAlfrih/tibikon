from datetime import datetime


class Tibikon():
	def __init__(self, serv, day=datetime.now()):
		self.day = day
		self.service = self.service(serv)
		self.level = self.service_leveler(serv)	
		self.type = self.types(self.level)
		


	def service(self, service):
		return "Vespers"

	def service_leveler(self, service):
		level = 2
		return level


	def types(self, level):	
		if level == 0:
			typer = 'XX'
		elif level == 1:		
			typer = 'WW'
		elif level == 2:
			typer = 'VV'
		elif level == 3:
			typer = 'YY'
		elif level == 4:
			typer = 'YW'
		elif level == 5:		
			typer = 'YV'
		elif level == 6:
			typer = 'ZZ'
		elif level == 7:
			typer = 'XZ'
		elif level == 8:
			typer = 'XW'
		elif level == 9:		
			typer = 'XV'
		elif level == 10:
			typer = 'XYY'
		elif level == 11:
			typer = 'XYW'
		elif level == 12:
			typer = 'XYV'
		elif level == 13:		
			typer = 'WV'
		elif level == 14:
			typer = 'WYY'
		elif level == 15:
			typer = 'WYW'
		elif level == 16:
			typer = 'WYV'
		elif level == 17:
			typer = 'VYY'
		elif level == 18:
			typer = 'VYW'
		elif level == 19:		
			typer = 'VYV'
		elif level == 20:
			typer = 'YYY'
		elif level == 21:
			typer = 'YYW'
		elif level == 22:
			typer = 'YYV'
		elif level == 23:		
			typer = 'YWW'
		elif level == 24:
			typer = 'YWV'
		elif level == 25:
			typer = 'YVV'
		print(typer)
		return typer

	def period(day=datetime.now()):
		day_period = 0
		return day_period


tib = Tibikon('ves')