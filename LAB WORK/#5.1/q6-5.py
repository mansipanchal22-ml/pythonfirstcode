#q-6 split "apple,banana,grapes" into a list.
#- join the list["python","is","awesome"] into a sentence using sentence.
#- split a multiline string into separate lines and print them one by one

#split() string convert into list
#join() list convert into string
#splitlines() all multiline string convert into single line in split

fruits = "apple,banana,grapes"
fruit_list = fruits.split(",")
print(fruit_list)

words  = ["Python", "is", "awesome"]
sentence = " ". join(words)
print(sentence)

text = """Hello
Welcome
Python"""

lines = text.splitlines()

for line in lines:
    print(line)
    