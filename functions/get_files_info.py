import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_directory = os.path.abspath(os.path.join(working_directory, directory))

    if not abs_target_directory.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_target_directory):
        return f'Error: "{directory}" is not a directory'
    
    contents = os.listdir(abs_target_directory)

    content_details = ""

    for name in contents:
        size = os.path.getsize(os.path.join(abs_target_directory, name))
        is_dir = os.path.isdir(os.path.join(abs_target_directory, name))
        content_details += (f"- {name}: file_size:{size} bytes, is_dir:{is_dir}\n")
    return content_details

    