'''Q.5 Find the position of the word "AI" in the sentence "Machine Learning and AI are trending". Replace "AI" with "Artificial Intelligence" in the above sentence. Count how many times the word "data" appears in "data data mining and big data
'''
sentence = "Machine Learning and AI are trending"

print("Position of AI:", sentence.find("AI"))
new_sentence = sentence.replace("AI","Artificial Intelligence")
print("After Replacement:", new_sentence)

text = "data data mining and big data"
print("Count of 'data':", text.count("data"))


#find() 
#find the position

#replace()
#change the word

#count()
#counting the word
