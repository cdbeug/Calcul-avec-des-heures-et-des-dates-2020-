
def aff_tab(nom_tab, tab):
	print("")
	print(nom_tab+" ("+str(len(tab))+") : \n")
	for i in range(len(tab)):
		print(nom_tab+"["+str(i)+"] = "+str(tab[i]))
	print("")

def main():
	#(min, max) = (1800, 2004)
	(min, max) = (1, 3000)
	div_par_4 = []
	div_par_100 = []
	div_par_400 = []
	for i in range(min, max+1):
		if (i%4==0):
			div_par_4.append(i)
		if (i%100==0):
			div_par_100.append(i)
		if (i%400==0):
			div_par_400.append(i)

	div_par_4_et_pas_par_100 = []
	div_par_100_et_par_400 = []
	bisextile = []

	for i in div_par_4:
		if (i not in div_par_100):
			div_par_4_et_pas_par_100.append(i)
	for i in div_par_100:
		if (i not in div_par_400):
			div_par_100_et_par_400.append(i)

	for i in div_par_400:
		bisextile.append(i)
	for i in div_par_4_et_pas_par_100:
		bisextile.append(i)

	#aff_tab("div_par_400", div_par_400)
	#aff_tab("div_par_100", div_par_100)
	#aff_tab("div_par_100_et_par_400", div_par_100_et_par_400)
	#aff_tab("div_par_4", div_par_4)
	#aff_tab("div_par_4_et_pas_par_100", div_par_4_et_pas_par_100)

	for i in div_par_4:
		if (i in bisextile):
			print(str(i)+" est bisextile")
		else:
			if (i in div_par_100):
				print(str(i)+" n'est pas bisextile car divisible par 100")

main()