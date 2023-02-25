def student_count(ma_liste: list) -> list:
    student = []
    new_list = [] 
    for elt in ma_liste:
        new_list.append(elt.lower())

    for sex1 in new_list:
        if sex1 == "male":
            student.append((sex1, new_list.count(sex1)))
            break

    for sex2 in new_list:
        if sex2 == "female":
            student.append((sex2, new_list.count(sex2)))
            break
    return student


students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
print(student_count(students))
