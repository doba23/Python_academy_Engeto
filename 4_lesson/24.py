students = ['Adam, Baker','Chelsea, Archer',
            'Marcus, Archer','Oliver, Cook',
            'Alex, Dyer', 'Sandra, Turner',
            'Ann, Fisher', 'Glenn, Hawkins',
            'Samuel, Baker','Clara, Slater',
            'Tyler, Hunt', 'Alex, Smith',
            'Clara, Woodman','Abraham, Mason',
            'Marcus, Sawyer','Alex, Glover',
            'Glenn, Cook','Clara, Fisher',
            'Alfred, Dyer', 'Curt, Head',
            'Oliver, Slater','Alex, Mason',
            'Tyler, Fisher','Ann, Parker',
            'Samuel, Hawkins', 'Ann, Woodman',
            'Sandra, Slater', 'Curt, Dyer']

print('Extracting ...')

#split
names = []
surnames = []
students_list = []
while students:
    students_list.append (students[0].split(', '))
    students = students[1:]

#store as list
while students_list:
    names.append(students_list[0][0])
    surnames.append(students_list[0][1])
    students_list = students_list[1:]

#convert to set (not reapeat names)
names = set(names)
surnames = set(surnames)

print('Unique names:', names)
print('Unique surnames:', surnames)
