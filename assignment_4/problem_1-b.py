EMAIL_AT_CHAR = "@"

def verify_email_helper(email):
    for i in range(len(email)):
        if email[i] == EMAIL_AT_CHAR:
            return (True, i)
    return (False, i)

def verify_email(email):
    verification_tuple = verify_email_helper(email)
    if verification_tuple[0] == True:
        print(f"Valid email! Found @ at index {verification_tuple[1]}.")
    if verification_tuple[0] == False:
        print(f"Invalid email! Did not find @.")

email_input = input("enter an email: ")
verify_email(email_input)
