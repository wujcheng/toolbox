import string
import random

def random_string(length):
    return "".join(random.choices(string.ascii_letters+string.digits, k=length))

if __name__ == "__main__":
    print(random_string(16))
