import os

def get_files_content(working_directory, file_path):
    """读取指定文件的内容"""
    try:
        # 处理绝对路径的情况
        if os.path.isabs(file_path):
            abs_file_path = os.path.abspath(file_path)
        else:
            # 相对路径：相对于工作目录
            abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
        abs_working_dir = os.path.abspath(working_directory)
        
        # 检查文件是否在允许的工作目录内
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # 检查文件是否存在且为常规文件
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        # 读取文件内容
        with open(abs_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if len(content) > 10000:
                return content[:10000] + f'\n[...File "{file_path}" truncated at 10000 characters]'
            else:
                return content

    except PermissionError as e:
        return f'Error: Permission denied - {str(e)}'
    except FileNotFoundError as e:
        return f'Error: File not found - {str(e)}'
    except OSError as e:
        return f'Error: OS error - {str(e)}'
    except Exception as e:
        return f'Error: Unexpected error - {str(e)}'