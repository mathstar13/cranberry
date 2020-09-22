def parse(fle):
	fll = open(fle)
	fl3 = fll.read()
	fl2 = fl3.replace('<cy var ','')
	fl1 = fl2.replace(' cy>','')
	fl = fl1.replace('equals','=')
	fll.close()
	return fl
def dump(n,v):
	f = open(n,'a')
	vn = v.replace('=',' equals ')
	f.write(f'\n<cy var.save {vn} cy>')
	f.close()