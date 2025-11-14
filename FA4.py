n_stu = int(input("Enter number of students: "))
n_sub = int(input("Enter number of subjects: "))
class_score = 0

for n in range(1, n_stu + 1):
    total = 0
    print(f"\nStudent {n}")
    for k in range(1, n_sub + 1):
        score = int(input(f"Input score {k}: "))
        total += score
    stud_ave = total / n_sub
    print(f"Average for Student {n} = {stud_ave:.2f}")
    class_score += stud_ave

class_ave = class_score / n_stu
print(f"\nClass average = {class_ave:.2f}")