
import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Student Details")
print("----------------")
print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])
print("Skills:", ", ".join(data["skills"]))
