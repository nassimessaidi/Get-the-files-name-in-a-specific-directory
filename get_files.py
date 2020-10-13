# Load necessary module
import os


# Function for writing the output the files_list output in a file called directory.txt
def write_in_file():
    # count variable for counting number of files
    count = 0
    with open('directory.txt', 'w') as f:
        for i in files_list:
            count += 1
            f.write(i + "\n")

        # We make separate between files and number of files
        f.write('_' * 30)
        f.write(f'\nNumber of files are: {count}')


while True:
    try:
        directory = input('Enter the directory(Leave it blank and click Enter if you want the current directory): ')

        # Remove unnecessary spaces
        directory = directory.strip()

        if directory == "":
            # If the directory input is empty we take the current directory with os.getcwd()
            directory = os.getcwd()

            # Loop through the directory to find just the files and store them in files_list
            files_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

            # called the function above to write the output in a file
            # because files_list is global variable we don't need to pass it as an argument
            write_in_file()

            # print a message that confirm that the program works, and display the path of output file
            print('All files has been extracted successfully under:', os.path.join(os.getcwd(), 'directory.txt'))

        # if the user pass a custom path, we check if it a valid path before entering the loop
        elif os.path.exists(directory):
            # The same instructions as above
            files_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
            write_in_file()
            print('All files has been extracted successfully under:', os.path.join(os.getcwd(), 'directory.txt'))

        # if the path does not exists, we give the user a hint
        else:
            print("Directory does not exists")
            # continue: instruction for skip the break and give the user a chance for a new correct directory
            continue

        break

    # If any unsuspected error was found, this will raise and show the user the Error
    except Exception as e:
        print('[*] Error:', e)
