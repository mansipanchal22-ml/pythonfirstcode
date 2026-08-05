#Write a function that accepts **kwargs to print a formatted description of a person.

def person(**kwargs):
    print ("person details")
    print ("name:", kwargs["name"])
    print ("age:", kwargs["age"])
    print ("city:", kwargs["city"])
    
person(name="Mansi", age = 20, city="Ahemdabad")
    