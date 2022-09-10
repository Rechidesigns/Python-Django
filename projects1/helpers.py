from datetime import datetime
import random
import string


def generate_order_id():
    """This function generates random ids with the date and certain strings."""
    rand_str = [random.choice(string.ascii_letters) for _ in range(4)]
    code = "".join(rand_str)
    today = datetime.now()
    return today.strftime(f"%d%m%y-{code}")





