import random as rnd

while True:
    faktorA = rnd.randint(1, 10)
    faktorB = rnd.randint(1, 10)
    praviRezultat = faktorA * faktorB

    izhod = False
    steviloNapak = 0
    while steviloNapak < 3:
        mojOdgovor = input(f' {faktorA} * {faktorB} = ')
        if mojOdgovor.upper() == 'Q' or len(mojOdgovor) == 0:
            izhod = True
            break
        elif int(mojOdgovor) == praviRezultat:
            print('ODLIČNO! Le tako naprej.')
            break
        else:
            if steviloNapak == 2: 
                print(f'pravilen rezultat je {praviRezultat} ')
            else:
                print('poskusi znova')
            steviloNapak += 1
    if izhod:
        break 
