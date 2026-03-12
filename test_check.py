plays = 0 
def gamble (w, x, y, z):
    machinea = 0
    machineb = 0
    machinec = 0
    while w != 0:
        if w >= x:
            machine += x
            plays += x 
            if machine >= 35:
                w += 30
                machinea = machinea - 35
            if w == y:
                machineb += y 
                w = w - y
                plays += y
                if machineb >= 100:
                    w += 100
                    machineb = machineb - 100
            if w >= z:
                machinec += z
                w = w - z
            if machinec >= 10:
                w += 9
                machinec = machinec - 10
