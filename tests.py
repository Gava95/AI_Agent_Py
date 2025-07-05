from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def tests():

    test_files_info = False
    test_files_content = False
    test_write_file = False
    test_run_python = True


    if test_files_info == True:

        # Return a list of the contents of the calculator directory.
        print(get_files_info("calculator", "."))

        # Return a list the contents of the calculator/pkg directory.
        print(get_files_info("calculator", "pkg"))

        # this should return an error string because the /bin directory 
        # is not inside the calculator directory
        print(get_files_info("calculator", "/bin"))

        # this should return an error string because the agent it not allowed 
        # to work outside of the working directory calculator
        print(get_files_info("calculator", "../"))


    if test_files_content == True:

        # Return a list of the content of the main.py file in calculator directory.
        print(get_file_content("calculator", "main.py"))

        # Return a list of the content of the calculator.py file in calculator/pkg directory.
        print(get_file_content("calculator", "pkg/calculator.py"))

        # this should return an error string because the /bin/cat is a directory not a file
        # and is not inside the calculator directory
        print(get_file_content("calculator", "/bin/cat"))


    if test_write_file == True:

        # Overwrite the lorem.txt file in calculator directory.
        print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

        # Create and write the morelorem.txt file in calculator/pkg directory.
        print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

        # Create and write the temp.txt file and also create the calculator/tmp directory.
        print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    

    if test_run_python == True:

        # Run main.py file in calculator directory.
        print(run_python_file("calculator", "main.py"))

        # Run tests.py file in calculator directory.
        print(run_python_file("calculator", "tests.py"))

        # Run ../main.py file in calculator/.. directory. This should return an error
        print(run_python_file("calculator", "../main.py"))

        # Run nonexistent.py file in calculator directory. This should return an error
        print(run_python_file("calculator", "nonexistent.py"))
        





if __name__ == "__main__":
    tests()
