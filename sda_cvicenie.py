menu = {
    "Pivo" : 2,
    "Kofola" : 2,
    "Pizza" : 12,
    "Polievka" : 1
}
platim_za = []

def platba(menu):
    while True:
        platim = input("Za čo chceš platiť?:")
        if platim == "Vsetko zaplatene":
            return False
        elif platim not in menu and platim != "Vsetko" and platim != "Vsetko zaplatene":
            print("Také tu nemáme")
        elif platim == "Vsetko":
            return print(platim_za)
        else:
            for k,n in menu.items():
                if platim == k:
                    platim_za.append(n)
        
def platenie():
    print("Potrebujes zaplatiť:",sum(platim_za))
    spropitne = int(input("Koľko '%' spropitneho??"))
    celkove_spropitne = print("Platba s dýškem",(sum(platim_za) + ((sum(platim_za)* spropitne / 100))))
    return celkove_spropitne
       
def koniec_platby():
    platba(menu)



playing = True
while playing:
    for n in range(int(input("Koľko ľudí ide platiť?:"))):
        playing = koniec_platby()
        platenie()
        





