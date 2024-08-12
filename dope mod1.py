grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johny','Bilbo','Steve','Khendrik','Aaron'}
print(grades,students)
middle_mark = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
print(middle_mark)
alphabet = sorted(students)
print(alphabet)
journal = tuple(zip(middle_mark,alphabet))
print(journal)
