# FastAPI Text Summarizer

## Setup

1. **Create Access Token on Hugging Face**:
   - Visit https://huggingface.co/ and create an Access Token in your account settings.

2. **Set Access Token Permissions**:
   - Ensure the access token has permissions to:
     - Make calls to the serverless Inference API.
     - Make calls to Inference Endpoints.

3. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`a JSON body containing the text to be summarized.

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
5. **Create .env File**:
   Create a .env file similar to .env.example and insert your HUGGINGFACEHUB_API_TOKEN.
6. **Run the Application**:
   ```bash
   uvicorn main:app --reload
7. **Test the Endpoint:**:
   Send a POST request to http://127.0.0.1:8000/summarize with a JSON payload containing a text field.
   Example using curl:
    ```bash
    curl -X POST "http://127.0.0.1:8000/summarize" -H "Content-Type: application/json" -d '{"text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."}'

