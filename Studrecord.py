students={
    "Anu":[85,90,78],
    "Gowri":[72,88,91],
    "Vishnu":[95,80,85]
}
for name, marks in students.items():
    total=sum(marks)
    average=sum(marks)/ len(marks)
    print(f"student: {name}")
    print(f"marks: {marks}")
    print(f"Total marks: {total}")
    print(f"average marks: {average:.2f}")
    print("."* 20)