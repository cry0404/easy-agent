import os
#这里需要考虑如何获取工作目录,这里的工作目录其实是指定的目录，比如 calculator 目录，那么工作目录就是 calculator 目录
#如果 directory 不为空，那么就列出 directory 目录下的文件和目录
#如果 directory 为空，那么就列出工作目录下的文件和目录


#返回值始终是一个字符串？
def get_files_info(working_directory, directory=None):
    try:
        # 确定要列出的目录
        if directory is None:
            target_dir = working_directory
        else:
            # directory 应该是相对于 working_directory 的路径
            target_dir = os.path.join(working_directory, directory)
        
        # 检查目标目录是否存在且是目录
        if not os.path.exists(target_dir):
            return f'Error: "{target_dir}" does not exist'
            
        if not os.path.isdir(target_dir):
            return f'Error: "{target_dir}" is not a directory'
        
        # 如果指定了directory，检查是否在工作目录范围内
        if directory is not None:
            # 获取绝对路径进行比较
            abs_working_dir = os.path.abspath(working_directory)
            abs_target_dir = os.path.abspath(target_dir)
            
            # 检查目标目录是否在工作目录内
            if not abs_target_dir.startswith(abs_working_dir):
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # 列出目录内容
        files = os.listdir(target_dir)
        file_info_list = []
        
        for file in files:
            file_path = os.path.join(target_dir, file)
            file_info = {
                'name': file,
                'size': os.path.getsize(file_path),
                'is_directory': os.path.isdir(file_path)
            }
            file_info_list.append(file_info)
        
        # 构建返回字符串
        result_lines = []
        for file in file_info_list:
            result_lines.append(f"- {file['name']}: file_size={file['size']} bytes, is_dir={file['is_directory']}")
        
        return '\n'.join(result_lines)
        
    except PermissionError as e:
        return f'Error: Permission denied - {str(e)}'
    except FileNotFoundError as e:
        return f'Error: File not found - {str(e)}'
    except OSError as e:
        return f'Error: OS error - {str(e)}'
    except Exception as e:
        return f'Error: Unexpected error - {str(e)}'