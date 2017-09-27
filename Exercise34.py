from Exercise21 import freq_listing
import string
path="prueba.txt"
archivo=open(path,'r')
text=archivo.read()
text=text.strip()
dic=freq_listing(text)
alphabet=string.ascii_lowercase
for i in alphabet:
    if i in dic:
        print(i,": ",dic[i])
