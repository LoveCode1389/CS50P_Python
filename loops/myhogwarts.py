students = {
    "name": "house",
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": 'Gryffindor',
    "Draco": "Slytherin",
}

# my work(for design)
one = 0
n = []

for i in students:
    n.append(len(i))
one = max(n)
# my work(for design )

for student in students:
    faseleh = one - len(student)
    print(student + (' ' * faseleh), "|" ,students[student])
    if student == "name":
        print("--------------------")