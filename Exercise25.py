vowels=["a","e","i","o","u"]
exceptions=["be","see","flee","knee"]
def make_ing_form(word):
    if word.endswith("ie"):
            word=word[:-2]+"ying"
    elif word.endswith("e"):
        if word not in exceptions:
            word=word[:-1]+"ing"
        else:
            word=word+"ing"
    elif word[0] not in vowels:
        if word[1] in vowels:
            if word[2] not in vowels:
                word=word+word[2]+"ing"
    else:
        word+="ing"
    return word

print(make_ing_form("lie"))
print(make_ing_form("see"))
print(make_ing_form("move"))
print(make_ing_form("hug"))
