import os

def write_file(working_directory, file_path, content):
    try:
      if not os.path.exists(file_path):
        file_path = os.makedirs(file_path)
      if os.path.isabs(file_path):
        #不是绝对路径就需要join
        abs_file_path = os.path.abspath(file_path)
      else:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

      abs_working_dir = os.path.abspath(working_directory)
      if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
      if not os.path.isdir(abs_working_dir):
        return f'Error: Working directory not found or is not a directory: "{working_directory}"'
      if not os.path.isdir(os.path.dirname(abs_file_path)):
        return f'Error: Parent directory not found or is not a directory: "{os.path.dirname(abs_file_path)}"'
      if not os.access(abs_working_dir, os.W_OK):
        return f'Error: Permission denied - cannot write to working directory: "{working_directory}"'
      
      parent_dir = os.path.dirname(abs_file_path)
      if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
      if not os.access(parent_dir, os.W_OK):
        return f'Error: Permission denied - cannot write to parent directory: "{parent_dir}"'
      with open(abs_file_path, 'w', encoding='utf-8') as file:
        file.write(content)
      return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except PermissionError as e:
      return f'Error: Permission denied - {str(e)}'
    except FileNotFoundError as e:
      return f'Error: File not found - {str(e)}'
    except OSError as e:
      return f'Error: OS error - {str(e)}'
    except Exception as e:
      return f'Error: Unexpected error - {str(e)}'