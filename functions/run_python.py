import os
import sys
import subprocess

def run_python_file(working_directory, file_path):
    # Create the absolute working directory path
    abs_working_directory = os.path.abspath(working_directory)

    # Create the absolute full path file by joining the working directory path and the file_path parameter
    abs_full_path_file = os.path.abspath(os.path.join(working_directory, file_path))

    # Check if the abs_full_path_file is outside the working directory, if yes it raise an error
    if abs_full_path_file.startswith(abs_working_directory) == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # Check If abs_full_path_file exist 
    if os.path.exists(abs_full_path_file) == False:
        return f'Error: File "{file_path}" not found.'
    
    # Check if the abs_full_path_file  with the ".py" extension, if not it raise an error
    if abs_full_path_file.endswith(".py") == False:
        return f'Error: "{file_path}" is not a Python file.'

    try:
        # Set a timeout of 30 seconds to prevent infinite execution
        result = subprocess.run(["python", abs_full_path_file], text=True, timeout=30, capture_output=True, cwd=abs_working_directory)

        # Format the output : STDOUT and STDERR
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        # If the process exits with a non-zero code
        if result.returncode != 0:
            return f"Process exited with code X, {result.returncode}"

        # If no output is produced
        if result.returncode == 0:
            return "No output produced.\n"
        
    except Exception as error:
        return f"Error: executing Python file: {error}"
