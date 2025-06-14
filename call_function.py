from declare_function import *
from google import genai
from functions import *

def call_function(function_call_part, verbose=False):
  if verbose:
    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
  
  else:
    print(f" - Calling function: {function_call_part.name}")

  function_name = function_call_part.name
  function_args = function_call_part.args

  function_args["working_directory"] = "./calculator"

  function_map = {
    "get_files_info": get_files_info,
    "get_files_content": get_files_content,
    "write_file": write_file,
    "run_python_file": run_python_file,
  }
  
  try:
    if function_name in function_map:
      result = function_map[function_name](**function_args)
      # 返回成功的函数响应
      return types.Content(
        role="tool",
        parts=[
          types.Part.from_function_response(
            name=function_name,
            response={"result": result}
          )
        ],
      )
    else:
      # 函数不存在的情况
      return types.Content(
        role="tool",
        parts=[
          types.Part.from_function_response(
            name=function_name,
            response={"error": f"Function '{function_name}' not found"}
          )
        ],
      )
  
  except Exception as e:
    error_msg = f"Error calling {function_name}: {str(e)}"
    if verbose:
      print(error_msg)
    
    # 返回错误响应
    return types.Content(
      role="tool",
      parts=[
        types.Part.from_function_response(
          name=function_name,
          response={"error": error_msg}
        )
      ],
    )
