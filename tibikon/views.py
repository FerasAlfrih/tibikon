from django.shortcuts import render
from .funcs import Feast as tbk
import datetime as dt

def home(request):
	if request.method == "POST":
		ser = request.POST.get('service')
		date = request.POST.get('date')
		date = date.replace("-", ",")
		date = dt.datetime.strptime(date, '%Y,%m,%d').date()
		dat = date.strftime('%A')
		serv = tbk(ser, date)
		service = serv.service.service
		pascha = serv.Easter
		ascension = serv.Ascension
		pentecost = serv.Pentecost
		Zacchaeus = serv.Zacchaeus
		PnPH = serv.PnPH
		PS = serv.PS
		LD = serv.LD
		SF = serv.SF
		sink = serv.sink
		isit = True
		lent = serv.lent
		orthodoxy = serv.orthodoxy
		GP = serv.GP
		cross = serv.cross
		ladder = serv.ladder
		egypt = serv.egypt
		lazarus = serv.lazarus
		palms = serv.palms
		GM = serv.GM
		GT = serv.GT
		GW = serv.GW
		GTH = serv.GTH
		GF = serv.GF
		GS = serv.GS
	else:
		service = None
		date = None
		dat = None
		pascha = None
		ascension = None
		pentecost = None
		sink = None
		Zacchaeus = None
		PnPH = None
		PS = None
		LD = None
		SF = None
		isit = False
		lent = None
		orthodoxy = None
		GP = None
		cross = None
		ladder = None
		egypt = None
		lazarus = None
		palms = None
		GM = None
		GT = None
		GW = None
		GTH = None
		GF = None
		GS = None

	context = {
		'service': service,
		'date': date,
		'dat': dat,
		'pascha': pascha,
		'ascension':ascension,
		'pentecost':pentecost,
		'sink' : sink,
		'Zacchaeus': Zacchaeus,
		'PnPH' : PnPH,
		'PS' : PS,
		'LD' : LD,
		'SF' : SF,
		'isit' : isit,
		'lent': lent,
		'orthodoxy' : orthodoxy,
		'GP' : GP,
		'cross' : cross,
		'ladder' : ladder,
		'egypt' : egypt,
		'lazarus' : lazarus,
		'palms' : palms,
		"GM" : GM ,
		"GT" : GT,
		"GW" : GW,
		"GTH" : GTH,
		"GF" : GF,
		"GS" : GS,

	}
	return render(request, 'home.html', context)