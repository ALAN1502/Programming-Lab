nums=list(map(int,input("Enter the integers separated by space:").split()))
result=["over" if n>100 else n for n in nums]
print("Modified list=",result)