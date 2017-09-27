def Correct(string):
    spaces=0
    correction=""
    for c in string:
        if c==" ":
            spaces+=1
            if spaces>1:
                pass
            elif spaces==1:
                correction+=c
        elif c==".":
            correction=correction+c+" "
        else:
            correction+=c
            spaces=0
    return correction

frase="This   is  very funny  and    cool.Indeed!"
print(Correct(frase))
