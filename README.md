# OWNO Backend

A serverless backend application built with AWS SAM (Serverless Application Model) that provides user registration functionality through API Gateway and Lambda.

## Architecture

- **API Gateway**: Handles HTTP requests
- **Lambda Function**: Processes registration requests
- **Python 3.10**: Runtime environment
- **SAM/CloudFormation**: Infrastructure as Code

## Prerequisites

- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- [Python 3.10](https://www.python.org/downloads/)
- [Docker](https://hub.docker.com/search/?type=edition&offering=community)
- AWS Account and configured credentials

## Project Structure

```
owno-backend/
├── owno/
│   ├── __init__.py
│   ├── app.py         # Lambda handler
│   └── main.py        # Business logic
├── events/            # Test events
├── tests/             # Unit tests
└── template.yaml      # SAM template
```

## API Endpoints

### Register User
- **URL**: `/register`
- **Method**: `POST`
- **Body**:
```json
{
    "phone_number": "+1234567890"
}
```
- **Success Response**:
```json
{
    "message": "User registered successfully",
    "phone_number": "+1234567890"
}
```

## Local Development

1. **Build the application**:
```bash
sam build --use-container
```

2. **Test locally**:
```bash
# Test with example event
sam local invoke OwnoFunction --event events/event.json

# Start local API
sam local start-api
curl -X POST http://localhost:3000/register -H "Content-Type: application/json" -d '{"phone_number": "+1234567890"}'
```

## Deployment

1. **Initial deployment**:
```bash
sam deploy --guided
```

2. **Subsequent deployments**:
```bash
sam deploy
```

The deployment will prompt for:
- Stack Name (e.g., "owno-backend")
- AWS Region
- Confirmation of changes
- IAM role creation permission
- Save arguments to samconfig.toml

## Testing

```bash
# Install test dependencies
pip install -r tests/requirements.txt

# Run unit tests
python -m pytest tests/unit -v

# Run integration tests (requires deployed stack)
AWS_SAM_STACK_NAME="owno-backend" python -m pytest tests/integration -v
```

## Monitoring and Logs

View Lambda function logs:
```bash
sam logs -n OwnoFunction --stack-name "owno-backend" --tail
```

## Cleanup

Remove the deployed stack:
```bash
sam delete --stack-name "owno-backend"
```

## Development with AWS Toolkit

For an enhanced development experience, you can use the AWS Toolkit available for:
- [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
- [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
- And other popular IDEs

## Resources

- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [API Gateway Documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)