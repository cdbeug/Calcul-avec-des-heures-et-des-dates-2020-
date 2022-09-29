import changement_de_bases_de_numeration as cb

class calculs_horaires:
	def __init__(self):
		pass

	'''
		L'année bisextile est définie par convention
		Elle doit être divisible par 4 ou par 400 et 
		non-divisible par 100.
	'''
	def est_une_annee_bisextile(self, annee):
		if (annee%400==0):
			return True
		elif (annee%4==0 and not annee%100==0):
			return True
		else:
			return False

###########################################################################

################### Fonctions utilitaires ####################

def is_number(a):
	chiffres = [".", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	nombre_de_points = 0
	a_tmp = (str)(a)

	if (a==""):
		return False
	j = 0
	for i in a_tmp:
		if (i=="-" and j>0):
			return False
		if (i=="."):
			nombre_de_points+=1
		if (nombre_de_points>1):
			return False
		if i not in chiffres:
			return False
		j+=1
	return True	

def is_integer(a):
	if (is_number(a)):
		return ("." not in str(a))
	else:
		return False

def entre_nombre(phrase):
	cmp = 0
	res = ""
	while (not is_number(res)):
		if (cmp>0):
			print("Veuiller entrer un nombre")
		res = input(phrase)
		cmp+=1
	if (is_integer(res)):
		return int(res)
	else:
		return float(res)

def entre_entier(phrase):
	cmp = 0
	res = ""
	while (not is_integer(res)):
		if (cmp>0):
			print("Veuiller entrer un entier")
		res = input(phrase)
		cmp+=1
	return int(res)

'''
	Prend un entier, un double ou un str
'''
def separe_partie_decimale_entiere(nombre):
	if (type(nombre)==int or type(nombre)==float):
		nombre = str(nombre)
	# Ne prend pas en compte le nombre lorsqu'il s'affiche avec une puissance de 10
	if ("e" in nombre):
		return (0, 0)
	if (is_integer(nombre)):
		return (int(nombre), 0)
	else:
		tab = nombre.split('.')
		return (int(tab[0]), int(tab[1]))

'''
	Renvoie True si nombre contient une décimale
'''
def contient_decimale(nombre):
	if (nombre==""):
		return False
	(ent, dec) = separe_partie_decimale_entiere(nombre)
	return (dec!=0)

'''
	Parcours le tableau tab et retourne le premier indice de la valeur valeur.
'''
def indice_valeur (tab, valeur):
	for i in range(len(tab)):
		if (tab[i]==valeur):
			return i
	return -1

def entre_choix_tab (tab_choix, phrase):
	q = 0
	while (q<1 or q>len(tab_choix)):
		print("")
		print(phrase)
		i = 0
		for j in tab_choix:
			print(str(i+1)+" : "+str(j))
			i+=1
		q = entre_entier("? = ")
		print("")
	return q

############ Fonctions utilitaires principales ###############

def entre_annee(message):
	annee = 0
	while (annee==0):
		annee = entre_entier(message)
		if (annee==0):
			print("L'an 0 n'existe pas dans le calendrier actuel")
	return annee

def donne_liste_types_date_descendante_avec_accents():
	hierarchie_types = []
	hierarchie_types.append("millénaire")
	hierarchie_types.append("sciècle")
	hierarchie_types.append("année")
	hierarchie_types.append("mois")
	hierarchie_types.append("semaine")
	hierarchie_types.append("jour")
	hierarchie_types.append("heure")
	hierarchie_types.append("minute")
	hierarchie_types.append("seconde")

	return hierarchie_types

def donne_liste_types_date_ascendante_avec_accents():
	tmp = donne_liste_types_date_descendante_avec_accents()
	res = tmp[::-1]
	return res

def donne_liste_types_date_descendante():
	hierarchie_types = donne_liste_types_date_descendante_avec_accents()
	for i in range(len(hierarchie_types)):
		tmp = hierarchie_types[i]
		tmp = tmp.replace('é', 'e')
		tmp = tmp.replace('è', 'e')
		hierarchie_types[i] = tmp

	return hierarchie_types

def donne_liste_types_date_ascendante():
	tmp = donne_liste_types_date_descendante()
	res = tmp[::-1]
	return res

def donne_table_de_correspondance_descendante():
	hierarchie_types = donne_liste_types_date_descendante()

	table_de_correspondance_aux = []
	table_de_correspondance_aux.append(10) # millénaire
	table_de_correspondance_aux.append(100) # sciècle
	table_de_correspondance_aux.append(12) # année
	table_de_correspondance_aux.append(4) # mois
	table_de_correspondance_aux.append(7) # semaine
	table_de_correspondance_aux.append(24) # jour
	table_de_correspondance_aux.append(60) # heure
	table_de_correspondance_aux.append(60) # minute

	table_de_correspondance = {}
	i = 0
	for j in range(len(table_de_correspondance_aux)):
		table_de_correspondance[hierarchie_types[j]] = table_de_correspondance_aux[i]
		i+=1

	return table_de_correspondance

def donne_table_de_correspondance_ascendante():
	hierarchie_types = donne_liste_types_date_ascendante()

	table_de_correspondance_aux = []
	table_de_correspondance_aux.append(1) # seconde
	table_de_correspondance_aux.append(60) # minute
	table_de_correspondance_aux.append(60) # heure
	table_de_correspondance_aux.append(24) # jour
	table_de_correspondance_aux.append(7) # semaine
	table_de_correspondance_aux.append(4) # mois
	table_de_correspondance_aux.append(12) # année
	table_de_correspondance_aux.append(100) # sciècle
	table_de_correspondance_aux.append(10) # millénaire

	table_de_correspondance = {}

	for i in range(len(hierarchie_types)):
		table_de_correspondance[hierarchie_types[i]] = {}
		for j in range(i, len(hierarchie_types)):
			#print("\ni =", i); print("j =", j)
			multiple = donne_table_de_correspondance_ascendante_calcule_multiple(i, j, table_de_correspondance_aux)
			table_de_correspondance[hierarchie_types[i]][hierarchie_types[j]] = multiple
			#print(hierarchie_types[i], ",", hierarchie_types[j], "=", table_de_correspondance[hierarchie_types[i]][hierarchie_types[j]])

	return table_de_correspondance

'''
	Exprime les correspondance en double :
		seconde seconde, seconde minutes, ... minute heure, minute jour, etc...
'''
def donne_table_de_correspondance_descendante_complexe():
	hierarchie_types = donne_liste_types_date_descendante()

	table_de_correspondance_aux = []
	table_de_correspondance_aux.append(1) # millénaire
	table_de_correspondance_aux.append(10) # sciècle
	table_de_correspondance_aux.append(100) # année
	table_de_correspondance_aux.append(12) # mois
	table_de_correspondance_aux.append(4) # semaine
	table_de_correspondance_aux.append(7) # jour
	table_de_correspondance_aux.append(24) # heure
	table_de_correspondance_aux.append(60) # minute
	table_de_correspondance_aux.append(60) # seconde

	table_de_correspondance = {}

	for i in range(len(hierarchie_types)):
		table_de_correspondance[hierarchie_types[i]] = {}
		for j in range(i, len(hierarchie_types)):
			#print("\ni =", i); print("j =", j)
			multiple = donne_table_de_correspondance_ascendante_calcule_multiple(i, j, table_de_correspondance_aux)
			table_de_correspondance[hierarchie_types[i]][hierarchie_types[j]] = multiple
			#print(hierarchie_types[i], ",", hierarchie_types[j], "=", table_de_correspondance[hierarchie_types[i]][hierarchie_types[j]])

	return table_de_correspondance

'''
	Parcours table_de_correspondance_aux entre indice1 et indice2 en multipliant les 
	cases parcourues et renvoie le résultat.
'''
def donne_table_de_correspondance_ascendante_calcule_multiple (indice1, indice2, table_de_correspondance_aux):
	if (indice1<0 or indice1>len(table_de_correspondance_aux)-1):
		print("donne_table_de_correspondance_ascendante_aux : Erreur, Indice1="+str(indice1)+" n'est pas conforme")
		return -1
	if (indice2<0 or indice2>len(table_de_correspondance_aux)-1):
		print("donne_table_de_correspondance_ascendante_aux : Erreur, Indice2="+str(indice2)+" n'est pas conforme")
		return -1
	if (indice1>indice2):
		print("donne_table_de_correspondance_ascendante_aux : Erreur, Indice1="+str(indice1)+">Indice2="+str(indice2))
		return -1
	if (indice1==indice2):
		table_de_correspondance_aux[indice1] = 1
	res = table_de_correspondance_aux[indice1]
	i = indice1
	while (i<indice2+1):
		res*=table_de_correspondance_aux[i]
		i+=1
	return res

'''
	Prend un tableau avec un format, du type :
		[1, 2, 3, 0, 5, 0, 7, 0, 0]
		0 : type non-voulu
		différent de 0 : type voulu
'''
def fabrique_liste_des_types_cible_voulus(tab_liste_tmp):
	liste_brute = donne_liste_types_date_descendante()
	#print(liste_brute)
	res = []
	for i in range(len(tab_liste_tmp)):
		if (tab_liste_tmp[i]!=0):
			res.append(liste_brute[i])
	return res

def convertit_choix_des_types_en_format_tab(choix):
	res = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	if (type(choix)!=str): return
	tmp_tab = choix.split(",")
	if (len(tmp_tab)==0):return res
	for i in tmp_tab:
		tmp2 = i.replace(" ", "")
		if (tmp2!=""):
			if(is_integer(tmp2)):
				tmp3 = int(tmp2)
				if (tmp3>0 and tmp3<len(res)):
					res[tmp3-1] = 1
	return res

def verifie_format_choix_des_types_cible_voulus(tmp):
	if (type(tmp)!=str): return False
	tmp_tab = tmp.split(",")
	if (len(tmp_tab)==0):return True
	for i in tmp_tab:
		tmp2 = i.replace(" ", "")
		if (tmp2==""): return False
		elif not is_integer(tmp2): return False
	return True	

################### Fonctions principales ####################

#********************* Année bisextile **********************#

def est_une_annee_bisextile(annee):
	ch = calculs_horaires()
	return ch.est_une_annee_bisextile(annee)

def annee_bisextile_dialogue():
	print("Entrer une année :")
	annee = entre_annee("Année = ")
	annee_bisextile_affichage(annee)

def annee_bisextile_affichage(annee):
	ch = calculs_horaires()
	res = ch.est_une_annee_bisextile(annee)
	if (res):
		print("L'année", annee, "est bisextile")
	else:
		print("L'année", annee, "n'est pas bisextile")

#***################# Dates décomposées ##################***#

###***************** Dates déscendantes *******************###

'''
	types possibles :
		millénaire
		sciècle
		année
		mois
		semaine
		jour
		heure
		minute
		seconde
'''
def date_descendante(nombre, type):
	hierarchie_types = donne_liste_types_date_descendante()

	res={}
	for i in hierarchie_types:
		res[i] = 0

	table_de_correspondance = donne_table_de_correspondance_descendante()
	res[type] = nombre
	if (is_integer(nombre)):
		return res
	premier_type = 0
	j = 0
	for i in hierarchie_types:
		if (i==type):
			premier_type = j
		j+=1
	if (premier_type==len(hierarchie_types)-1):
		return res
	i = premier_type+1
	while (i<len(hierarchie_types)):
		type_present = hierarchie_types[i]
		type_precedent = hierarchie_types[i-1]

		multiple = table_de_correspondance[type_precedent]
		if (res[type_precedent]!=0):
			res[type_present] = res[type_precedent]*multiple
			(ent, dec) = separe_partie_decimale_entiere(res[type_precedent])
			if (dec!=0):
				#print("multiple_des =", multiple)
				res[type_present] = float("0."+str(dec))*multiple
		i+=1

	return res

##***####**************** Affichage *****************###***###

def affichage_date_descendante(tab, type_de_base):
	#print(str(tab))
	liste_types = donne_liste_types_date_descendante()
	liste_types_avec_accents = donne_liste_types_date_descendante_avec_accents()
	res = ""
	i = 0
	type = ""
	valeur = 0
	nbre_de_valeurs = 0
	for i in tab:
		type = i
		valeur = tab[i]
		if (type!="seconde"):
			valeur = int(valeur)
		if (valeur!=0):
			nbre_de_valeurs+=1
	if (nbre_de_valeurs==0):
		valeur = tab[type_de_base]
		res = str(valeur)+" "+type_de_base
		if(valeur>0):
			res+="s"
		return res
	#print("Nombre de valeurs =", nbre_de_valeurs)
	for i in range(len(tab)):
		type = liste_types[i]
		type_avec_accent = liste_types_avec_accents[i]
		valeur = tab[type]
		if (type!="seconde"):
			if ("e" not in str(valeur)):
				valeur = int(valeur)
		if (valeur!=0):
			res+=str(valeur)+" "+str(type_avec_accent)
			if (valeur>1 and type!="mois"):
				res+="s"

			nbre_de_valeurs-=1
			if (nbre_de_valeurs>1):
				res+=", "
			elif (nbre_de_valeurs==1):
				res+=" et "
		i+=1

	return res

'''
	Crée le tableau et renvoie les str
'''
def affichage_date_descendante_complet(nombre, type):
	tmp = date_descendante(nombre, type)
	#print(tmp)
	return affichage_date_descendante(tmp, type)

'''
	Crée le tableau et renvoie les str
'''
def affichage_date_ascendante_complet(nombre, type, types_cible_voulus):
	tmp = date_ascendante(nombre, type, types_cible_voulus)
	return affichage_date_descendante(tmp, type)

###****************** Dates ascendantes *******************###

'''
	types possibles :
		millénaire
		sciècle
		année
		mois
		semaine
		jour
		heure
		minute
		seconde

	types_cible_voulus :
		tableau où l'utilisateur (de la fonction)
		mettra les type cibles dans lesquels seront 
		exprimés le nombre nombre

		La fonction exprimera le type donné
		en le type choisi le plus grand,
		puis décomposera en descendant à partir de ce type.

'''
def date_ascendante(nombre, type, types_cible_voulus):
	hierarchie_types = donne_liste_types_date_descendante()

	res={}
	for i in hierarchie_types:
		res[i] = 0

	table_de_correspondance_ascendante = donne_table_de_correspondance_ascendante()

	#print(types_cible_voulus)
	if (len(types_cible_voulus)==0):
		res[type] = nombre
		#print(res)
		return res

	plus_grand_type_voulu = types_cible_voulus[0]
	#print("plus_grand_type_voulu =", plus_grand_type_voulu)
	table_de_correspondance_descendante_complexe = donne_table_de_correspondance_descendante_complexe()

	# expression du nombre en fonction du plus grand type voulu
	res[plus_grand_type_voulu] = nombre/table_de_correspondance_ascendante[type][plus_grand_type_voulu]

	# décomposition
	if (len(types_cible_voulus)>1):
		i = 0
		i+=1
		while (i<len(types_cible_voulus)-1):
			type_present = types_cible_voulus[i]
			type_precedent = types_cible_voulus[i-1]
			multiple = table_de_correspondance_descendante_complexe[type_precedent][type_present]

			#print("type_present =", type_precedent); print("type_present =", type_present)
			if (res[type_precedent]!=0):
				res[type_present] = res[type_precedent]*multiple
				(ent, dec) = separe_partie_decimale_entiere(res[type_precedent])
				if (dec!=0):
					res[type_present] = float("0."+str(dec))*multiple
			i+=1	

	# tranformation en int de tous les nombres sauf les secondes dans res
	#print(res)
	return res


#************************** Main ****************************#

def traitement_annee(ratio, annee):
	heures = 0; minutes = 0; secondes = 0
	dec=0; dec_h = 0; dec_m = 0
	nombre_de_jours = 365
	if (est_une_annee_bisextile(annee)):
		nombre_de_jours = 366
	jours = float(nombre_de_jours)*ratio
	res = affichage_date_descendante_complet(jours, 'jour')+"."
	return res

#################### Menus #####################

#***************** Principal ******************#

def menu_principal ():
	q = 0
	while (q<1 or q>2):
		print("Menu :")
		print("1 : Années bisextiles")
		print("2 : Calculs avec des dates")
		#print("3 : Savoir si des années comprises entre deux années sont bisextiles")
		q = entre_entier("? = ")

	return q

#**************** Secondaires *****************#

def menu_calculs_dates ():
	q = 0
	while (q<1 or q>3):
		print("Menu :")
		print("1 : Calcul avec des années")
		print("2 : decomposer une quantité de temps exprimée en float du plus grand vers le plus petit")
		print("3 : decomposer une quantité de temps exprimée en float du plus petit vers le plus grand")
		q = entre_entier("? = ")
	return q

def menu_annee_bisextile ():
	q = 0
	while (q<1 or q>3):
		print("Menu :")
		print("1 : Savoir si une année est bisextile")
		print("2 : Savoir si plusieurs années sont bisextiles")
		print("3 : Savoir si des années comprises entre deux années sont bisextiles")
		q = entre_entier("? = ")
	return q

#***************** Tertiaires *****************#

def menu_choix_des_types_cible_voulus():
	bool_ok = True
	res = ""
	liste_types = donne_liste_types_date_descendante_avec_accents()
	while (bool_ok):
		print("")
		print("Choisissez les types dans lesquelles vous souhaitez que soient exprimés le nombre, \nselon le format suivant :")
		print("? = 1, 2, 8")
		for i in range(len(liste_types)):
			print(str((i+1))+" : "+liste_types[i])
		res = input("? = ")	
		print("")
		if (verifie_format_choix_des_types_cible_voulus(res)):
			bool_ok = False
	return res

#################### Tests #####################

def tests_calculs_horaires():
	ch = calculs_horaires()
	print(ch.est_une_annee_bisextile(100))
	print(ch.est_une_annee_bisextile(400))
	print(ch.est_une_annee_bisextile(4))

def test_donne_table_de_correspondance_ascendante():
	res = donne_table_de_correspondance_ascendante()

def tests():
	#execution_calculs_dates()
	#print(contient_decimale(""))

	nombre = 275776867866781.2376286
	type = "seconde"
	#type2 = "millenaire"
	print("nombre =", nombre)
	print("type =", type)
	#print("type2 =", type2)
	#print(verifie_format_choix_des_types_cible_voulus("0, 0, 0, 0, 0, 0, 0, 0, 0"))
	#tab_liste_menu = menu_choix_des_types_cible_voulus()
	tab_liste_tmp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	#tab_liste_tmp = [1, 2]
	#tab_liste_tmp = []
	#tab_liste_tmp = convertit_choix_des_types_en_format_tab(tab_liste_menu)
	types_cible_voulus = fabrique_liste_des_types_cible_voulus(tab_liste_tmp)
	#print("types_cible_voulus =", types_cible_voulus)
	#res = date_ascendante(nombre, type, types_cible_voulus)
	#print(str(res))
	#print(affichage_date_descendante(res, type))
	print(affichage_date_ascendante_complet(nombre, type, types_cible_voulus))
	#print(affichage_date_descendante_complet(res[type2], type2))

##################### Main #####################

def execution_calculs_dates():
	print("")
	q = menu_calculs_dates()
	print("")

	if (q==1):
		annee = 2019
		ratio = entre_nombre("Entrez un ratio : \nRatio = ")
		#ratio = 1.75
		#print("Entrez un ratio : \nRatio = "+str(ratio))
		print("")
		res_2019 = traitement_annee(ratio, annee)
		annee = 2020
		res_2020 = traitement_annee(ratio, annee)
		print("Année normale (365 jours) :")
		print(res_2019)
		print("")
		print("Année bisextile (366 jours) :")
		print(res_2020)
	if (q==2):
		nombre = entre_nombre("Entrer le nombre (si possible, à virgule)\nNombre = ")
		liste_types_avec_accents = donne_liste_types_date_descendante_avec_accents()
		liste_types = donne_liste_types_date_descendante()
		type_q = entre_choix_tab(liste_types_avec_accents, "Quel est l'ordre de grandeur de votre nombre ?")
		type = liste_types[type_q-1]
		print(affichage_date_descendante_complet(nombre, type))

	if (q==3):
		nombre = entre_nombre("Entrer le nombre\nNombre = ")
		liste_types_avec_accents = donne_liste_types_date_ascendante_avec_accents()
		liste_types = donne_liste_types_date_ascendante()
		type_q = entre_choix_tab(liste_types_avec_accents, "Quel est l'ordre de grandeur de votre nombre ?")
		type = liste_types[type_q-1]
		tab_liste_menu = menu_choix_des_types_cible_voulus()
		tab_liste_tmp = convertit_choix_des_types_en_format_tab(tab_liste_menu)
		types_cible_voulus = fabrique_liste_des_types_cible_voulus(tab_liste_tmp)
		print(affichage_date_ascendante_complet(nombre, type, types_cible_voulus))
		
	print("")

def execution_annee_bisextile():
	bool = True
	print("")
	q = menu_annee_bisextile()
	print("")

	if (q==1):
		annee_bisextile_dialogue()
	if (q==2):
		while (True):
			print("")
			annee_bisextile_dialogue()
			print("")
	if (q==3):
		annee1 = 11
		annee2 = 10
		tmp = 0
		while (annee1>annee2):
			annee1 = entre_annee("Veuillez entrer la première année\nAnnée 1 = ")
			annee2 = entre_annee("Veuillez entrer la première année\nAnnée 2 = ")
			if (tmp>0):
				print("Année 1 doit être avant l'année 2 :")
			tmp+=1

		print("")
		limite = annee2-annee1+1
		for i in range(0, limite):
			annee_bisextile_affichage(annee1+i)
	print("")

def execution_principale():
	print("")
	q = menu_principal()

	if (q==1):
		execution_annee_bisextile()
	if (q==2):
		execution_calculs_dates()

	print("")

def main():
	while (True):
		execution_principale()

main()
#tests()