"""
    def sort_length(liste: list):
    for item in range(len(liste)):
        for i in range(len(liste) - 1):
            if len(liste[i]) > len(liste[i+1]):
                liste[i], liste[i+1] = liste[i+1], list[i]
    return print(liste)


names = ["Peter", "Jon", "Andrew"]
sort_length(names)
"""