import tarfile as tar
import sys
import os
import shutil


if __name__ == "__main__":
    layer_tmp_folder = "layer.tar.docker_image_tmp"
    layer_filename = 'layer.tar'
    build_folder = sys.argv[1]
    tar_name = sys.argv[2]
    tar_name = os.path.abspath(tar_name)
    os.chdir(build_folder)
    with tar.open(tar_name, 'w:bz2') as the_file:
        for root, dirs, files in os.walk('.', topdown=True):
            if layer_tmp_folder in dirs:
                layer_zip_path = os.path.join(root, layer_filename)
                layer_inner_tmp_folder = os.path.join(root, layer_tmp_folder)
                with tar.open(layer_zip_path, 'w:bz2') as the_layer_file:
                    the_layer_file.add(layer_inner_tmp_folder, arcname='/')
                the_file.add(layer_zip_path, arcname=layer_zip_path[1:])
                dirs[:] = [d for d in dirs if d != layer_tmp_folder]
                os.remove(layer_zip_path)
            for item in files:
                file_path = os.path.join(root, item)
                the_file.add(file_path, arcname=file_path[1:])