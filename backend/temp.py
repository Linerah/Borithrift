import hashlib
import re
#text = input("Enter text: ")
text = "asd"
hash_obj = hashlib.sha512()
hash_obj.update(text.encode("utf-8"))
print(hash_obj.hexdigest())

email = "josuegoogle.com"
regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
if re.fullmatch(regex, email):
    print("ye")
else:
    print("nah")