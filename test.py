import os
import subprocess

download_folder = '/Downloads'  # Caminho relativo
for _, _, files in os.walk(download_folder):
    for file in files:
        directory = os.path.join(download_folder, file)
        new_directory = directory[:-4]

        if not os.path.isdir(new_directory):
            os.mkdir(new_directory)

        subprocess.run(['unzip', '-q', file, '-d', file[:-4]], cwd=download_folder, input=b'A\n')

        # Excluir o arquivo .zip
        os.remove(directory)
    break
