""" Functionality test for OpenAI API in Python. """

from dotenv import load_dotenv
load_dotenv(override=True)

import os,sys
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")
#print(f"OpenAI API Key: {openai_api_key}")

client = OpenAI()

def get_gpt_response(prompt):
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(get_gpt_response("Tell me how to use the OpenAI API in Python" + " give me in markdown format with code snippets."))