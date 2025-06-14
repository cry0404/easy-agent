import os
from dotenv import load_dotenv
import sys
import argparse
from google.genai import types
from system_prompt import system_prompt
from declare_function import *
from call_function import call_function  # 导入我们的函数调用处理器

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

from google import genai

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", action="store_true", help="Show verbose output")
parser.add_argument("user_prompt", type=str, help="The prompt to send to the model")
args = parser.parse_args()

verbose = args.verbose
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
    schema_get_files_content,
    schema_write_file,
    schema_run_python_file,
  ]
)
client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents= messages,
    config=types.GenerateContentConfig(
      tools=[available_functions],
      system_instruction=system_prompt
    )
)

if response.function_calls:  # 如果LLM调用了函数
    # 调用我们的函数处理器
    tool_response = call_function(response.function_calls[0], verbose=verbose)
    
    # 检查返回的 types.Content 是否包含 function_response
    if not hasattr(tool_response.parts[0], 'function_response') or not tool_response.parts[0].function_response:
        raise RuntimeError("Fatal error: call_function did not return a proper function_response")
    
    # 获取实际的响应内容
    function_result = tool_response.parts[0].function_response.response
    
    # 如果 verbose 模式开启，打印函数调用结果
    if verbose:
        function_name = response.function_calls[0].name
        print(f"Function '{function_name}' result:")
        
        # 检查是否是错误响应
        if 'error' in function_result:
            print(f"  Error: {function_result['error']}")
        elif 'result' in function_result:
            print(f"  Success: {function_result['result']}")
        else:
            print(f"  Raw response: {function_result}")
    
    # 将工具响应添加到消息历史中，以便后续对话
    messages.append(tool_response)
    
    # 可以选择继续与AI对话，让它处理函数调用结果
    # next_response = client.models.generate_content(...)
    
else:
    # 没有函数调用，直接显示AI的文本回复
    prompt_token_count = response.usage_metadata.prompt_token_count
    candidates_token_count = response.usage_metadata.candidates_token_count
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_token_count}")
        print(f"Response tokens: {candidates_token_count}")
    print(response.text)