import os  # Importing the os module for interacting with the operating system

class_no = 0  # Initializing a variable 'class_no' with the value 0
class_yes = 1  # Initializing a variable 'class_yes' with the value 1 (This variable is not used in the code provided)

label_folder = './dataset/labels/train'  # Defining the path to the folder containing the label files

# Looping through each file in the specified folder
for file_name in os.listdir(label_folder):
    if file_name.endswith('.txt'):  # Checking if the file has a '.txt' extension
        file_path = os.path.join(label_folder, file_name)  # Creating the absolute path of the file

        # Opening the file in read mode and reading all lines into a list
        with open(file_path, 'r') as f:
            lines = f.readlines()

        modified_lines = []  # Creating an empty list to store modified lines
        # Iterating through each line in the file
        for line in lines:
            line = line.strip().split()  # Removing leading/trailing whitespace and splitting the line into a list
            # Checking if the first element in the line is '1' or '2'
            if line[0] == '1' or line[0] == '2':
                line[0] = str(class_no)  # If '1' or '2', setting the first element to the string representation of 'class_no'
            else:
                line[0] = str(class_no)  # If not '1' or '2', setting the first element to the string representation of 'class_no'
            modified_line = ' '.join(line)  # Joining the modified line elements into a string
            modified_lines.append(modified_line)  # Appending the modified line to the list

        # Writing the modified lines back to the same file, overwriting its content
        with open(file_path, 'w') as f:
            f.write('\n'.join(modified_lines))  # Writing the modified lines separated by newline characters to the file
