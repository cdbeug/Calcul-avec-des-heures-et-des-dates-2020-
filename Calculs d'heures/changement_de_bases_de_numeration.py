
class System_de_numeration:
	def __init__(self, base):
		self.base = base
		self.symboles = [i for i in range(0, base)]

	def convertir_nombre_simple(self, nombre):
		res = []
		str_nombre = str(nombre)
		for i in str_nombre:
			res.append(i)
		return res		


	############## Fonctions utilitaires ##############

	'''
		tmp est un str
	'''
	def enleve_zero_a_gauche(self, tmp):
		res = ""
		if (tmp==""):
			return ""
		bool = True
		i = 0
		while (i<len(tmp) and bool):
			if (tmp[i]!="0"):
				bool = False
			i+=1
		i-=1
		if (i<len(tmp)):
			res = tmp[i:]
		else:
			res = "0"
		return res

	def nombre_vers_str(self, nombre):
		if (type(nombre)==int):
			return str(nombre)
		str_nombre = ""
		for i in nombre:
			str_nombre+=str(i)
		return str_nombre

	######## Fonctions utilitaires principales #########

	'''
		Si n2 est strictement plus long que n1, échange n1 et n2 et les renvoie
	'''
	def trie_deux_nombres(self, n1, n2):
		# n1 doit être le plus long
		if (len(n1)<len(n2)):
			tmp1 = n1
			n1 = n2
			n2 = tmp1
		return (n1, n2)

	'''
		nombre est de type list, et en base base
	'''
	def to_base_10(self, nombre):
		base = self.base
		i = 0
		# On part de la gauche vers la droite,
		# donc on commence avec les valeurs les plus
		# grosses.
		# Pour chaque symbole, on ajoute la valeur
		# de celui-ci (donnée par la table) et
		# avec facteur lié à sa position.
		for c in nombre:
			i *= base
			i += self.symboles[int(c)]
		res = self.convertir_nombre_simple(i)
		return res

	'''
		nombre est de type list, et en base 10
	'''
	def from_base_10(self, nombre):
		base = self.base
		""" Convert from a base 10 to the custom base"""
		number = int(self.nombre_vers_str(nombre))
		res = []
		# Division euclidienne en boucle jusqu'à ce que le
		# reste soit égal à zero.
		if (number==0):
			return [0]
		while number:
			number, value = divmod(number, base)
			# Le résultat est l'index du symbole.
			# On le place le plus à gauche, chaque
			# symbole ayant une valeur plus grande
			# que le précédent.
			res.insert(0, self.symboles[value])

		return res

	'''
		L'opération se fait dans ce sens :
			n1<opérateur>n2
	
		Valeurs possibles de operation :
			'+', '-', '*', '/', '%', '//', '**'
	'''
	def operation (self, n1, n2, operation):
		base = self.base
		operations_possibles = ['+', '-', '*', '/', '%', '//', '**']
		if (operation not in operations_possibles):
			print("operation : "+str(operation)+" n'est pas une opération possible")
			return -1
		n1_b = int(self.nombre_vers_str(self.to_base_10(n1)))
		n2_b = int(self.nombre_vers_str(self.to_base_10(n2)))
	
		if (operation=='+'):
			res_b = n1_b+n2_b
		if (operation=='-'):
			res_b = n1_b-n2_b
		if (operation=='*'):
			res_b = n1_b*n2_b
		if (operation=='/'):
			res_b = n1_b/n2_b
		if (operation=='%'):
			res_b = n1_b%n2_b
		if (operation=='//'):
			res_b = n1_b//n2_b
		if (operation=='**'):
			res_b = n1_b**n2_b

		res2_b = self.convertir_nombre_simple(res_b)
		res = self.from_base_10(res2_b)
		return res

	'''
		Renvoie n1 en base2
	'''
	def change_base(self, n1, base1, base2):
		conv1 = System_de_numeration(base1)
		res1 = conv1.to_base_10(n1)
		conv2 = System_de_numeration(base2)
		res2 = conv2.from_base_10(res1)
	
		return res2

	############## Fonctions principales ##############

	def affiche_nombre_libelle(self, nom_nombre, nombre):
		print(nom_nombre, "=", self.nombre_vers_str(nombre))

	def affiche_nombre(self, nombre):
		print(self.nombre_vers_str(nombre))

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

############# Fonctions utilitiares importantes ################

def entre_base(phrase):
	base = -1
	while (base<4):
		print("La base doit être suppérieure ou égale à 4 : ")
		base = entre_entier(phrase)
	return base

#*********************** Change base **************************#

'''
	Prend un tableau et renvoie un tableau
'''
def change_base_tab_tab (n1, base1, base2):
	conv = System_de_numeration(base1)
	res = conv.change_base(n1, base1, base2)
	return res

'''
	Prend un entier et renvoie un tableau
'''
def change_base_int_tab (n1, base1, base2):
	conv = System_de_numeration(base1)
	n1_tab = conv.convertir_nombre_simple(n1)
	res = change_base_tab_tab(n1_tab, base1, base2)
	return res

'''
	Prend un tableau et renvoie un entier (ne marche que vers la base 10)
'''
def change_base_tab_int (n1, base):
	res_tab = change_base_tab_tab(n1, base, 10)
	res = int(nombre_vers_str(res_tab))
	return res

'''
	S'adapte aux arguments donnés
'''
def change_base (n1, base1, base2):
	if (base1==10):
		if (base2==10):
			return n1
		else:
		# base2!=10
			res = change_base_int_tab(n1, base1, base2)
			return res
	else:
	# base1!=10
		if (base2==10):
			res = change_base_tab_int(n1, base1)
			return res
		else:
		# base2!=10
			res = change_base_tab_tab(n1, base1, base2)
			return res

#************************ Affichage ***************************#

'''
	Prend une liste
'''
def nombre_vers_str(nombre):
	conv = System_de_numeration(10)
	res = conv.nombre_vers_str(nombre)
	return res

def affiche_nombre_tab_libelle(nom_nombre, nombre):
	conv = System_de_numeration(10)
	res = conv.affiche_nombre_libelle(nom_nombre, nombre)
	return res

def affiche_nombre_tab(nombre):
	conv = System_de_numeration(10)
	res = conv.affiche_nombre(nombre)
	return res

##################### Tests #####################

def tests_systeme_de_numeration():
	base = 100
	n1_initial = 30
	n2_initial = 10
	conv = System_de_numeration(base)
	n1 = conv.convertir_nombre_simple(n1_initial)
	n2 = conv.convertir_nombre_simple(n2_initial)
	res_tmp = conv.operation(n1, n2, base, '+')
	conv.affiche_nombre_libelle("tests : res_tmp", res_tmp)
	res_tmp2 = conv.to_base_10(res_tmp)
	conv.affiche_nombre_libelle("tests : res_tmp2", res_tmp2)


##################### Menu #####################

def menu ():
	q = 0
	while (q<1 or q>3):
		print("Menu :")
		print("1 : Changer un nombre de base")
		print("2 : Changer plusieurs nombres de base")
		print("3 : Changer plusieurs nombres de base en gardant la même base")
		q = entre_entier("? = ")
	return q

##################### Main #####################	

def execution_principale():
	bool = True
	q = menu()
	if (q==1 or q==2):
		while (bool):
			base1 = entre_base("Base initiale = ")
			base2 = entre_base("Base finale = ")
			nombre = entre_nombre("nombre = ")
			if (base1!=10):
				conv = System_de_numeration(base1)
				nombre = conv.convertir_nombre_simple(nombre)
			res = change_base(nombre, base1, base2)
			print("res =", res)

			if (q==2):
				bool = True
			else:
				bool = False
	if (q==3):
		base1 = entre_base("Base initiale = ")
		base2 = entre_base("Base finale = ")
		while (True):
			nombre = entre_nombre("nombre = ")
			res = change_base(nombre, base1, base2)
			print("res =", res)		

def main():
	while (True):
		print("")
		execution_principale()
		print("")

#tests_systeme_de_numeration()
#main()