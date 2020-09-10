'''snooker.txt
Helyezes;Nev;Orszag;Nyeremeny
52;Akani Sunny;Thaiföld;118500
'''
import collections

class Snooker:
    def __init__(self, sor):
        helyezes, nev, orszag, nyeremeny = sor.strip().split(';')
        self.helyezes  = int(helyezes)
        self.nev       = nev
        self.orszag    = orszag
        self.nyeremeny = int(nyeremeny)

with open("snooker.txt", 'r', encoding='latin2') as f:
    fejlec = f.readline()
    lista = [Snooker(sor) for sor in f]  

#3. feladat
print( f'3. feladat: A világranglistán {len(lista)} versenyző szerepel.')

#4. feladat
öb = sum ( [ sor.nyeremeny for sor in lista ] )
öv = len(lista)

átlag = öb / öv
print( f'4. feladat: a versenyzők átlagosan {átlag:.2f} fontot kerestek.')

#5. feladat
lgnyeremeny = 0
for sor in lista:
    if sor.orszag == "Kína":
        if sor.nyeremeny > lgnyeremeny:
            lgnyeremeny = sor.nyeremeny
            nev0 = sor.nev
            helyezes0 = sor.helyezes
            
print( f'5. feladat: A legjobban kereső kinai versenyző:')
print( f'     Helyezés: {helyezes0}  ')
print( f'     Név: {nev0}  ')
print( f'     Ország: {sor.orszag}  ')
print( f'     Nyeremény összege: {lgnyeremeny*380} Ft  ')

#6. feladat
számláló = 0 
for sor in lista:
    if sor.orszag == "Norvégia":
        számláló = számláló + 1 
        if számláló > 0:
            print( f'6. feladat: A versenyzők között van norvég versenyző.')
        else:
            print( f'6. feladat: A versenyzők között nincs norvég versenyző.')
                    
#7. feladat
cnt = collections.Counter()
for sor in lista:
    cnt[sor.orszag] += 1
print( f'7. feladat: Statisztika')
for orszag , darab in cnt.items():
    if darab > 4:
        print(f'{orszag} - {darab} fő')