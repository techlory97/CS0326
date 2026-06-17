scelta = input("Scegli la figura geometrica (cerchio, quadrato, rettangolo, triangolo): ")
if scelta == "cerchio":
    raggio = float(input("Inserisci il raggio del cerchio: "))
    area = 3.14 * raggio ** 2
    print("L'area del cerchio è:", area)
elif scelta == "quadrato":
    lato = float(input("Inserisci il lato del quadrato: "))
    area = lato ** 2
    print("L'area del quadrato è:", area)
elif scelta == "rettangolo":
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    area = base * altezza
    print("L'area del rettangolo è:", area)
elif scelta == "triangolo":
    base = float(input("Inserisci la base del triangolo: "))
    altezza = float(input("Inserisci l'altezza del triangolo: "))
    area = (base * altezza) / 2
    print("L'area del triangolo è:", area)
else:
    print("Figura geometrica non valida.")
    
