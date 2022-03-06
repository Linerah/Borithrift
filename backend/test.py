import re

def check_valid_email(email):
    # RFC 5322 email standard
    regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if (re.fullmatch(regex, email)):
        return True
    return False

print(check_valid_email("josue@tech.in"))