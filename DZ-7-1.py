import os

def bulk_rename_files(directory, desired_name, num_digits, source_ext, target_ext, name_range=None):
    for root, _, files in os.walk(directory):
        for idx, filename in enumerate(sorted(files)):
            if filename.endswith(source_ext):
                original_name_part = filename[name_range[0] - 1 : name_range[1]]
                new_name = f"{desired_name}_{original_name_part}_{str(idx).zfill(num_digits)}.{target_ext}"
                original_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_name)
                os.rename(original_path, new_path)
                print(f"Переименовано: {filename} -> {new_name}")

source_directory = urok-2/urok7-1
desired_name = 'new_name'
num_digits = 4  # Количество цифр в порядковом номере
source_ext = '.txt'  # Расширение исходных файлов
target_ext = 'txt'  # Расширение конечных файлов
name_range = [3, 6]  # Диапазон символов для взятия из исходного имени

bulk_rename_files(source_directory, desired_name, num_digits, source_ext, target_ext, name_range)
