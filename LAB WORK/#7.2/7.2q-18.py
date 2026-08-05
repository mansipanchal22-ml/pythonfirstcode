# Q.18 Create a function that takes a list of words and returns two lists: one with words starting with vowels and the other with words starting with consonants.

def split_words(words):
    vowel_word = []
    consonant_word = []

    for word in words:
        if word[0].lower() in "aeiou":
            vowel_word.append(word)
        else:
            consonant_word.append(word)

    return vowel_word, consonant_word
words = ["Cat","Yellow","Orange","Purple","Black"]

v, c = split_words(words)

print("vowel Words =", v)
print("Consonant =", c)