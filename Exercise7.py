def Reverse(text):
    new=""
    v=len(text)
    while v>0:
        v-=1
        new+=text[v]
    return new

rev=input("Please, introduce a text: ")

print(Reverse(rev))
