#Pomocí cyklu for napiš program, který vypíše:
#0 na druhou je 0
#1 na druhou je 1
#2 na druhou je 4
#3 na druhou je 9
#4 na druhou je 16
#Jak pojmenuješ proměnnou cyklu?

cislo = 0
for x in range(5):
    print(cislo, "na druhou je", cislo ** 2)
    cislo = cislo + 1
