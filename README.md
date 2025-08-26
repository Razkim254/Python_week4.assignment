📄 ReadMe: File Read & Modify Script
📝 Description

This Python script allows a user to read the contents of a text file, automatically convert all text to uppercase, and save the modified version to a new file. It includes built-in error handling to manage common issues like missing files or permission errors.

🚀 Features

Prompts the user to enter the name of a file to read.

Converts the file’s contents to uppercase.

Saves the modified content to a new file with the prefix modified_.

Gracefully handles errors such as:

File not found

Permission denied

Other unexpected errors

📂 Example
Input:

File name: assignment.txt
File content:

This is my Python assignment.

Output:

New file: modified_assignment.txt
New content:

THIS IS MY PYTHON ASSIGNMENT.

⚙️ How to Use

Make sure you have Python 3 installed.

Save the script to a .py file, for example: file_modifier.py.

Place the file you want to read (e.g., assignment.txt) in the same directory.

Open a terminal or command prompt and run:

python file_modifier.py


When prompted, enter the filename:

Python assignment: assignment.txt


The script will read the file, convert its contents to uppercase, and write the result to a new file: modified_assignment.txt.

🛠 Requirements

Python 3.x

The input file must exist in the same directory as the script, or you must provide the correct relative/full path.

⚠️ Error Handling

If the file does not exist → you'll see an error message.

If the file cannot be accessed → you'll see a permission error.

If an unknown error occurs → it will be printed with details.

📌 Author

This script was created as part of a Python file handling and error management assignment.

Let me know if you'd like to convert this into a Markdown file (README.md) or include screenshots, usage GIFs, or sample files.
