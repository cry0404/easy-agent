import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from system_prompt import system_prompt
from declare_function import *
from call_function import call_function

# 加载环境变量
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# 初始化Gemini客户端
client = genai.Client(api_key=API_KEY)

def ai_agent_with_iteration(user_prompt, max_iterations=20, verbose=False):
    """
    带有20次迭代限制的AI代理实现
    """
    # 检查API密钥
    if not API_KEY:
        raise ValueError("未找到GEMINI_API_KEY环境变量，请确保.env文件中包含API密钥")
    
    # 初始化消息列表
    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=user_prompt)]
        )
    ]
    
    # 配置可用工具
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_files_content, 
            schema_write_file,
            schema_run_python_file,
        ]
    )
    
    # 开始迭代循环
    for iteration in range(max_iterations):
        if verbose:
            print(f"=== 迭代 {iteration + 1}/{max_iterations} ===")
        
        try:
            # 1. 调用AI模型生成回复
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,  # 传递完整的消息历史
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt
                )
            )
            
            # 2. 处理响应的候选项
            if response.candidates:
                for candidate in response.candidates:
                    # 将候选项内容添加到消息历史
                    messages.append(candidate.content)
            
            # 3. 检查是否有函数调用
            if response.function_calls:
                if verbose:
                    print(f"AI想要调用函数: {response.function_calls[0].name}")
                
                # 4. 执行函数调用
                tool_response = call_function(
                    response.function_calls[0], 
                    verbose=verbose
                )
                
                # 5. 将函数调用结果添加到消息历史
                messages.append(tool_response)
                
                # 6. 打印函数调用结果（用于调试）
                if verbose:
                    function_result = tool_response.parts[0].function_response.response
                    if 'error' in function_result:
                        print(f"函数调用错误: {function_result['error']}")
                    else:
                        print(f"函数调用成功: {function_result['result']}")
                
                # 7. 继续下一轮迭代
                continue
                
            else:
                # 8. 没有函数调用，任务完成
                if verbose:
                    print("=== 任务完成 ===")
                    print("AI的最终回复:")
                    print(response.text)
                return response.text
                
        except Exception as e:
            error_msg = f"迭代 {iteration + 1} 发生错误: {str(e)}"
            if verbose:
                print(error_msg)
            return f"执行失败: {error_msg}"
    
    # 9. 达到最大迭代次数
    warning_msg = f"达到最大迭代次数 {max_iterations}，AI可能陷入了循环或任务过于复杂"
    if verbose:
        print(f"=== {warning_msg} ===")
    return f"任务未完成: {warning_msg}"

# 使用示例
if __name__ == "__main__":
    user_input = "帮我查看calculator项目的结构，然后运行main.py文件"
    result = ai_agent_with_iteration(user_input, verbose=True)
    print("最终结果:", result)