import functools
def Find_longest_word(lista):
    return functools.reduce(lambda x,y: x if x>=y else y,lista)
lista=[]
while True:
    word=input("Introduce una palabra: ")
    if word=="break":
        break
    else:
        lista.append(len(word))
print (Find_longest_word(lista))
