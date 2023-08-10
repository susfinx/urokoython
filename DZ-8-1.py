__all__ = ['get_directory_info']

import os
import json
import csv
import pickle

def get_directory_info(directory_path):
    result = []

    def process_directory(dir_path):
        dir_info = {
            'name': os.path.basename(dir_path),
            'type': 'directory',
            'size': 0
        }
        total_size = 0

        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                total_size += file_size
                result.append({
                    'name': file,
                    'type': 'file',
                    'parent_directory': dir_path,
                    'size': file_size
                })

        for dir_name in os.listdir(dir_path):
            child_path = os.path.join(dir_path, dir_name)
            if os.path.isdir(child_path):
                child_info = process_directory(child_path)
                total_size += child_info['size']
                result.append(child_info)

        dir_info['size'] = total_size
        return dir_info

    directory_info = process_directory(directory_path)

    with open('directory_info.json', 'w') as json_file:
        json.dump(directory_info, json_file, indent=4)

    with open('directory_info.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['name', 'type', 'parent_directory', 'size'])
        csv_writer.writeheader()
        csv_writer.writerows(result)

    with open('directory_info.pkl', 'wb') as pickle_file:
        pickle.dump(result, pickle_file)

get_directory_info('/python/DZ')
