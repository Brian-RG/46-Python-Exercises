#Lingo
word="tiger"
while True:
    regreso=""
    intento=input("")
    c=0
    x=len(intento)
    for c  in range(x):
        if intento[c]==word[c]:
            regreso=regreso+"["+intento[c]+"]"
        elif intento[c] in word:
            regreso+="("+intento[c]+")"
        else:
            regreso+=intento[c]
    print("clue: ",regreso)
    if intento==word:
        print(regreso)
        print("You did it!")
        break
