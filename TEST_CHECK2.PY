def gamble(w, x, y, z):
    plays = 0 
    cycle = 0
    machinea = x
    machineb = y
    machinec = z
    while w!= 0:
        w -= 1
        plays += 1
        if cycle == 0:
            machinea += 1
            cycle += 1
        elif cycle == 1:
            machineb += 1
            cycle += 1
        else: 
            machinec += 1
            cycle = 0
        if machinea == 35:
            w += 30
            machinea = 0
        if machineb == 100:
            w += 60
            machineb = 0
        if machinec == 10:
            w += 9 
            machinec = 0
    print ("Martha plays", plays, "times before going broke")
gamble(77, 4, 9, 3)