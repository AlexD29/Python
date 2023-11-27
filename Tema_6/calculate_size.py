#3
import os
import sys


def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        return size
    except Exception as e:
        print(f"Error getting file size: {e}")
        return None


def calculate_size(directory_path):
    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        sum = 0
        for file in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file)

            if os.path.isfile(file_path):
                sum = sum + get_file_size(file_path)

        print(f"Total size of directory: {sum} KB")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Format: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        calculate_size(directory_path)
