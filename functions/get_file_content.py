import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    # Create the full path by joining the absolute working directory path and the file_path parameter
    full_path_file = os.path.join(working_directory, file_path)

    # Check if the full path file is outside the working directory, if yes it raise an error
    if os.path.abspath(full_path_file).startswith(os.path.abspath(working_directory)) == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # Check if the full path is a file, if not it raise an error
    if os.path.isfile(os.path.abspath(full_path_file)) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(os.path.abspath(full_path_file), "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(os.path.abspath(full_path_file)) > MAX_CHARS:
                file_content_string.append(f'[...File "{full_path_file}" truncated at {MAX_CHARS} characters]')
        
        return file_content_string

    except Exception as error:
        return f'Error reading file "{file_path}": {error}'


    
