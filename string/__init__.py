'''
Created on 4 nov. 2020

@author: tdiard
'''

string = "Le confinmanne c kan"

def occurence(string, caractere):
    a = 0
    for lettre in string:
        a += 1
        if(lettre == caractere):
            return a
    return -1
    
print(occurence(string, "a"))
print("------------------------------------------")
def nmboccurence(string, caractere):
    a = 0
    for lettre in string:
        if(lettre == caractere):
            a += 1
    return a
    
print(nmboccurence(string, "a"))
print("------------------------------------------")
def recherche(motif,texte):
    for i in range(len(texte)-len(motif)+1):
        present = True
        for j in range(len(motif)):
            if (texte[i+j] != motif[j]):
                present = False
                break
        if(present):
            return i
    return -1

print(recherche("kan",string))
        
            
                