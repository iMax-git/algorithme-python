string  = "Essai pour le package search"

def recherche(string,motif):
    for i in range(len(string)-len(motif)+1):
        find = True
        for j in range(len(motif)):
            if (string[i+j] != motif[j]):
                find = False
                break
        if (find):
            return i
    return -1
            
#print(recherche(string, "sea"))


def BMHDecalage(alphabet, motif):
    p = len(motif)
    d = {}
    for i in alphabet:
        d[i] = p
    for j in range(len(motif)):
        d[motif[j]] = (p - j-1)
    print(d)
        
#BMHDecalage("ACTG", "ATTAT")

def distancefin(lettre, motif):
    d = 0
    for i in range(len(motif)-1,-1,-1):
        if motif[i] == lettre:
            return d
        d+=1
    return d
    

#print(distancefin("M", "ATMTAT"))

def construitDecalage(alphabet, motif):
    decalage = {}
    maxi = len(motif)
    for l in alphabet:
        decalage[l] = maxi
    for l in motif:
        maxi -= 1
        decalage[l] = maxi
    return decalage
print(construitDecalage("ATCG", "ATT"))

print("-------------------------------")
def horspool(alphabet,motif,texte):
    decalage = construitDecalage(alphabet, motif)
    print(decalage)
    p = len(motif)
    print(p)
    n = len(texte)
    print(n)
    i = p-1
    print(i)
    while(i<=n):
        present = True
        for j in range(p):
            if(texte[i-j] != motif[p-j-1]):
                present = False
                i += decalage[texte[i-j]]-j
                print("!=" + str(i))
                break
        if(present):
            return i - p + 1
    return -1
print(horspool("ATCG", "ATT", "ATCATCATCGATTAGTC"))
        
        
print("-----------------")

def horspooldecalage(alphabet,motif):
    p = len(motif)
    d = {}
    for l in alphabet:
        print(l)
        d[l] = p
    print("-------------")
    for i in range(p):
        print(p)
        print(i)
        print(motif[i])
        d[motif[i]] = p-i-1
        print("-")
    print(d)
    
horspooldecalage("ATCG", "ATT")




