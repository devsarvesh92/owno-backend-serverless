"""
Main module for the owno backend
"""

import hashlib
from typing import Any
import uuid


def register_user(*, phone_number: str) -> dict[str, Any]:
    """
    Register a user with the given phone number
    """
    user_uuid = str(uuid.uuid4())
    hash_object = hashlib.sha256(user_uuid.encode())
    hash_hex = hash_object.hexdigest()
    hash_int = str(int(hash_hex, 16))[:4]
    return {
        "user_id": user_uuid,
        "otp": hash_int,
        "phone_number": phone_number,
        "message": "OTP sent to phone number",
    }
