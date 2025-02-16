"""
SMS Utility Functions
"""

import boto3
from botocore.exceptions import ClientError


def send_sms(phone_number: str, message: str, topic_arn: str = None) -> dict:
    """
    Send SMS using AWS SNS.

    Args:
        phone_number (str): Phone number with country code (e.g., +1234567890)
        message (str): Message content to send
        topic_arn (str, optional): SNS Topic ARN if using a topic

    Returns:
        dict: Response from AWS SNS
    """
    try:
        # Initialize SNS client
        sns_client = boto3.client(
            "sns", region_name="us-east-1"  # Change to your region
        )

        # Set up the SMS attributes (optional)
        sns_client.set_sms_attributes(
            attributes={"DefaultSMSType": "Transactional"}  # or 'Promotional'
        )

        # Prepare message attributes
        message_attributes = {
            "AWS.SNS.SMS.SMSType": {
                "DataType": "String",
                "StringValue": "Transactional",  # or 'Promotional'
            }
        }

        if topic_arn:
            # Publish to topic
            response = sns_client.publish(
                TopicArn=topic_arn,
                Message=message,
                MessageAttributes=message_attributes,
            )
        else:
            # Send directly to phone number
            response = sns_client.publish(
                PhoneNumber=phone_number,
                Message=message,
                MessageAttributes=message_attributes,
            )

        print(f"Message sent! Message ID: {response['MessageId']}")
        return response

    except ClientError as e:
        print(f"Error sending SMS: {e.response['Error']['Message']}")
        raise
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise
