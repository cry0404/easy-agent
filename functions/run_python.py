import os
import subprocess
def run_python_file(working_directory, file_path):
  try:
    abs_working_directory = os.path.abspath(working_directory)
    if os.path.isabs(file_path):
      abs_file_path = file_path
    else:
      abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    
    if not abs_file_path.startswith(abs_working_directory):
      return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
      return f'Error: File "{file_path}" not found'
    if not abs_file_path.endswith(".py"):
      return f'Error: "{file_path}" is not a Python file.'

    result = subprocess.run(
      ["python3", file_path],
      timeout = 30,
      capture_output = True,
      cwd = working_directory,
      text = True
    )
    if result.stdout or result.stderr:
      print("STDOUT:", result.stdout)
      print("STDERR:", result.stderr)
    if result.returncode is not 0:
      print("Procees exited with code X", result.result.returncode)
    return f'Successfully executed "{file_path}"'
  except subprocess.TimeoutExpired as e:
    return f'Error: Process timed out after 30 seconds'
  except subprocess.CalledProcessError as e:
    return f'Error: Process exited with code {e.returncode}'
  except Exception as e:
    return f'Error: Unexpected error - {str(e)}'                  