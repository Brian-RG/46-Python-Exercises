from Functions import archivo_valido
while True:
    path=input("Please, introduce the path: ")
    if archivo_valido(path):
        break
abrir=open(path,'r')
lineas=abrir.readlines()
for line in lineas:
    line = line.strip()
    print("checkin on ",line)
    reverse=line[::-1]
    print("reverse is",reverse)
    if reverse==line:
        print("hey, equal, so",line)
    else:
        print("not equal")
