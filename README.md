Natürlich! Hier ist die aktualisierte README.md inklusive Hinweis für Support-Anfragen per E-Mail:


---

README.md (inkl. Support-Kontakt)

# OpenAI Chat API Query Script (with Full Error Handling)

This Python script allows you to query the OpenAI Chat API using the latest SDK (`openai >= 1.0.0`) and silently handles all possible errors.

## Features

- Uses the modular OpenAI Python client (`OpenAI(api_key=...)`)
- Supports `gpt-4` and other models
- Catches and logs:
  - Authentication errors
  - Rate limits
  - API/internal errors
  - Connection issues and timeouts
  - Invalid requests and missing endpoints
- Logs all errors to `openai_errors.log`
- Returns `None` silently if any issue occurs

## Usage

1. Install the OpenAI SDK:
   ```bash
   pip install --upgrade openai

2. Replace the placeholder your-api-key with your actual OpenAI API key.


3. Run the script:

python openai_query.py



Example

The script sends a single prompt:

response = query_openai("How does sunlight work?")

If a valid response is returned, it is printed. Otherwise, the script outputs:

No response received.


---

Support

For questions, feature requests, or help with integration, feel free to reach out via email:

info@antonioblago.com

or via Website (antonioblago.de)[antonioblago.de]


---

License

MIT License – feel free to use, adapt, or extend it.
