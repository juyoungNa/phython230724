# ChatGPT_파일분류.py

import os
import shutil

def move_files_by_extension(src_folder, dest_folder, extensions):
    for filename in os.listdir(src_folder):
        if filename.lower().endswith(extensions):
            src_path = os.path.join(src_folder, filename)
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(src_path, dest_path)

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def main():
    downloads_folder = r'C:\Users\student\Downloads'
    images_folder = os.path.join(downloads_folder, 'images')
    data_folder = os.path.join(downloads_folder, 'data')
    docs_folder = os.path.join(downloads_folder, 'docs')

    create_folder_if_not_exists(images_folder)
    create_folder_if_not_exists(data_folder)
    create_folder_if_not_exists(docs_folder)

    move_files_by_extension(downloads_folder, images_folder, ('.jpg', '.jpeg'))
    move_files_by_extension(downloads_folder, data_folder, ('.csv', '.xlsx'))
    move_files_by_extension(downloads_folder, docs_folder, ('.pdf'))

if __name__ == "__main__":
    main()