n=['sonam',52,56,60]
name=n[0]
scores= n[1:]
students_marks={}
sum=0
for i in scores:
    sum+=i
score=sum/3
score = float(score)
students_score=students_marks[name]=score
print (students_score)