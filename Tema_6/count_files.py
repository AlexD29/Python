#4
import os
import sys


def is_directory_empty(directory_path):
    try:
        return not any(os.listdir(directory_path))
    except Exception as e:
        print(f"Error checking if directory is empty: {e}")
        return None


def get_file_extension(file_path):
    root, extension = os.path.splitext(file_path)
    return extension


def list_all_files(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if os.path.isfile(file_path):
            print(filename)


def count_files(directory_path):
    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        if is_directory_empty(directory_path):
            raise FileNotFoundError(f"Directory {directory_path} is empty.")

        list_all_files(directory_path)

        extensions_dict = {}
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            if os.path.isfile(file_path):
                extension = get_file_extension(filename)
                if extension  in extensions_dict:
                    extensions_dict[extension] += 1
                else:
                    extensions_dict[extension] = 1

        print(extensions_dict)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Format: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        count_files(directory_path)
