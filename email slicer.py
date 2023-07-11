# collect email from user
# split or slice the email using the @ , the first part as the user name , the second part is gonna be saved as domain
# split domain using .,
def main():
    print("welcome to the email slicer ")

    email_input = input("Enter your email address:")
    (user_name, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("user_name:", user_name)
    print("Domain:", domain)
    print("Extension:", extension)


while True:
    main()
