amount = int(input("Enter the money you want: "))
a = amount // 500
amount = amount % 500
b = amount // 200
amount = amount %200
c = amount // 100
amount %= 100
d = amount // 50
amount %= 50
e = amount // 20
amount %= 20
f = amount // 10
amount %= 10
print("you will get 500 rupees",a,"times")
print("you will get 200 rupees",b,"times")
print("you will get 100 rupees",c,"times")
print("you will get 50 rupees",d,"times")
print("you will get 20 rupees",e,"times")
print("you will get 10 rupees",f,"times")
