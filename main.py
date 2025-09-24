# key : value
student = {
    "name": "Gipsz Jakab",
    "age": 25,
    "skills": ["Python", "Linux", "Git"]
}

print(student["name"]) # Gipsz Jakab
print(student["age"])
print(student["skills"])

students = [
    {
        "name": "Gipsz Jakab",
        "age": 25,
        "skills": ["Python", "Linux", "Git"]
    },
    {
        "name": "Para Zita",
        "age": 28,
        "skills": ["C#", "Windows", "Git"]
    }
]

for s in students:
    print(s["name"])