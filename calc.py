import re

wynik = 0

loop = True

#funkcja wyrzuca wiodace zera z liczb jezeli liczba nie jest zerem

def wywal_zera(element):
    if len(str(element)) > 1:
        return str(element).lstrip("0")
    else:
        return str(element)

#glowna funckja do obliczen

def przeliczaj():

    global wynik,counter,loop

    dzialanie = ""
    skladowe = []
    bez_widacych_zer = []


    dzialanie = input("Type equation:\n")

#zabezpieczenie przed brakiem wprowadzenia
    if dzialanie == "":
        print("No input!")
#wyjscie
    elif dzialanie == "quit":
        loop = False
#reset
    elif dzialanie == "c":
        wynik = 0

#dodanie spacji przed/po liczbach zeby mozna je bylo potem pociac dla funkcji wywalania zer
    else:

        dzialanie = re.sub('(\\d+)', ' \\1 ', dzialanie)

# wywalam wiodace zera jezeli gdzies sa
        skladowe = dzialanie.split()
        bez_wiodacych_zer = list(map(wywal_zera, skladowe))
        dzialanie = ''.join(bez_wiodacych_zer)

# wywalam litery, znaki specjalne itd

        dzialanie = re.sub('[a-zA-Z,:%$#@!&^=_" "]','', dzialanie)

        if dzialanie == "":
            dzialanie = 0
            wynik = 0
        else:
            wynik = eval(dzialanie)

        print ("Result:", wynik)



print("Basic semi fool-proof single equation calculator")
print("Type 'quit' to exit the program. Type 'c' to reset")
print("Calculator will ignore letters, most special characters and will remove any leading zeroes from numbers")
print(" \( \) works and can be used in equations")

while loop:

    przeliczaj()



