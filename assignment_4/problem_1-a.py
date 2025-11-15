EMAIL_AT_CHAR = "@"


def verify_email_helper(email, index=0):
    if len(email) == index:
        return (False, index)
    if email[index] == EMAIL_AT_CHAR:
        return (True, index)
    index += 1
    return verify_email_helper(email, index)


def verify_email(email):
    verification_tuple = verify_email_helper(email)
    if verification_tuple[0] == True:
        print(f"Valid email! Found @ at index {verification_tuple[1]}.")
    if verification_tuple[0] == False:
        print("Invalid email! Did not find @.")


input_email = input("enter your email: ")
verify_email(input_email)
