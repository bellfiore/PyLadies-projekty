#Napis program, ktery se zepta na 3 cisla a zjisti, jestli je jejich
#soucet vetsi nez 10

#print ("povrch krychle o straně 2852 cm", 6*2852**2, "cm2" )
#strana = int (input ("Zadej stranu krychle v cm: "))
#print ("povrch krychle o straně", strana, "je", 6*strana**2, "cm2")

cislo1 = int (input("Napis cislo1: "))
cislo2 = int (input("Napis cislo2: "))
cislo3 = int (input("Napis cislo3: "))
soucet = cislo1 + cislo2 + cislo3
if soucet > 10:
    print("Soucet je vetsi nez 10")
else:
    print("Soucet je mensi nez 10")
