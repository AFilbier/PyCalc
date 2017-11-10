import re


wynik = 0
counter = 0
loop = True


#funkcja wyrzuca wiodace zera z liczb jezeli liczba nie jest zerem
def wywal_zera(element):
    if len(str(element)) > 1:
        return str(element).lstrip("0")
    else:
        return str(element)


#Glowna fukncja do obliczen
def przeliczaj():
    global wynik,counter,loop

    dzialanie = ""
    skladowe = []
    bez_widacych_zer = []


#zeby prompt byl tylko na poczatku, po resecie, po wyniku 0
    if wynik == 0:
        if counter == 0:
            dzialanie = input("Type equation:\n")
        if counter == 1:
            dzialanie = input("Last one evaluated to zero, type next equation:\n")
    else:
        dzialanie = input(str(wynik))

#zabezpieczenie przed brakiem wprowadzenia
    if dzialanie == "":
        print("No input!")

#wyjscie
    elif dzialanie == "quit":
        loop = False
#reset
    elif dzialanie == "c":
        wynik = 0
        counter = 0

#dodanie spacji przed/po liczbach zeby mozna je bylo potem pociac dla funkcji wywalania zer
    else:
        counter = 1
        dzialanie = re.sub('(\\d+)', ' \\1 ', dzialanie)

# wywalam wiodace zera jezeli gdzies sa
        skladowe = dzialanie.split()
        bez_wiodacych_zer = list(map(wywal_zera, skladowe))
        dzialanie = ''.join(bez_wiodacych_zer)

# wywalam litery, znaki specjalne itd
        dzialanie = re.sub('[a-zA-Z,:%$#@!&^()=_" "]','', dzialanie)

#jezel to kolejne dzialanie to przenies do niego wynik poprzedniego
        if wynik == 0:
# jezeli znajdziesz niedozwolony podwojny operator w srodku dzialania to nie licz
            if str(dzialanie).find("++") != -1 or str(dzialanie).find("+*") != -1 or str(dzialanie).find("+/") != -1 \
                    or str(dzialanie).find("-+") != -1 or str(dzialanie).find("-*") != -1 or str(dzialanie).find("-/") != -1 \
                    or str(dzialanie).find("/+") != -1 or str(dzialanie).find("/*") != -1 or str(dzialanie).find("//") != -1 \
                    or str(dzialanie).find("*+") != -1 or str(dzialanie).find("*/") != -1:
                print("Invalid operator!")
            else:
                wynik = eval(dzialanie)

#Sprawdzenie czy sa tylko dopuszczalne operatory i czy nie ma podwojnych operatorow na poczatku i w srodku (** i operajce z ujemnymi sa dozwolone)
        else:
#Kolejne dzialanie po pierwszym musi zaczynac sie operatorem
            if str(dzialanie)[0] == "+" or str(dzialanie)[0] == "-" or str(dzialanie)[0] == "/" or str(dzialanie)[0] == "*":
                if str(dzialanie).find("++") != -1 or str(dzialanie).find("+*") != -1 or str(dzialanie).find("+/") != -1 \
                        or str(dzialanie).find("-+") != -1 or str(dzialanie).find("-*") != -1 or str(dzialanie).find("-/") != -1 \
                        or str(dzialanie).find("/+") != -1 or str(dzialanie).find("/*") != -1 or str(dzialanie).find("//") != -1 \
                        or str(dzialanie).find("*+") != -1 or str(dzialanie).find("*/") != -1:
                        print("Invalid operator!")
                else:
                    wynik = eval(str(wynik) + dzialanie)
            else:
                print("No valid operator")




print("Basic semi fool-proof continuous calculator")
print("Type 'quit' to exit the program. Type 'c' to reset")
print("Calculator will ignore letters, wrong operators, double operators, special characters and will remove any leading zeroes from numbers")
print("Do note that operations as x--y are still totally valid")


while loop:

    przeliczaj()

