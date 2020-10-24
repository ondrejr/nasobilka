import random
import datetime

znak_nasobeni = '.'
max_cislo_umi = 50
max_vysledek = 100
a_zacina_od = 3    	             # b zacina od 0
soubor_ini = 'nasobilka.ini'
fn = datetime.datetime.now().strftime("%m%d%H%M")

class read_ini():
    """ načtení ini
    """
    def __init__(self):
        try:
            with open(soubor_ini, "r", encoding="utf-8") as dest:
                inis = dest.readlines()
            for vals in inis:
                val = vals.split('=')
                if val[0] == 'jmeno':
                    self.jmeno_uzivatele = val[1]
            print('spouští uživatel {}'.format(self.jmeno_uzivatele))
            self.pokr = True    
        except:
            print('soubor {} se jménem uživatele neexistuje'.format(soubor_ini))
            self.pokr = False

    def pokr():
        """ načtení ini v pořádku - možno pokračovat ?
        """
        return self.pokr

    def jmeno_uzivatele():
        """ jméno uživatele z ini
        """
        return self.jmeno_uzivatele


def gen_a_b():
    """ vygeneruje a, b
        a       je v intervalu 0           - max_cislo
        b       je v intervalu a_zacina_od - max_cislo
    """
    pom = max_vysledek / 10
    rnd_a = random.random() * pom
    a = int(rnd_a + a_zacina_od)
    if a >= pom - a_zacina_od:
        a -= a_zacina_od
    #print()
    #print('{} {}'.format(rnd_a, a_zacina_od))
    b = int(random.random()* pom)
    return a, b
    

ini = read_ini()            


while ini.pokr:
    try:
        a, b = gen_a_b()
        print()

        if a * b > max_cislo_umi:
            vysl = '{} ještě neumí {} {} {} = {}'.format(ini.jmeno_uzivatele, a, znak_nasobeni, b, a * b)
            v = 0
        else:
            vysl = 'je to špatně'
            print('zadej výsledek {} {} {}: '.format(a, znak_nasobeni, b))
            v = int(input())
        if v == a * b:
            vysl = 'je to dobře'

        print('{}'.format(vysl))
        cas = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        with open('vysledek{}.txt'.format(fn), "a+", encoding="utf-8") as dest:
            dest.write('{}       {} x {} = {}       {}\n'.format(cas, a, b, v, vysl))

        print()
    except ValueError:
            print()
            print('neplatné zadání')
            #exit(0)
