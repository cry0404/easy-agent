from google.genai import types





schema_get_files_info = types.FunctionDeclaration(
    name = "get_files_info",
    description = "Get the information of the files in the working directory",
    parameters = types.Schema(
        type = types.Type.OBJECT,
         properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    )
)