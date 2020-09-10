import collections

with open("snooker.txt", 'r', encoding='latin2') as f:
    lista = list()
    fejlec = f.readline()
    for sor in f:
        lista.append(sor.strip().split(";"))




#3. feladat
print( f'3. feladat: A világranglistán {len(lista)} versenyző szerepel')



#4. feladat
öb = sum ( [ int(sor[3]) for sor in lista ] )
öv = len(lista)

átlag = öb / öv

print( f'4. feladat: a versenyzők átlagosan {átlag:.2f} fontot kerestek')

#5. feladat
lgnyeremeny = 0
for helyezes,nev,orszag,nyeremeny in lista:
    if orszag == "Kína":
        if int(nyeremeny) > lgnyeremeny:
            lgnyeremeny = int(nyeremeny)
            nev0 = nev
            helyezes0 = helyezes
            
print( f'5. feladat: A legjobban kereső kinai versenyző:')
print( f'     Helyezés: {helyezes0}  ')
print( f'     Név: {nev0}  ')
print( f'     Ország: {orszag}  ')
print( f'     Nyeremény összege: {lgnyeremeny*380} Ft  ')

#6. feladat
számláló = 0 
for helyezes,nev,orszag,nyeremeny in lista:
    if orszag == "Norvégia":
        számláló = számláló + 1 
        if számláló > 0:
            print( f'6. feladat: A versenyzők között van norvég versenyző.')
        else:
            print( f'6. feladat: A versenyzők között nincs norvég versenyző.')
            

        
#7. feladat
cnt = collections.Counter()
for helyezes,nev,orszag,nyeremeny in lista:
    cnt[orszag] += 1
print( f'7. feladat: Statisztika')
for orszag , darab in cnt.items():
    if darab > 4:
        print(f'{orszag} - {darab} fő')

    




            
            
            
        
            
            
            
        
            
            
                    



    