# to see adult or not
age = input("enter your age:")

if int(age) >= 18:
    print("you are an adult")
    print("you can vote")
elif 18 > int(age) >= 3:
    print("you are in school")
else:
    print("you are a child")
print("thank you")
