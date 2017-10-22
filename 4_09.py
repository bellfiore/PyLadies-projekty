#Pomoci cyklu for a parametru end pro print napiš program, který
#postupne z jednotlivých "X" vypise:
#X X X X X
#print (1, "dva", end="")
#pocet hodnot X = a
#pocet radku X = b

#UTEKLO MI JEDNO X Z POSLEDNI RADKY!!!!

hodnota = "X"
for a in range(5):
    print(hodnota)
    for b in range(5):
        print(hodnota, end=" ")
