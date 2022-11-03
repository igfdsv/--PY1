import string
from random import sample
def get_random_password(length: int = 8) -> str:
    return ''.join(sample(string.ascii_letters + string.ascii_lowercase + string.digits, length))


print(get_random_password())
