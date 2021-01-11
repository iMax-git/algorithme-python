'''
Created on 2 nov. 2020

@author: tdiard
'''



classeDeNSI = [ {
    "nom" : "Pierre",
    "notes" : [10, 12, 14],
    "specialites" : ("NSI", "Math")
    }, {
    "nom" : "Paul",
    "notes" : [11, 12],
    "specialites" : ("NSI", "Math")
    }, {
    "nom" : "Jacques",
    "notes" : [15, 18, 17],
    "specialites" : ("NSI", "Anglais")
    }, {
    "nom" : "Jean",
    "notes" : [12,15, 13, 17],
    "specialites" : ("Physique","NSI")
    }
]


D = classeDeNSI
print(D[1]["notes"][0])
print("------------------------------------------")
   
def list(value):
    print("----(Liste des eleves)----")
    for name in value:
        print(name["nom"])

list(D)
print("------------------------------------------")

def findnote(classe,nom):
    for i in classe:
        eleve = i["nom"]
        if(eleve == nom):
            note = i["notes"]
            print(note)
            
findnote(D, "Jacques")


print("------------------------------------------")

def bestnote(classe):
    rsl = 0
    for i in classe:
        notes = i["notes"]
        for note in notes:
            if(note > rsl):
                rsl = note
    print(rsl)
            
bestnote(D)

print("------------------------------------------")

def getSpe(classe):
    rsl = []
    for i in classe:
        spe = i["specialites"]
        for info in spe:
            if(info not in rsl):
                rsl.append(info)
    print(rsl)
        
getSpe(D)
            
        