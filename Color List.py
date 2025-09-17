list_1=input("Enter first list of colors(comma separated):").split(",")
list_2=input("Enter second list of colors(comma separated):").split(",")
list_1=[c.strip() for c in list_1]
list_2=[c.strip() for c in list_2]
diff_colors=[c for c in list_1 if c not in list_2]
print("colors in list-1 but not in list-2:",diff_colors)
