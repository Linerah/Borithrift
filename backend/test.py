# Generate a unique user ID based on time since epoch
import hashlib
import time


def generate_user_ID():
    cur_time = str(time.time())
    hashed_time = hashlib.sha1()
    hashed_time.update(cur_time.encode("utf8"))
    return hashed_time.hexdigest()

print(generate_user_ID())