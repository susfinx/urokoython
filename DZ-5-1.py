import os

def split_file_path(file_path):
    path, file_name = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(file_name)
    return path, file_name, file_extension

file_path = "/path/to/some/file.txt"
path, file_name, file_extension = split_file_path(file_path)
print("Путь:", path)
print("Имя файла:", file_name)
print("Расширение файла:", file_extension)
