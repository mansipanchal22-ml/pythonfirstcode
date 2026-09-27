# 5. *Challenge*    
#Write a function that takes a list of dictionaries 
#(students with "name" and "score") and returns the 
#names of students who scored above 80, sorted by score in descending order. Use filter(),
#sorted(), and map() (or a combination).

def top_students(students):
    # 1. Filter students with score > 80
    high_scorers = filter(lambda s: s["score"] > 80, students)
    
    # 2. Sort by score in descending order
    sorted_scorers = sorted(high_scorers, key=lambda s: s["score"], reverse=True)
    
    # 3. Extract just the names
    return list(map(lambda s: s["name"], sorted_scorers))