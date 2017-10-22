#Pomoci cyklu for a prikazu if napis program, ktery z jednotlivych
#"X" a mezer vypise:

for i in range(5):
    if i==0 or i==5:
        print("X" * 6)
    else:
        print("X" + " " * 4 + "X")
