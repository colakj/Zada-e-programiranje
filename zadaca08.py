def pozdrav(ime):
    print("Pozdrav", ime +"!")

dobrodosao = lambda ime: print("Dobrodošao", ime+" !")

def treca_funkcija(funkcija):
    funkcija("Josipa")

treca_funkcija(pozdrav)
treca_funkcija(dobrodosao)
    
