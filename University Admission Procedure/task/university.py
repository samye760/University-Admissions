import copy

max_students = int(input())

departments = {
    "Biotech": [],
    "Chemistry": [],
    "Engineering": [],
    "Mathematics": [],
    "Physics": [],
}

applicants = []

with open("applicants.txt", "r") as apps:
    for app in apps:
        applicants.append(app.split())

applicants.sort(key=lambda x: (-float(x[2]), x[0], x[1]))

app_copy = copy.deepcopy(applicants)

choice = 7

bio = departments['Biotech']
chem = departments['Chemistry']
eng = departments['Engineering']
math = departments['Mathematics']
phys = departments['Physics']

while (len(departments['Biotech']) < max_students or len(departments['Chemistry']) < max_students
        or len(departments['Engineering']) < max_students or len(departments['Mathematics']) <
        max_students or len(departments['Physics']) < max_students) and choice < 10 and applicants:

    if len(bio) < max_students:
        bio1 = [x for x in sorted(app_copy, key=lambda x: (-max(((int(x[3]) + int(x[2])) / 2), int(x[6])), x[0], x[1]))
                if x[choice] == 'Biotech'][:max_students - len(bio)]

        bio.extend(bio1)

        for student in bio:
            if student in applicants:
                applicants.remove(student)

        app_copy = copy.deepcopy(applicants)

    if len(chem) < max_students:
        chem1 = [x for x in sorted(app_copy, key=lambda x: (-max(int(x[3]), int(x[6])), x[0], x[1]))
                 if x[choice] == 'Chemistry'][:max_students - len(chem)]

        chem.extend(chem1)

        for student in chem:
            if student in applicants:
                applicants.remove(student)

        app_copy = copy.deepcopy(applicants)

    if len(eng) < max_students:
        eng1 = [x for x in sorted(app_copy, key=lambda x: (-max(((int(x[5]) + int(x[4])) / 2), int(x[6])), x[0], x[1]))
                if x[choice] == 'Engineering'][:max_students - len(eng)]

        eng.extend(eng1)

        for student in eng:
            if student in applicants:
                applicants.remove(student)

        app_copy = copy.deepcopy(applicants)

    if len(math) < max_students:
        math1 = [x for x in sorted(app_copy, key=lambda x: (-max(int(x[4]), int(x[6])), x[0], x[1]))
                 if x[choice] == 'Mathematics'][:max_students - len(math)]

        math.extend(math1)

        for student in math:
            if student in applicants:
                applicants.remove(student)

        app_copy = copy.deepcopy(applicants)

    if len(phys) < max_students:
        phys1 = [x for x in sorted(app_copy, key=lambda x: (-max(((int(x[2]) + int(x[4])) / 2), int(x[6])), x[0], x[1]))
                 if x[choice] == 'Physics'][:max_students - len(phys)]

        phys.extend(phys1)

        for student in phys:
            if student in applicants:
                applicants.remove(student)

        app_copy = copy.deepcopy(applicants)

    choice += 1

for department in departments:

    if department == 'Biotech':
        departments[department].sort(key=lambda x: (-max(((int(x[3]) + int(x[2])) / 2), int(x[6])), x[0], x[1]))
        score1 = 3
        score2 = 2
    elif department == 'Chemistry':
        departments[department].sort(key=lambda x: (-max(int(x[3]), int(x[6])), x[0], x[1]))
        score1 = 3
        score2 = False
    elif department == 'Engineering':
        departments[department].sort(key=lambda x: (-max(((int(x[5]) + int(x[4])) / 2), int(x[6])), x[0], x[1]))
        score1 = 5
        score2 = 4
    elif department == 'Mathematics':
        departments[department].sort(key=lambda x: (-max(int(x[4]), int(x[6])), x[0], x[1]))
        score1 = 4
        score2 = False
    else:
        departments[department].sort(key=lambda x: (-max(((int(x[2]) + int(x[4])) / 2), int(x[6])), x[0], x[1]))
        score1 = 2
        score2 = 4

    with open(f"{department.lower()}.txt", 'w') as write_file:

        for student in departments[department]:

            try:
                write_file.write(' '.join([
                    student[0], student[1],
                    str(max(((int(student[score1]) + int(student[score2])) / 2), float(student[6]))) + '\n']))
            except ValueError:
                write_file.write(
                    ' '.join([student[0], student[1], str(max(float(student[score1]), float(student[6]))) + '\n']))
