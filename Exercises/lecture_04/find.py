import os
import sys

INITIAL_FOLDER = "D:\Projects"


def find_file(startFolder: str, filename: str) -> str:
    for dirpath, dirnames, filenames in os.walk(startFolder):
        if filename in filenames:
            result = os.path.join(dirpath, filename)
            return result
    return None


if len(sys.argv) >= 2:
    file_to_search = sys.argv[1]
    output = find_file(INITIAL_FOLDER, file_to_search)
    if output:
        print(output)
    else:
        print("file not found")

else:
    print("not enough parameters")


