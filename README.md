################################################################################
### General
################################################################################

NOTE:
-----
	- Les fonctions prefixees d'un _ sont des fonctions privees. Elles ne
	doivent pas etre appelees directement (sauf indications contraires)
	- Les mot prefixes d'un @ font reference aux arguments

################################################################################
### HStrings
################################################################################

Description:
============

	Fonctions effectuant des operations sur les chaines de caracteres

Fonctions:
==========

splitStr
-----
	description : decoupe une chaine par groupe de @size characteres
	prototype   : splitStr(string, size = 2)
	return      : un tableau contenant les differents groupes de caracteres
