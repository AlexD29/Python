#2
import os
import sys

def get_file_extension(file_path):
    root, extension = os.path.splitext(file_path)
    return extension

def rename_files(directory_path, file_extension):
    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        k = 1
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            if os.path.isfile(file_path) and filename.endswith(file_extension):
                try:
                    new_filename = "file" + str(k) + get_file_extension(filename)
                    os.rename(filename, new_filename )
                    print(f"File renamed from {filename} to {new_filename}")
                    k = k + 1

                except Exception as e:
                    print(f"Error renaming file: {e}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Format: python script.py <directory_path> <file_extension>")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]

        rename_files(directory_path, file_extension)
