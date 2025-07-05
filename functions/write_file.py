import os

def write_file(working_directory, file_path, content):
    # Create the full path file by joining the absolute working directory path and the file_path parameter
    full_path_file = os.path.join(working_directory, file_path)

    # Check if the full_path_file is outside the working directory, if yes it raise an error
    if os.path.abspath(full_path_file).startswith(os.path.abspath(working_directory)) == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # Check If full_path_file file doesn't exist and is a directory
    if os.path.exists(os.path.abspath(full_path_file)) and os.path.isdir(os.path.abspath(full_path_file)):
        return f'Error: "{file_path}" is a directory, not a file'
    
    # In case full_path_file doesn't exist, we create it and then we write in it the content parameter
    try:
        with open(full_path_file, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as error:
        return f'Error file writing "{file_path}": {error}'
    
    

