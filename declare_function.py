from google.genai import types





schema_get_files_info = types.FunctionDeclaration(
    name = "get_files_info",
    description = "Get the information of the files in the working directory",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory path",
            ),
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
        required=["working_directory"]  # directory 是可选的
    )
)

schema_get_files_content = types.FunctionDeclaration(
    name = "get_files_content",
    description = "Get the content of the file in the working directory",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory path",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to get the content of, relative to the working directory",
            ),
        },
        required=["working_directory", "file_path"]
    )
)

schema_write_file = types.FunctionDeclaration(
    name = "write_file",
    description = "Write the content to the file in the working directory",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory path",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
        required=["working_directory", "file_path", "content"]
    )
)

# 注意：实际函数名是 run_python_file，不是 run_python_code
schema_run_python_file = types.FunctionDeclaration(
    name = "run_python_file",
    description = "Run a Python file in the working directory",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory path",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to run, relative to the working directory",
            ),
        },
        required=["working_directory", "file_path"]
    )
)

