import os
from dotenv import load_dotenv
import sys
import argparse
from google.genai import types

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

from google import genai

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", action="store_true", help="Show verbose output")
parser.add_argument("user_prompt", type=str, help="The prompt to send to the model")
args = parser.parse_args()

verbose = args.verbose #这里的 verbose 就会是true
user_prompt = args.user_prompt
messages = [
  types.Content(
    role = "user",
    parts = [
      types.Part(
        text = user_prompt
      )
    ]
  )
]

client = genai.Client(api_key=API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents= messages
)
prompt_token_count = response.usage_metadata.prompt_token_count
candidates_token_count = response.usage_metadata.candidates_token_count
if verbose:
  print(f"User prompt: {user_prompt}")
  print(f"Prompt tokens: {prompt_token_count}")
  print(f"Response tokens: {candidates_token_count}")
print(response.text)