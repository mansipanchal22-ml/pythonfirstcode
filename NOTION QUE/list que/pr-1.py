str = ["aaabb", "cccdd"]

output = []

for word in str:
    result = ""
    count = 1

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            count += 1
        else:
            result += word[i - 1] + f"{count}"
            count = 1

    # છેલ્લા character માટે
    result += word[-1] + f"{count}"

    output.append(result)

print(output)