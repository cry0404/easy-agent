import argparse
from ai_agent import ai_agent_with_iteration

def main():
    """主函数，处理命令行参数并调用AI代理"""
    parser = argparse.ArgumentParser(description="AI代理助手 - 通过函数调用完成复杂任务")
    parser.add_argument("--verbose", action="store_true", help="显示详细输出信息")
    parser.add_argument("--max-iterations", type=int, default=20, help="最大迭代次数 (默认: 20)")
    parser.add_argument("user_prompt", type=str, help="发送给AI模型的用户指令")
    
    args = parser.parse_args()
    
    try:
        # 调用AI代理处理用户请求
        result = ai_agent_with_iteration(
            user_prompt=args.user_prompt,
            max_iterations=args.max_iterations,
            verbose=args.verbose
        )
        
        if not args.verbose:
            print("AI回复:", result)
            
    except ValueError as e:
        print(f"配置错误: {e}")
        print("请确保设置了GEMINI_API_KEY环境变量")
        exit(1)
    except Exception as e:
        print(f"运行错误: {e}")
        exit(1)

if __name__ == "__main__":
    main()