def longuest_value(d:dict):
    longuest = max(d.values(),key=len)
    return print(f"the longuest value is {longuest}")

fruits={'fruit':'apple','color':'green'}
longuest_value(fruits)