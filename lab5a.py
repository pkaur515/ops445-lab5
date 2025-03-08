#!/usr/bin/env python3
# Author ID:  pkaur515

def read_file_string(file_name):
    """Takes file_name as string for a file name, returns its entire contents as a string"""
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: The file {file_name} does not exist."
    except PermissionError:
        return f"Error: Permission denied for file {file_name}."

def read_file_list(file_name):
    """Takes a file_name as string for a file name, 
    returns its entire contents as a list of lines without new-line characters"""
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return f"Error: The file {file_name} does not exist."
    except PermissionError:
        return f"Error: Permission denied for file {file_name}."

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

