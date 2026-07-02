import random
import string


def generate_reservation_id() -> str:
    """
    Generate a unique reservation ID.
    Example: BB-A8F3K2
    """
    random_part = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=6)
    )

    return f"BB-{random_part}"