import string
from random import choice


def generate_short_url():
    return "".join(choice(string.ascii_letters + string.digits) for _ in range(6))
