from django.shortcuts import render
from .funcs import Feast as tbk
import datetime as dt
from django import template                                                             

register = template.Library()                                                           

@register.filter(name='persianize_digits')                                              
def persian_int(string):                                                                
    persianize = dict(zip("0123456789",'۰١٢۳٤۵٦۷۸۹'))                                   
    return ''.join(persianize[digit] if digit in persianize else digit for digit in str(string))

def home(request):
	if request.method == "POST":
		ser = request.POST.get('service')
		d = request.POST.get('date')
		e = dt.datetime.now()
		date = d if d != '' else dt.datetime.strftime(e, '%Y,%m,%d')
		date = date.replace("-", ",")
		date = dt.datetime.strptime(date, '%Y,%m,%d').date()
		dat = date.strftime('%A')
		serv = tbk(ser, date)
		tone = serv.tone
		iothina = serv.iothina
		pentaweek = serv.pentaweek
		service = serv.service.service
		servs = serv.service.serv
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
		toma = serv.toma
		perf = serv.perf
		mokh = serv.mokh
		sam = serv.sam
		blond = serv.blond
		fef = serv.fef
		saints = serv.saints
		date = serv.date
		apsfast = serv.apsfast
		natfast = dt.date(date.year, 11, 15)
		ladyfast = dt.date(date.year, 8, 1)
		ladybirth = dt.date(date.year, 9, 8)
		cross = dt.date(date.year, 9, 14)
		ladyent = dt.date(date.year, 11, 21)
		lordbirth = dt.date(date.year, 12, 25)
		lordcirc = dt.date(date.year, 1, 1)
		lordpab = dt.date(date.year, 1, 6)
		lordent = dt.date(date.year, 2, 2)
		evang = dt.date(date.year, 3, 25)
		lordtrans = dt.date(date.year, 8, 6)
		ladydeath = dt.date(date.year, 8, 15)

		context = {
		'service': service,
		'servs': servs,
		'tone' : tone,
		'iothina' : iothina,
		'pentaweek': pentaweek,
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
		'toma' : toma,
		'perf' : perf,
		'mokh' : mokh,
		'sam' : sam,
		'blond' : blond,
		'fef' : fef,
		'saints': saints,
		'apsfast' : apsfast,
		'natfast' : natfast,
		'ladyfast' : ladyfast,
		'ladybirth': ladybirth,
		'cross': cross,
		'ladyent': ladyent,
		'lordbirth': lordbirth,
		'lordcirc': lordcirc,
		'lordpab' : lordpab,
		'lordent' : lordent,
		'lordtrans' : lordtrans,
		'evang' : evang,
		'ladydeath' : ladydeath,

	}

	else:
		isit = False
		context = {
		'isit': isit,
		}

	
	return render(request, 'home.html', context)