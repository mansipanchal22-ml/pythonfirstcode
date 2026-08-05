# Develop a program where a UDF accepts *args and filters out the strings from the arguments.
# -Return a tuple of filtered values (strings in one tuple, numbers in another).

def filter_values(*args):
    string = ()
    number = ()
    
    for i in args:
        if type(i) == str:
            string = string + (i,)

        elif type(i) == int:
            number = number + (i,)

    return string, number

str,int = filter_values("mansi", 22,"lalit", 33,"veer", 44)

print("string :", str)
print("number :", int)