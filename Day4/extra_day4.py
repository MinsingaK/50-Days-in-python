def word_index(liste:list):
    for elt in liste:
        for i in range(len(liste)-1):
            if len(liste[i]) == len(liste[i+1]):
                return print("tous les mots ont la meme taille")
            elif len(elt) == len(max(liste)):
                l = liste.index(elt)
                return print(f"Le mot le plus long a pour indice {l}")

words1 = ["Hate","vengeance","remorse"]
words2 = ["Love", "Hate","papa","mama"]
word_index(words1)