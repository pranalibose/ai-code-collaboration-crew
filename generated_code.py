import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_email(email: str) -> Optional[str]:
    """
    Validate an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    Optional[str]: If the email is invalid, returns an error message. Otherwise, returns None.
    """

    try:
        # Use a more robust regular expression pattern to match a valid email address
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

        # Check if the email matches the pattern
        if re.match(pattern, email):
            logger.info(f"Email '{email}' is valid")
            return None
        else:
            logger.info(f"Email '{email}' is invalid")
            return "Invalid email address"

    except re.error as e:
        # Catch and log regular expression-related errors
        logger.error(f"Error occurred while compiling regular expression: {str(e)}")
        return "Error occurred while compiling regular expression"
    except Exception as e:
        # Catch and log other exceptions
        logger.error(f"Error occurred while validating email: {str(e)}")
        return "Error occurred while validating email"


# Example usage
email = "john.doe@example.com"
print(validate_email(email))  # Should print: None

invalid_email = "invalid_email"
print(validate_email(invalid_email))  # Should print: Invalid email address