import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_directory = os.path.abspath(os.path.join(working_directory, directory))

    if not abs_target_directory.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_target_directory):
        return f'Error: "{directory}" is not a directory'
    

    try:

        files_info = []
        for filename in os.listdir(abs_target_directory):
            filepath = os.path.join(abs_target_directory, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}\n"
            )
        return "\n".join(files_info)
    
    except Exception as e:
        return f"Error listing files: {e}"

    

    