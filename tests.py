#!/usr/bin/env python3

import sys
import os

# 添加 functions 目录到 Python 路径，以便导入函数
sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))

from get_files_info import get_files_info
from get_files_content import get_files_content
from write_file import write_file
from run_python import run_python_file 
def test_get_files_info():
    """测试 get_files_info 函数的各种场景"""
    
    print("=" * 60)
    print("测试 get_files_info 函数")
    print("=" * 60)
    
    # 测试 1: 列出 calculator 目录下的当前目录内容
    print("\n1. 测试: get_files_info('calculator', '.')")
    print("-" * 40)
    result1 = get_files_info("calculator", ".")
    print(result1)
    
    # 测试 2: 列出 calculator 目录下的 pkg 子目录内容
    print("\n2. 测试: get_files_info('calculator', 'pkg')")
    print("-" * 40)
    result2 = get_files_info("calculator", "pkg")
    print(result2)
    
    # 测试 3: 尝试访问系统目录 /bin (应返回错误)
    print("\n3. 测试: get_files_info('calculator', '/bin') - 应返回错误")
    print("-" * 40)
    result3 = get_files_info("calculator", "/bin")
    print(result3)
    
    # 测试 4: 尝试访问上级目录 ../ (应返回错误)
    print("\n4. 测试: get_files_info('calculator', '../') - 应返回错误")
    print("-" * 40)
    result4 = get_files_info("calculator", "../")
    print(result4)
    
    print("\n" + "=" * 60)
    print("get_files_info 测试完成")
    print("=" * 60)


def test_get_files_content():
    """测试 get_files_content 函数的各种场景"""
    
    print("=" * 60)
    print("测试 get_files_content 函数")
    print("=" * 60)
    
    # 测试 1: 读取 main.py 文件内容 (包含 def main():)
    print("\n1. 测试: get_files_content('calculator', 'main.py')")
    print("-" * 40)
    result1 = get_files_content("calculator", "main.py")
    print(result1)
    
    # 测试 2: 读取 calculator.py 文件内容 (包含 def _apply_operator)
    print("\n2. 测试: get_files_content('calculator', 'pkg/calculator.py')")
    print("-" * 40)
    result2 = get_files_content("calculator", "pkg/calculator.py")
    print(result2)
    
    # 测试 3: 尝试读取不存在的文件 (应返回错误)
    print("\n3. 测试: get_files_content('calculator', 'nonexistent.py') - 应返回错误")
    print("-" * 40)
    result3 = get_files_content("calculator", "nonexistent.py")
    print(result3)
    
    # 测试 4: 尝试访问系统文件 (应返回错误)
    print("\n4. 测试: get_files_content('calculator', '/etc/passwd') - 应返回错误")
    print("-" * 40)
    result4 = get_files_content("calculator", "/etc/passwd")
    print(result4)
    
    # 测试 5: 尝试访问上级目录的文件 (应返回错误)
    print("\n5. 测试: get_files_content('calculator', '../functions/get_files_content.py') - 应返回错误")
    print("-" * 40)
    result5 = get_files_content("calculator", "../functions/get_files_content.py")
    print(result5)
    
    print("\n" + "=" * 60)
    print("get_files_content 测试完成")
    print("=" * 60)


def test_write_file():
    """测试 write_file 函数的各种场景"""
    
    print("=" * 60)
    print("测试 write_file 函数")
    print("=" * 60)
    
    # 测试 1: 在工作目录根目录下创建文件
    print("\n1. 测试: write_file('calculator', 'lorem.txt', 'wait, this isn\\'t lorem ipsum')")
    print("-" * 40)
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result1)
    
    # 测试 2: 在子目录中创建文件（自动创建目录）
    print("\n2. 测试: write_file('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet')")
    print("-" * 40)
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result2)
    
    # 测试 3: 尝试写入工作目录外的文件 (应返回错误)
    print("\n3. 测试: write_file('calculator', '/tmp/temp.txt', 'this should not be allowed') - 应返回错误")
    print("-" * 40)
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result3)
    
    # 测试 4: 尝试写入上级目录文件 (应返回错误)
    print("\n4. 测试: write_file('calculator', '../test.txt', 'should not work') - 应返回错误")
    print("-" * 40)
    result4 = write_file("calculator", "../test.txt", "should not work")
    print(result4)
    
    # 测试 5: 验证写入的文件内容
    print("\n5. 验证写入的文件内容:")
    print("-" * 40)
    print("读取 lorem.txt 内容:")
    verify_result1 = get_files_content("calculator", "lorem.txt")
    print(verify_result1)
    
    print("\n读取 pkg/morelorem.txt 内容:")
    verify_result2 = get_files_content("calculator", "pkg/morelorem.txt")
    print(verify_result2)
    
    print("\n" + "=" * 60)
    print("write_file 测试完成")
    print("=" * 60)

def test_run_python_file():
    """测试 run_python_file 函数的各种场景"""
    print("=" * 60)
    print("测试 run_python_file 函数")
    print("=" * 60)

    # 1. 正常运行 main.py
    print("\n1. 测试: run_python_file('calculator', 'main.py')")
    print("-" * 40)
    result1 = run_python_file("calculator", "main.py")
    print(result1)

    # 2. 正常运行 tests.py
    print("\n2. 测试: run_python_file('calculator', 'tests.py')")
    print("-" * 40)
    result2 = run_python_file("calculator", "tests.py")
    print(result2)

    # 3. 运行目录外的 main.py，应返回错误
    print("\n3. 测试: run_python_file('calculator', '../main.py') - 应返回错误")
    print("-" * 40)
    result3 = run_python_file("calculator", "../main.py")
    print(result3)

    # 4. 运行不存在的文件，应返回错误
    print("\n4. 测试: run_python_file('calculator', 'nonexistent.py') - 应返回错误")
    print("-" * 40)
    result4 = run_python_file("calculator", "nonexistent.py")
    print(result4)

    print("\n" + "=" * 60)
    print("run_python_file 测试完成")
    print("=" * 60)

if __name__ == "__main__":
    # 运行所有测试
    #test_get_files_info()
    print("\n" + "=" * 80 + "\n")
    #test_get_files_content()
    print("\n" + "=" * 80 + "\n")
    #test_write_file()
    print("\n" + "=" * 80 + "\n")
    test_run_python_file()