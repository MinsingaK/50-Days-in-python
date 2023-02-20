def dico_names(liste:list):
    dico = {}
    empty_list = []
    for name in liste:
        if name.startswith("S"):
            empty_list.append(name)
            dico.update({name:empty_list.count(name)})
    return dico
names = ["Joseph","Nathan","Sasha","Kelly","Muhammad","Jabulani","Sera","Patel","Sera"]
print(dico_names(names))
    