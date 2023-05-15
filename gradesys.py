def gradesys(mark):
    if mark >= 90 :
        return "your grade is an A"
    elif mark >=80 and mark <90:
        return "your grade is B" 
    elif mark >=70 and mark <80:
        return "your grade is C" 
    elif mark >=60 and mark <70:
        return "your grade is D" 
    elif mark >=50 and mark <60:
        return "your grade is D" 
    else:
        return "You have failed bwana!!"

mark = 46

print(gradesys(mark))