#Set total to zero
#Set grade counter to one
#While grade counter is less than or equal to ten
#Input the next grade
#Add the grade into the total
#Set the class average to the total divided by ten
#Print the class average.


total = 0
grade_counter = 1

while grade_counter <= 10:
    newGrade = int(input("enter new grade"))
    total += newGrade
    grade_counter += 1


classAvg = total / 10
print(classAvg)