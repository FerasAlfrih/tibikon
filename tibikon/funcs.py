import datetime as dt
import xml.etree.ElementTree as etree


	

class Feast():

	def __init__(self, serv, date):
		self.serv = serv
		self.d = date
		self.date = self.dater(self.d, self.serv)
		self.Easter, self.Ascension, self.Pentecost = self.easter()
		self.Zacchaeus, self.PnPH, self.PS, self.LD, self.SF, self.lent, self.orthodoxy, self.GP, self.cross, self.ladder, self.egypt, self.lazarus, self.palms, self.GM, self.GT, self.GW, self.GTH, self.GF, self.GS= self.paschalion()
		self.feast, self.sink = self.feast(self.date)
		self.level = self.leveler()
		self.service = self.service()		
		self.tone, self.iothina, self.pentaweek = self.toner()
	

	def easter(self):
		year=self.date.year
		silver=year%19
		pfm=21+(19*silver+15)%30
		dow=(pfm+year+year//4)%7
		easter=pfm+7-dow
		if easter>31:
			e = easter - 31
			easter = str(year) + ',' + '4' + ',' + str(e)
		else:
			easter= str(year) + ',' + '3' + ',' + str(easter)
		Easter = dt.datetime.strptime(easter, '%Y,%m,%d').date()
		if year <2100:
			Easter = Easter + dt.timedelta(days=13)
		else:
			Easter = Easter + dt.timedelta(days=14)
		Ascension = Easter + dt.timedelta(days=39)
		Pentecost = Easter + dt.timedelta(days=49)
		return Easter, Ascension, Pentecost


	def paschalion(self):		 
		easter = self.Easter
		Zacchaeus = easter - dt.timedelta(days=77)
		PnPH = easter - dt.timedelta(days=70)
		PS = easter - dt.timedelta(days=63)
		LD = easter - dt.timedelta(days=56)
		SF = easter - dt.timedelta(days=49)
		lent = easter - dt.timedelta(days=48)
		orthodoxy = easter - dt.timedelta(days=42)
		GP = easter - dt.timedelta(days=35)
		cross = easter - dt.timedelta(days=28)
		ladder = easter - dt.timedelta(days=21)
		egypt = easter - dt.timedelta(days=14)
		lazarus = easter - dt.timedelta(days=8)
		palms = easter - dt.timedelta(days=7)
		GM = easter - dt.timedelta(days=6)
		GT = easter - dt.timedelta(days=5)
		GW = easter - dt.timedelta(days=4)
		GTH = easter - dt.timedelta(days=3)
		GF = easter - dt.timedelta(days=2)
		GS = easter - dt.timedelta(days=1)
		
		return Zacchaeus, PnPH, PS, LD, SF, lent, orthodoxy, GP,cross,ladder,egypt,lazarus,palms, GM, GT, GW, GTH, GF, GS

	def is_sunday(self, date, service): 
		if date.strftime("%A") == "Sunday" and service != "Vespers":
			return True
		elif date.strftime("%A") == "Saturday" and service == "Vespers":
			return True
		else:
			return False

	def dater(self, d, service):
		if service == "Vespers":
			date = d + dt.timedelta(days=1)
		else:
			date = d
		return date


	def leveler(self):
		lev = []
		if self.is_sunday(self.d, self.serv):
			lev.append('X')
		f =self.feast
		f= ''.join(f.split())
		lev.append(f)
		level = ""
		for ele in lev: 
			level += ele
			
		return level

	def toner(self):
		date = self.date
		easter = self.Easter
		pentecost = self.Pentecost
		tones = ['الأول','الثاني','الثالث','الرابع','الخامس','السادس','السابع','الثامن']
		iothinas = ['الأولى','الثانية','الثالثة','الرابعة','الخامسة','السادسة','السابعة','الثامنة', 'التاسعة', 'العاشرة', 'الحادية عشرة']
		delta = date - easter
		delta = (delta.days / 7)
		tone = tones[(int(delta)%8) - 1]
		idelta = date - pentecost
		pentaweek = int(idelta.days / 7)
		iothina = iothinas[(pentaweek%11) - 1]
		return tone, iothina, pentaweek


	def service(self):
		if self.serv == "Vespers": 			
			service = Vespers(self.level)
			return service


	def feast(self, date):	
		d = "a" + str(date.day)
		m = date.strftime("%B")
		tree = etree.parse("static/files/calendar.xml")
		root = tree.getroot()		
		for node in root:
		    month = str(node).split(" ")[1]
		    month = month.replace("\'", "")
		    month = month.capitalize()
		    if month == m:		    
			    day = node.find(d)
			    i = node.find(d)[0].text
			    i = i.replace("\"", "")
			    i = i.replace(" ", "")
			    k = node.find(d)[1].text
			    day = str(day).split(" ")[1]
			    day = day.replace("a", "")
			    day = day.replace("\'", "")
			    return i, k
		    else:
		    	return None
	



class Vespers():

	def __init__(self, level):
		self.level = level	
		def func_not_found(): # just in case we dont have the function
			print( 'No Function '+self.level+' Found!')	
		func = getattr(self,self.level,func_not_found)
		self.service = func()

	def XX(self):
		service = "Qyamah"
		return service

	def WW(self):
		service = "Sayiedi"
		return service

	def VV(self):
		service = "Waldi"
		return service

	def YY(self):
		service = "MumtazG"
		return service

	def YW(self):
		service = "MumtazW"
		return service

	def YV(self):
		service = "MumtazN"
		return service

	def ZZ(self):
		service = "Normal"
		return service

	def YVY(self):
		service = "MumtazWE"
		return service

	def XZZ(self):
		service = "QN"
		return service

	def XWW(self):
		service = "QS"
		return service

	def XVV(self):
		service = "QW"
		return service

	def XYY(self):
		service = "QMG"
		return service

	def XYW(self):
		service = "QMW"
		return service

	def XYV(self):
		service = "QMN"
		return service

	def WV(self):
		service = "SW"
		return service

	def WYY(self):
		service = "SMG"
		return service

	def WYW(self):
		service = "SMW"
		return service

	def WYV(self):
		service = "SMN"
		return service

	def VYY(self):
		service = "WMG"
		return service

	def VYW(self):
		service = "WMW"
		return service

	def VYV(self):
		service = "WMN"
		return service

	def YYY(self):
		service = "2MG"
		return service

	def YYW(self):
		service = "GW"
		return service

	def YYV(self):
		service = "GN"
		return service

	def YWW(self):
		service = "2MW"
		return service

	def YWV(self):
		service = "WN"
		return service

	def YVV(self):
		service = "2MN"
		return service

	def ZV(self):
		service = "+W"
		return service

	def ZW(self):
		service = "+S"
		return service

	def ZX(self):
		service = "+Q"
		return service

	def ZY(self):
		service = "N+"
		return service

	def VY(self):
		service = "-W"
		return service

	def YYZ(self):
		service = "-MG"
		return service

	def WY(self):
		service = "-S"
		return service

	def XY(self):
		service = "-Q"
		return service

	def XWV(self):
		service = "QSW"
		return service

	def XWYY(self):
		service = "QSMG"
		return service

	def XWYW(self):
		service = "QSMW"
		return service

	def XWYV(self):
		service = "QSMN"
		return service

	def XVYY(self):
		service = "QWMG"
		return service

	def XVYW(self):
		service = "QWMW"
		return service

	def XVYV(self):
		service = "QWMN"
		return service

	def XYYY(self):
		service = "Q2MG"
		return service

	def XYYW(self):
		service = "QGW"
		return service

	def XYYV(self):
		service = "QGN"
		return service

	def XYWW(self):
		service = "Q2MW"
		return service

	def XYWV(self):
		service = "QWN"
		return service

	def XYVV(self):
		service = "Q2MN"
		return service

	def XZV(self):
		service = "Q+W"
		return service

	def XZW(self):
		service = "Q+S"
		return service

	def XZX(self):
		service = "Q+Q"
		return service

	def XZY(self):
		service = "QN+"
		return service

	def XVY(self):
		service = "Q-W"
		return service

	def XYYZ(self):
		service = "Q-MG"
		return service

	def XWY(self):
		service = "Q-S"
		return service

	def XXY(self):
		service = "Q-Q"
		return service

	def XYVY(self):
		service = "QMumtazWE"
		return service


		
class sahar():
	
	def __init__(self, level):
		self.level = level	
		def func_not_found(): # just in case we dont have the function
			print( 'No Function '+self.level+' Found!')	
		func = getattr(self,self.level,func_not_found)
		self.service = func()

	def XX(self):
		service = "Qyamah"
		return service

	def WW(self):
		service = "Sayiedi"
		return service

	def VV(self):
		service = "Waldi"
		return service

	def YY(self):
		service = "MumtazG"
		return service

	def YW(self):
		service = "MumtazW"
		return service

	def YV(self):
		service = "MumtazN"
		return service

	def ZZ(self):
		service = "Normal"
		return service

	def YVY(self):
		service = "MumtazWE"
		return service

	def XZZ(self):
		service = "QN"
		return service

	def XWW(self):
		service = "QS"
		return service

	def XVV(self):
		service = "QW"
		return service

	def XYY(self):
		service = "QMG"
		return service

	def XYW(self):
		service = "QMW"
		return service

	def XYV(self):
		service = "QMN"
		return service

	def WV(self):
		service = "SW"
		return service

	def WYY(self):
		service = "SMG"
		return service

	def WYW(self):
		service = "SMW"
		return service

	def WYV(self):
		service = "SMN"
		return service

	def VYY(self):
		service = "WMG"
		return service

	def VYW(self):
		service = "WMW"
		return service

	def VYV(self):
		service = "WMN"
		return service

	def YYY(self):
		service = "2MG"
		return service

	def YYW(self):
		service = "GW"
		return service

	def YYV(self):
		service = "GN"
		return service

	def YWW(self):
		service = "2MW"
		return service

	def YWV(self):
		service = "WN"
		return service

	def YVV(self):
		service = "2MN"
		return service

	def ZV(self):
		service = "+W"
		return service

	def ZW(self):
		service = "+S"
		return service

	def ZX(self):
		service = "+Q"
		return service

	def ZY(self):
		service = "N+"
		return service

	def VY(self):
		service = "-W"
		return service

	def YYZ(self):
		service = "-MG"
		return service

	def WY(self):
		service = "-S"
		return service

	def XY(self):
		service = "-Q"
		return service

	def XWV(self):
		service = "QSW"
		return service

	def XWYY(self):
		service = "QSMG"
		return service

	def XWYW(self):
		service = "QSMW"
		return service

	def XWYV(self):
		service = "QSMN"
		return service

	def XVYY(self):
		service = "QWMG"
		return service

	def XVYW(self):
		service = "QWMW"
		return service

	def XVYV(self):
		service = "QWMN"
		return service

	def XYYY(self):
		service = "Q2MG"
		return service

	def XYYW(self):
		service = "QGW"
		return service

	def XYYV(self):
		service = "QGN"
		return service

	def XYWW(self):
		service = "Q2MW"
		return service

	def XYWV(self):
		service = "QWN"
		return service

	def XYVV(self):
		service = "Q2MN"
		return service

	def XZV(self):
		service = "Q+W"
		return service

	def XZW(self):
		service = "Q+S"
		return service

	def XZX(self):
		service = "Q+Q"
		return service

	def XZY(self):
		service = "QN+"
		return service

	def XVY(self):
		service = "Q-W"
		return service

	def XYYZ(self):
		service = "Q-MG"
		return service

	def XWY(self):
		service = "Q-S"
		return service

	def XXY(self):
		service = "Q-Q"
		return service

	def XYVY(self):
		service = "QMumtazWE"
		return service



class divineLiturgie():
	
	def __init__(self, arg):
		self.arg = arg

class firstHour():
	
	def __init__(self, arg):
		self.arg = arg

class thirdHour():
	
	def __init__(self, arg):
		self.arg = arg


class sixthHour():
	
	def __init__(self, arg):
		self.arg = arg


class ninethHour():
	
	def __init__(self, arg):
		self.arg = arg

class Midnight():
	
	def __init__(self, arg):
		self.arg = arg


# F = Feast("Vespers",dt.date(2020,9,9)).easter()