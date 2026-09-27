# 4. **Combined**    
#Given a list of strings `["Python", "is", "awesome", "and", "powerful"]`:
    
#- Use `filter()` to keep only words longer than 3 characters.

words = ["Python", "is", "awesome", "and", "powerful"]
longer_words = list(filter(lambda  w: len(w) > 3,words))
print(longer_words)

#- Use `map()` to convert them to uppercase.




#- Use `sorted()` to sort the result alphabetically.
#- Use `reduce()` to concatenate them into a single string separated by spaces.

