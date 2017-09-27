import random
list_of_pokemon=["audino", "bagon", "baltoy", "banette", "bidoof", "braviary", "bronzor", "carracosta", "charmeleon",
"cresselia", "croagunk", "darmanitan", "deino", "emboar", "emolga", "exeggcute", "gabite",
"girafarig", "gulpin", "haxorus", "heatmor", "heatran", "ivysaur", "jellicent", "jumpluff", "kangaskhan",
"kricketune", "landorus", "ledyba", "loudred", "lumineon", "lunatone", "machamp", "magnezone", "mamoswine",
"nosepass", "petilil", "pidgeotto", "pikachu", "pinsir", "poliwrath", "poochyena", "porygon2",
"porygonz", "registeel", "relicanth", "remoraid", "rufflet", "sableye", "scolipede", "scrafty", "seaking",
"sealeo" ,"silcoon", "simisear", "snivy", "snorlax", "spoink", "starly", "tirtouga", "trapinch", "treecko",
"tyrogue", "vigoroth", "vulpix", "wailord", "wartortle", "whismur", "wingull", "yamask"]

No=["f","o","q","u","x","z","2"]

def pokemon_game(word):
    f_election=""
    s_election=""
    selected=[]
    estado=""
    time=0
    while True:
        while True:
            m=len(s_election)
            m-=1
            f_pok=random.randint(0,69)
            f_election=list_of_pokemon[f_pok]
            if time==0:
                time+=1
                print("Player One: ",f_election)
                selected.append(f_election)
                break
            elif s_election[m] in No:
                    print("There's no pokemon with '",s_election[m],"' in the list")
                    estado="lost"
                    break
            elif f_election[0] == s_election[m]:
                if f_election in selected:
                    print("player One: ",f_election)
                    print("You lost!")
                    estado="lost"
                    break
                else:
                    print("Player One: ",f_election)
                    selected.append(f_election)
                    break
        if estado=="lost":
            break
        while True:
            n=len(f_election)
            n-=1
            if f_election[n] in No:
                print("There's no pokemon with '",f_election[n],"' in the list")
                estado="lost"
                break
            s_pok=random.randint(0,69)
            s_election=list_of_pokemon[s_pok]
            if s_election[0] == f_election[n]:
                if s_election in selected:
                    print("Player two: ",s_election)
                    print("You lost!")
                    estado="lost"
                    break
                else:
                    print("Player two: ",s_election)
                    selected.append(s_election)
                    break
        if estado=="lost":
            break

#mamoswine
word=""
pokemon_game(word)
