from functools import partial
import json
import logging
from typing import Any
from main import register_user

LOGGER = logging.getLogger(__name__)


def lambda_handler(event, context):
    """
    Entry point for the lambda function
    """
    LOGGER.info(f"Received event: {json.dumps(event)}")
    result = _get_handler(event)()
    LOGGER.info(f"Returning result: {json.dumps(result)}")
    return {
        "statusCode": 200,
        "body": json.dumps(result),
    }


def _get_handler(event: dict[str, Any]):
    """
    Get the handler for the event
    """
    method = event.get("httpMethod", {})
    path = event.get("path", {})

    match method, path:
        case "POST", "/register":
            return partial(register_user, phone_number=event.get("phone_number"))
