##NUMBERS
########################################

# Exercitiul 1:
# Introdu de la tastatura doua numere.Fa suma lor ,diferenta si produsul.Afiseaza-le pe
# pe ecran:
#
# a = int(input("a = "))
# b = int(input("b = "))
#
# s = a + b
# d = a - b
# p = a * b
# print(s, d, p)


#############################################################

# Exercitiul nr 2

# Afiseaza cate luni au trecut de cand te-ai nascut.Varsta se introduce de la tastatura:

# age = int(input("enter your age :"))
#
# print(f"{age * 12} months since you were born ")
##############################################################################

# Exercitiul nr 3 :

# Calculeaza indicele de masa corporala .Introdu de la tastatura datele de intrare :
# -greutatea[Kg],inaltimea[m]

# weight = float(input("weigh[kg] : "))
# height = float(input("height[cm] :"))
#
# bmi = weight / pow(height, 2)
# print(bmi)

############################################################################################

# Exercitiul nr 4 :
# Calculeaza ipotenuza , perimetru si aria unui triunghi dreptunghic ale carui catele au valorile 6 si 8.

# cat_1 = 6
# cat_2 = 8
#
# ipotenuza = (pow(cat_1, 2) + pow(cat_2, 2)) ** 0.5
#
# perimetru = cat_1 + cat_2 + ipotenuza
# aria = cat_1 * cat_2 / 2
# print(ipotenuza, perimetru, aria)


# STRINGS#################

# Exercitiul nr 1 :

# Introdu de la tastatura o propozitie .
# Afiseaza de cate ori apare caracterul a si care este indexul ultimei aparitii:

# sentence  = input("enter the sentence : ")
# print(f"{sentence.count('a')} and the last index is {sentence[-1]}")


# print(f"Number of occurrences: {sentence.count('a')}")
# if sentence.rfind('a') != -1:
#     print(f"Last index: {sentence.rfind('a')}")
# else:
#     print('The character does not exist!')
#####################################################################################

# Exercitiul nr 2 :

# Afiseaza care este extensia unui fiser.Numele fiserului se introduce de la tastatura :

# file_name = input("enter the file_name: ")
#
# ind = file_name.rfind('.')
# extensia = file_name[ind::]
#
# print(extensia)
#############################################################################

#Exercitiul nr 3 :

#Scrie un program care citeste un mesaj de la tastatura.Daca mesajul este un numar, ridica-l la puterea
#a 2 a si afiseaza pe ecran rezultatul .Daca nu este un numar afiseaza mesajul pe ecran.

# message = input("message: ")
#
# if message == int(input(message)):
#     print(f"{message ** 2}")
#
# else:
#     print(message)
#####################################################

#Exercitiul nr 4 :


#Se introduc de la tastatura 2 cuvinte. Afiseaza daca cele doua cuvnte au acceiasi lungime.

# word_1 = input("enter the word_1 :")
# word_2 = input("Enter the word_2 :")
#
# if len(word_1) == len(word_2):
#     print("The words have the same size!")
# else:
#     print("The words do not have the same size!")
################################################################################

#Exercitiul nr 5 :
# Afiseaza pe ecran numele  userul-ului din acest string:
# command = 'platform: Solaris; version: 2.5; username: mcristi_123_456; all rights reserved to...'
#
# if command.find('username') != -1:
#     ind_1 = command.find('username')
#     ind_2 = command.rfind(';')
#     print(command[ind_1 + len('username: '):ind_2])


###################################################################################
#Exercitiul nr 6 :
# Sa da urmatorul string:
# name = 'first-name'
# Convertiti acest string intr-unul snake_case.

# Import the 'sub' function from the 're' module for regular expression substitution
from re import sub
##################################################################################################


####CONDITIONAL STATEMENTS ################

# Exercitiul nr 1 :

# Intrordu un numar de 3 cifre de la tastatura.
# - Daca numarul este par afiseaza suma dintre numarul introdus si ultima lui cifra.
# - Daca este impar afiseaza daca este multiplu de 3.
#
# n = input('n = ')
#
# if len(n) == 3:
#     if int(n) % 2 == 0:
#         print(int(n) + int(n[-1]))
#     elif int(n) % 3 == 0:
#         print('it is divisible by 3')
#     else:
#         print('not divisible by 3')

#########################################################################################

# Exercitiul nr 2 :

# Fie un semafor programat, pentru pietoni. La inceputul fiecarei ore, timp de 3 minute este verde, dupa care
# timp de 2 minute este rosu, aceste ferestre de timp de 3, respectiv 2 minute, continuand pe parcursul
# intregii ore. Se citeste de la tastatura un timp t (min).
#
# Sa se determine ce culoare are semaforul la timpul t.

# t = int(input('time: '))
#
# if t % 5 >= 3:
#     print('red')
# else:
#     print('green')

######################################################################################

# Exercitiul nr 3

# Scrie un program care citeste o propozitie de la tastatura.
# Afiseaza numarul cuvintelor din acea propozitie

# sentence = input('sentence: ')
#
# print(f"number of words: {sentence.count(' ') + 1}")

#Exercitiul nr 4 :

# Introdu de la tastatura un numar intreg. Printeaza pe ecran:
# - ‘PYTHON’ daca numarul este mai mare decat 10
# - ‘python’ daca este mai mic sau egal cu 10.

# n = int(input("n = "))
#
# if n >10 :
#    print("PYTHON")
# else:
#       print("python")

#Exercitiul nr 4 :
#
# Introdu un cuvant de la tastatura.
# - Daca are mai putin de 5 caractere printeaza pe ecran ‘Cuvant scurt’
# - Daca are exact 5 caractere printeaza cuvantul introdus
# - Daca are mai mult de 8 caractere printeaza ‘Cuvant lung’.

# word = input('word: ')
#
# if len(word) < 5:
#     print('The word is short')
# elif len(word) > 8:
#     print('the word is long')
# elif len(word) == 5:
#     print(word)

###################################################################

#Exercitiul nr 5 :

# Scrie un program care citeste de la tastatura 2 numere.
# - Daca a > b afiseaza diferenta a - b.
# - Daca a < b afiseaza diferenta b - a.

# a = int(input("a = "))
# b = int(input("b = "))
#
# if a > b:
#     print(a - b)
# elif a < b:
#     print(b - a)

#######################################################################

#Exercitiul nr 6 :

# Introdu de la tastatura un username si o parola.
# - Daca sunt corecte afiseaza mesajul ->  {username} s-a logat cu succes
# Mai departe cere input-ul user-ului pentru nume, prenume, e-mail si experienta in IT (ani).
# - Daca experienta in IT este mai mica de 1.5 ani, afiseaza mesajul {nume} este junior.
# - Daca experienta in IT este intre 1.5 si 3 ani, afisati mesajul {nume} este intermediar.
# - Pentru mai mult de 3 ani experienta afisati mesajul {nume} este senior.

# Username-ul si parola sunt corecte daca au valorile hardcoded de mai jos:
# user = ‘windows_user’
# pass = ‘P@rolla’

# user = input("username :")
# pas = input("password :")
#
# if user == 'windows_user' and pas == 'P@rolla':
#     print(f"{user}  has logged succesfully")
# else:
#     print("The password or username is incorrect")
#
# name = input("enter your name :")
# first_name = input("enter your first_name :")
# email = input("enter your email address :")
# it_experience = float(input("it experience[years] :"))
#
# if it_experience < 1.5:
#     print(f"{name} is junior!")
# elif 1.5 < it_experience < 3:
#     print(f"{name} is intermediar")
# elif it_experience > 3:
#     print(f"{name} is senior.")

#################################################################################################

#LOOPS IN PYTHON ############

#Exercitiul nr 1 :

# names = ['Maria', 'Elena', 'Ioan']
# ages = ['2', '30', '7']
#
# for i, name in enumerate(names):
#     print(f'{name} is {ages[i]} years old')
#

for i in range(10):
    if i == 4:
         continue
    print(i)