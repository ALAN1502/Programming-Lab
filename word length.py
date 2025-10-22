list=input("Enter a lsit of words separated by spaces:").split(" ")
longest_length=0
for word in list:
    if len(word)>longest_length:
        longest_length=len(word)
        long_word=word
print("The longest word is",long_word)
print("The lenth of the longest word is:",longest_length)