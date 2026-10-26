
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()
lines = text.splitlines()
characters = len(text)

print("Total Words:", len(words))
print("Total Lines:", len(lines))
print("Total Characters:", characters)
