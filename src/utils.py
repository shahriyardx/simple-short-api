import string
import random

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
