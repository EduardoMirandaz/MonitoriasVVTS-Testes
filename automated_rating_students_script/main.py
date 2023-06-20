import subprocess
from constants import *


# Try to find any file in the downloads folder (and its subfolders)
# that contains a .java file with "test" or "Test" in the name.
try:
    subprocess.run(GET_CURRENT_TEST_CLASS_FROM_DOWNLOADS, shell=True, cwd=DOWNLOADS_DIRECTORY_PATH)
except subprocess.CalledProcessError:
    print(TEST_CLASS_NOT_FOUND_MESSAGE)
    exit()

# remove o package setado por alguns alunos
subprocess.run(IMPROVE_TEST_CLASS_FORMAT, shell=True)

# executa os comandos que rodam os testes
try:
    subprocess.run(INSTALL_TEST_ARTIFACTS_AND_EXECUTE, cwd=JAVA_PROGRAM_DIRECTORY_PATH)
except subprocess.CalledProcessError:
    print(COULD_NOT_RUN_TESTS_MESSAGE)
    exit()


# aqui nesse ponto preciso recuperar os dados referentes aos alunos!


# # deleta a pasta target
# subprocess.run(DELETE_TARGET_FOLDER, shell=True)
