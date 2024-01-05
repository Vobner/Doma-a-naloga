import random as rnd

while True:
    faktor_a = rnd.randint(1, 10)
    faktor_b = rnd.randint(1, 10)
    pravi_rezultat = faktor_a * faktor_b

    izhod = False
    stevilo_napak = 0
    while stevilo_napak < 3:
        moj_odgovor = input(f' {faktor_a} * {faktor_b} = ')
        if moj_odgovor.upper() == 'Q' or len(moj_odgovor) == 0:
            izhod = True
            break
        elif int(moj_odgovor) == pravi_rezultat:
            print('ODLIČNO! le tako naprej.')
            break
        else:
            if stevilo_napak == 2:
                print(f'pravilen rezultat je {pravi_rezultat} ')
            else:
                print('poskusi znova')
            stevilo_napak += 1
    if izhod:
        break
