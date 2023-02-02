print("Give a grade:")
grade = int(input())

while grade < 0 or grade > 5:
    print("Give a grade:")
    grade = int(input())

if grade == 0:
    print("Fail")
elif grade == 1 or grade == 2:
    print("Weak")
elif grade == 3 or grade == 4:
    print("Good")
elif grade == 5:
    print("Excellent")
