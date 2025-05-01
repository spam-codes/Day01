#Taking input the total number of students 
total_students = int(input("Enter The Number Of Students : "))
result =""
i=1
#taking input details of each student and calculating grades
while(total_students) :
    name = input(f"\n({i})-Enter Name Of The Student :")
    marks = int(input("Enter Marks :"))
    if marks>=80:
         std_grade = "A Grade"
    elif marks>=60:
         std_grade = "B Grade"
    elif marks>=50:
         std_grade = "C Grade"
    elif marks>=40:
         std_grade = "D Grade"
    else :
         std_grade = "Fail"
    result += (f"({i}){name} = {std_grade}\n")
    i+=1                       
    total_students-= 1
 #printing the final grades with name   
print("\nResult:-\n"+result)   
    