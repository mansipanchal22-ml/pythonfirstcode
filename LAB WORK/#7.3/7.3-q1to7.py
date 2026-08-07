# Q.1 Create a 1D array (list) with five integer elements. Display the array using a loop.

arr = [11,22,33,44,55]

for i in arr :
    print(i)

#Q.2 Develop a program to calculate the sum of all elements in a 1D array separately.
print("\n");#answer space aye isliye kiya ye

sum = 0
for i in arr :
    sum+=i
    print(sum)

#Q.3 Create a program to insert a new element at a specific position in a 1D array.

arr = [11,22,33,44,55]
arr.insert(2, 35)
print(arr)

#Q.4 Write a program to delete an element by its value from a 1D array.

arr = [25,36,45,50,30]
arr.remove(36)
print(arr)

#Q-5 Develop a program to update an element in a 1D array based on its index.

a = int(input("Enter the number to update: "))
b = int(input("Enter the new number: "))
c = arr.index(a)

arr[c]=b
print(arr)

#Q.6 Implement a program to search for an element in a 1D array and return its index.

arr = [50,60,70,20,30]
x = 20

index = arr.index(x)
print("Index =",index)

#Q.7 Write a program to concatenate two 1D arrays into a single array.

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]

# print(arr1+arr2)

def findind(l):
    """
    Searches a list for a user-specified integer.

    Parameters:
    l (list): The list to search.

    Returns:
    int: The index of the element if found,
         otherwise returns "Element not found".
    """

    a = int(input("Enter the element to search: "))

    for i in range(len(l)):
        if a == l[i]:
            return i

    return "Element not found"


arr = [10, 20, 30, 40, 50]

print("Index =", findind(arr))