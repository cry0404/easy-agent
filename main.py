import os
from dotenv import load_dotenv
import sys
import argparse
from google.genai import types
from system_prompt import system_prompt
from declare_function import schema_get_files_info
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
available_functions = types.Tool(
  function_declarations = [
    schema_get_files_info,
  ]
)
client = genai.Client(api_key=API_KEY)

#不要仅仅打印 generate_content 响应的 .text 属性，
# 还要检查 .function_calls 属性。如果 LLM 调用了函数，请打印函数名称和参数：



response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents= messages,
    config=types.GenerateContentConfig(
      tools=[available_functions],
      system_instruction=system_prompt
    )
)
if response.function_calls: #如果LLM调用了函数，则打印函数名称和参数
  print(f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})")
else:
  prompt_token_count = response.usage_metadata.prompt_token_count
  candidates_token_count = response.usage_metadata.candidates_token_count
  if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {candidates_token_count}")
  print(response.text)