"""
Main module for the owno backend
"""

import hashlib
import logging
from typing import Any
import uuid
from helpers.sms import send_sms

LOGGER = logging.getLogger(__name__)


def register_user(*, phone_number: str) -> dict[str, Any]:
    """
    Register a user with the given phone number
    """
    user_uuid = str(uuid.uuid4())
    hash_object = hashlib.sha256(user_uuid.encode())
    hash_hex = hash_object.hexdigest()
    hash_int = str(int(hash_hex, 16))[:4]
    message: str = "Verification code: {hash_int} for Owno registration"

    LOGGER.info(f"Generated OTP: {hash_int}")
    send_sms(
        phone_number=phone_number,
        message=message,
    )
    LOGGER.info(f"OTP sent to phone number: {phone_number}")

    return {
        "user_id": user_uuid,
        "otp": hash_int,
        "phone_number": phone_number,
        "message": message,
    }
