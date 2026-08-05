#write a UDF that takes a string as input and returns the frequency of each character in the string as a dictionary.

def char_frequency(text):
    freq = {}

    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

string = input("Enter a string: ")
result = char_frequency(string)

print("Character frequency:")
print(result)