from random import randint

import aneta_albrechtova as ai

def vstup():
    cislo_policka=int(input("Zadej pole kam chces hrat: " ))
    return cislo_policka

def tah_hrace(pole):

    while True:
        while True:
            try:
                cislo_policka = vstup()
                break #kdyz zada dobre cislo - break - prerusim cyklus- jde na if
            except ValueError:
                print("Nezadal jsi cele cislo.")
                continue #continue v cyklu

        if cislo_policka <= len(pole) and cislo_policka > 0:
            #historie.append(cislo_policka-1)
            symbol_hrace='o'
            if '-' in pole[cislo_policka-1]:
                pole=pole[:cislo_policka-1] + symbol_hrace + pole[cislo_policka:]
                #pole[cislo_policka-1]=symbol_hrace
                return pole
            else:
                print("Zadej jinou pozici. Tato je obsazena.")
        else:
            print("Zadej jinou pozici. Pozice je mimo range.")



def vyhodnot(pole):
    if 'xxx' in pole:
        #print ('Vyhral hrac s krizky.')
        return 'Vyhral hrac s krizky.'
    elif 'ooo' in pole:
        #print('Vyhral hrac s kolecky.')
        return 'Vyhral hrac s kolecky.'
    elif '-' not in pole:
        #print('Remiza!')
        return 'Remiza!'
    else:
        print('Hra jeste neskoncila!')
        return '!'




def hra(pole):
    pocet_kol=0
    #print("pocet kol:", pocet_kol)
    aktualni_stav='!'
    while aktualni_stav=='!':
        pole=ai.tah_pc(pole, 'x')
        pocet_kol += 1
        #print("pocet kol:", pocet_kol)
        print(pole)
        aktualni_stav=vyhodnot(pole)
        if  aktualni_stav!='!':
            print(aktualni_stav)
            break
        pole=tah_hrace(pole) #argument - skutecny parametr - pass by value - modifikujes ykopirovanou hodotu - musis mit returny
                                                                   # , pass by reference - v ramce predava se adresa, - nemusis mit returny - jako list
                                                                   # pokud mam pole [3]=5, tak jen modifikuju to pole, ktere uz znam a nemusim ho vracet
                                                                   # pokud pole = 5, tak vytvorim nove pole, na ktere nakonec ukazuju tim promenou pole
                                                                                    #, de musim pouzivat return, rpotoye jinak pc nevi, co vracim, ktery y tech dvou
        pocet_kol += 1
        #print("pocet kol:", pocet_kol)
        print(pole)
        aktualni_stav=vyhodnot(pole)
