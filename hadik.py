import time

while True:
    hadik = ("**********")
    n = [0]
    increasing = True

    while increasing:
        time.sleep(0.1)
        i = len(n) * "_"
        pole = i + hadik
        if len(n) < 20:
            n.append(1)
            print(pole)
        elif len(n) == 20:
            print(pole)
            increasing = False

    while not increasing:
        time.sleep(0.1)
        i = len(n) * "_"
        pole = i + hadik
        if len(n) >1:
            n.remove(1)
            print(pole)
        else:
            increasing = True
        
