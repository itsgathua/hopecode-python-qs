items = input("Enter hyphen-separated words: ")

words = items.split("-")
words.sort()

result = "-".join(words)

print(result)
