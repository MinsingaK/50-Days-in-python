def longuest_value(d:dict):
    longuest = max(d.values(),key=len)
    return longuest

fruits={'fruit':'apple','color':'green'}
print(longuest_value(fruits))