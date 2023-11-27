#1
import os
import sys

def read_and_print_files(directory_path, file_extension):
    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            if os.path.isfile(file_path) and filename.endswith(file_extension):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        print(f"Contents of {filename}:")
                        print(file.read())
                        print("\n" + "-"*30)

                except Exception as e:
                    print(f"Error reading {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Format: python script.py <directory_path> <file_extension>")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]

        read_and_print_files(directory_path, file_extension)
