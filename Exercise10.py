def is_member(x,y):
    finish="false"
    for m_x in x:
        if m_x in y:
            finish="true"
            break
    for m_y in y:
        if m_y in x:
            finish="true"
            break
    return finish
Lista1=[]
Lista2=[]
print("Introduce 2 list, this program will check them, if there is at least one member in common, will print 'true', otherwise, will print'false'")
print("Let's start with the first list")
print("Write 'break' to finish")
while True:
    m=input("Introduce a member: ")
    if m=="break":
        break
    else:
        Lista1.append(m)
print("Now, let's start with the second one")
print("Write 'break' to finish")
while True:
    n=input("Introduce a member: ")
    if n=="break":
        break
    else:
        Lista2.append(n)
print(is_member(Lista1,Lista2))
