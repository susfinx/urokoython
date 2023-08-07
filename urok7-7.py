import os
import shutil


def sort_files_by_type(source_folder):
    video_extensions = ['.mp4', '.avi', '.mkv']
    image_extensions = ['.jpg', '.png', '.gif']
    text_extensions = ['.txt', '.doc', '.pdf']

    for root, _, files in os.walk(source_folder):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_extension = os.path.splitext(filename)[1].lower()

            if file_extension in video_extensions:
                target_folder = os.path.join(source_folder, 'video')
            elif file_extension in image_extensions:
                target_folder = os.path.join(source_folder, 'images')
            elif file_extension in text_extensions:
                target_folder = os.path.join(source_folder, 'text')
            else:
                continue

            os.makedirs(target_folder, exist_ok=True)
            target_path = os.path.join(target_folder, filename)
            shutil.move(file_path, target_path)

    print("Сортировка завершена!")


source_folder = 'путь_к_вашей_папке'
sort_files_by_type(source_folder)
