characters = str(input("Enter character: "))
if 'A' <= characters <= 'Z':
    print("Upper case")
elif 'a' <= characters <= 'z':
    print("Lower case")
else:
    print("Not english letter")
