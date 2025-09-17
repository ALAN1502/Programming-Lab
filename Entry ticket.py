age=int(input("Enter the Age"))
if age<10:
    print("Rate=7")
elif age>=10 and age<60:
    print("Rate=10")
elif age>=60:
    print("Rate=5")
else:
    print("invalid")
