from validate_email_address import validate_email

def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValueError:
        return False

# Example usage:
email_to_validate = "example@example.com"
if is_valid_email(email_to_validate):
    print(f"{email_to_validate} is a valid email address.")
else:
    print(f"{email_to_validate} is not a valid email address.")
