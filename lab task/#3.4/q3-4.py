#Q3. Print only consonants from the string "PYTHON".

word = "PYTHON"

for ch in word:
    if ch in "AEIOUaeiou":
        continue
    print(ch)
    