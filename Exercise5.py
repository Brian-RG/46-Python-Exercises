def translate(word):
    rovaspraket=""
    for c in word:
        if c in ['a','e','i','o','u',' ','',',']:
            rovaspraket+=c
        else:
            rovaspraket=rovaspraket+c+"o"+c

    return rovaspraket

#main
print("This program will translate any word or sentence in rovaspraket")
trans=input("Please, introduce what you want to translate")
print("The word/sentence translated is "+translate(trans))
