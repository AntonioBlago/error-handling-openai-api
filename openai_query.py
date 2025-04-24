from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from openai import (
    APIError,
    APIConnectionError,
    AuthenticationError,
    RateLimitError,
    BadRequestError,
    NotFoundError,
    Timeout
)
import logging
import traceback

# Configure logging to log any errors silently
logging.basicConfig(filename="openai_errors.log", level=logging.WARNING)

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="your-api-key")  # Replace with your actual API key

def query_openai(prompt_text: str) -> str | None:
    """Send a prompt to OpenAI Chat API and return the response, or None if any error occurs."""
    
    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt_text}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            timeout=15  # Optional: timeout in seconds
        )
        return response.choices[0].message.content

    # Specific error handling
    except AuthenticationError:
        logging.warning("Authentication error – invalid or disabled API key.")
    except RateLimitError:
        logging.warning("Rate limit reached – too many requests.")
    except APIConnectionError:
        logging.warning("API connection error.")
    except Timeout:
        logging.warning("Request timed out.")
    except BadRequestError:
        logging.warning("Bad request – check model name or parameters.")
    except NotFoundError:
        logging.warning("Model not found or endpoint does not exist.")
    except APIError:
        logging.warning("Internal OpenAI API error.")
    except Exception:
        logging.warning("Unexpected error:\n" + traceback.format_exc())

    return None

# Example usage
response = query_openai("How does sunlight work?")
if response:
    print(response)
else:
    print("No response received.")
