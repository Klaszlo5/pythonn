#semmi megoldas
def pontok(lap)->int:
    pontok:int = 0
    for i in range(len(lap)):
        pontok += lap[i];
    return pontok
def eredmeny(egy, ketto):
    napok = pontok(egy)
    jatekos = pontok(ketto)
    for jatekos in range(napok):
        napok[jatekos] += napok[jatekos]
    if napok > 21 and jatekos < 2:
        print("napok jatekos")
#megjegyzes

