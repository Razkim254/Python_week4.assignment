def read_and_modify_file():
    input_filename = input("Python assignment: ")

    try:
        # Try opening the input file using the correct variable name
        with open(input_filename, 'r') as file:
            content = file.read()
            print("File read successfully!")
        
        # Modify the content (e.g., make all text uppercase)
        modified_content = content.upper()

        # Prepare output filename
        output_filename = "modified_" + input_filename
        
        # Write modified content to new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
            print(f"Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
