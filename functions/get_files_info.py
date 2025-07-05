import os

def get_files_info(working_directory, directory=None):

    # Create the full path by joining the working directory and the directory parameter
    full_path_directory = os.path.join(working_directory, directory)

    # Check if the full path directory is outside the working directory, if yes it raise an error
    if os.path.abspath(full_path_directory).startswith(os.path.abspath(working_directory)) == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # Check if the full path is a directory, if not it raise an error
    if os.path.isdir(full_path_directory) == False:
        return f'Error: "{directory}" is not a directory'

    
    # Get the contents of the directory
    file_and_dir_in_work_dir = os.listdir(full_path_directory)

    # Build the output string
    content_directory = []

    for element in file_and_dir_in_work_dir:
        element_path = os.path.join(full_path_directory, element)
        is_dir = os.path.isdir(element_path)
        file_size = os.path.getsize(element_path) if not is_dir else 0
        content_directory.append(f"- {element}: file_size={file_size} bytes, is_dir={is_dir}")

    return '\n'.join(content_directory)