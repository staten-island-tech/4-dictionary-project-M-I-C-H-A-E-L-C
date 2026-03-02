def lang(sent):
    s=0
    t=0
    for i in sent:
        if i == "s" or i =="S":
            s +=1
        elif i == "t" or i =="T":
            t +=1
    if s>= t: 
        print("french")
    else: 
        print("english")
lang("The red cat sat on the mat. Why are you so sad cat? Don't ask that.")
lang("Lorsque j'avais six ans j'ai vu, une fois, une magnifique image, dans un livre")
