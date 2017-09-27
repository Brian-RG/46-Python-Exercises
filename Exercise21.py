def freq_listing(word):
    frequency={}
    for c in word:
        if c in frequency:
            if c==" ":
                pass
            else:
                frequency[c]+=1
        else:
            if c==" ":
                pass
            else:
                frequency[c]=1
    return frequency


def main():
    palabra=input("Introduce una palabra:")
    print(freq_listing(palabra))

if __name__=="__main__":
    main()
