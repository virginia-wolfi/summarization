from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException, Request
from langchain_community.llms import HuggingFaceHub

# Load environment variables from .env file
load_dotenv()

app = FastAPI()



# Endpoint for text summarization
@app.post("/summarize")
async def summarize(request: Request):
    """
    Summarizes a piece of text using a Hugging Face model hosted on the Hub.

    Parameters:
    - request (Request): The incoming HTTP request object containing JSON data.

    Returns:
    - dict: A dictionary containing the summary of the text.

    Raises:
    - HTTPException(500): If there is an error during summarization, raises an HTTP 500 error
      with details of the exception.
    """
    try:
        data = await request.json()
        text = data.get("text", '')
        summarizer = HuggingFaceHub(repo_id="facebook/bart-large-cnn",
                                    task='summarization')
        summary = summarizer.invoke(text)

        return {"summary": summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
