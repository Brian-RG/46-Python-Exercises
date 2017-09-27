def is_member(list,element):
    for e in list:
        if e==element:
            return True
    return False
Lista=[]
print("This program will show if a value you enter is in a list of values previously established")
print("write break to finish")
while True:
    v=input("Introduce the member: ")
    Lista.append(v)
    if v=="break":
        break
print("now, we'll check if any character/word you introduce is part of this list")
print("Write 'break' to finish entering words")
while True:
    mem=input("Introduce you word: ")
    if mem=="break":
        break
    print(is_member(Lista,mem))
