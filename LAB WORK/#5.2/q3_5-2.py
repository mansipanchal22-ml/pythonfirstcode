#create a list and a tuple both containing the same 3 items.
#-try changing the first item of each.
#-discuss the error(in case of tuple) and explain why it happens.


lst = [10,20,30,40,50]
tup = (10,20,30,40,50,)

print(lst,tup)

#chnge first item for the list
lst[0] = 100
print("update lst:", lst)

'''#chnge first item for the tuple
#explanation = tuple is immutable is liye ek bar tuple create ho jaye fir usme chnges nhi kr skte 
but hum try krte tub aese per error aa jati he
tup[0] = 100
print("update tup:", tup)'''