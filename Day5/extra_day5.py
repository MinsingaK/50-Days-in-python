def student_count(listee:list)->list:
    """
        m=0
        f=0
    """
    liste = []
    new_list = [] 
    for elt in listee:
        new_list.append(elt.lower())

    for sex1 in new_list:
        if sex1 == "male":
            # m +=1
            liste.append((sex1,new_list.count(sex1)))
            break

    for sex2 in new_list:
        if sex2 == "female":
            # f +=1
            liste.append((sex2,new_list.count(sex2)))
            break
    return liste

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
print(student_count(students))