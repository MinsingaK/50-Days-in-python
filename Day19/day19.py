def words_count(string:str):
    num = string.split(' ')
    print(f"your string of words has {len(num)} words.")


words_count('je suis actuellement a ActivSpace.')


def count_element(string:str):
    string = string.replace(' ','')
    return print(f"Your sting of words has {len(string)} elements")


count_element('i love learning')