'''Create a list of 5 fruits. Print the second and last fruit 
    - add "Mango" to the list. Remove the first element
    - sort the list alphabetically. Reverse it.'''

fruit = ["Apple","Banana","orange","Grapes","kiwi"]

print("second fruit:", fruit[1])
print("Last fruit:", fruit[-1])

#add mango
fruit.append("Mango")
print("After adding Mango:", fruit)

#remove first element
fruit.pop(0)
print("after removing first element:", fruit)

#sort alphabetically
fruit.sort()
print("sort alphabetically:", fruit)

#reverse the list
fruit.reverse()
print("reverse list:", fruit)

