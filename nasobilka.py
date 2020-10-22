import random
import datetime

fn = datetime.datetime.now().strftime("%m%d%H%M")

while True:
    try:
        #print('zadejte a: ')
        a = int((random.random()*8)+2)
        b = int(random.random()*10)

        if a*b > 50:
            vysl = 'Aleš ještě neumí {} . {} = {}'.format(a,b,a*b)
            v = 0
        else:
            vysl = 'je to špatně'
            print('zadej výsledek {} . {}: '.format(a, b))
            v = int(input())
        if v == a*b:
            vysl = 'je to dobře'
        #print('výsledek a*b: {}, {}'.format(a*b, vysl))
        print('{}'.format(vysl))
        cas = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        with open('vysledek{}.txt'.format(fn), "a+", encoding="utf-8") as dest:
            dest.write('{}       {} . {} = {}       {}\n'.format(cas, a, b, v, vysl))

        print()
    except ValueError:
            print()
            print('neplatné zadání')
            #exit(0)
