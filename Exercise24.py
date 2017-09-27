suffix=("ch","sh","o","s","x","z")
def make_3sg_person(word):
    if word.endswith(suffix):
        word=word+"es"
    elif word.endswith("y"):
        word=word[:-1]+"ies"
    else:
        word+="s"
    return word

print (make_3sg_person("try"))
print(make_3sg_person("brush"))
print(make_3sg_person("run"))
print(make_3sg_person("fix"))
