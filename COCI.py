def honi(word):
    x=0
    y=0
    for i in range (len (word)):
        if word[i] == "HONI"[x]:
            x += 1
        elif x == 3:
            x=0
            y += 1 
    print(y)
honi(input("Input Phrase:"))