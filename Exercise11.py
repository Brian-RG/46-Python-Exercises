def generate_n_chars(x,y):
    count=0
    string=""
    while count<x:
        count+=1
        string+=y
    return string

print("This program will return a string with n character you introduce, m times")
m=int(input("Introduce the number of times you want the character: "))
n=input("Introduce the character: ")
print(generate_n_chars(m,n))
