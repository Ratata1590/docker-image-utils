import tarfile as tar
import sys
import os
import shutil


if __name__ == "__main__":
    tmp_folder_name = 'tmp'
    layer_filename = 'layer.tar'
    os.makedirs(tmp_folder_name, exist_ok=True)
    file_name = sys.argv[1]
    with tar.open(file_name) as the_file:
        the_file.extractall(tmp_folder_name)
    for root, dirs, files in os.walk(tmp_folder_name, topdown=True):
        for item in files:
            file_path = os.path.join(root, item)
            if item == layer_filename:
                tmp_folder_path = f'{file_path}.docker_image_tmp'
                os.makedirs(tmp_folder_path, exist_ok=True)
                with tar.open(file_path) as the_file:
                    the_file.extractall(tmp_folder_path)
                os.remove(file_path)