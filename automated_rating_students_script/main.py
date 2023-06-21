import subprocess
from os import path, makedirs, mkdir, remove, walk
from constants import *
from webscrappingEDisciplinas import students
from requests import get
from getAuthCookies import cookies
from extractCoverageFromJaCoCoHTML import rateStudent


def downloadAllTheTestArchives():
    downloads_directory = 'Downloads'
    flag_before_download_all_archives = input('Você deseja baixar os arquivos java.zip ou já os tem?\nCaso deseja baixar aperte enter.\nSe já tem baixado, digite "N"\n')
    if(flag_before_download_all_archives.upper() == 'N') : return downloads_directory
    #For each student, download the zip file containing the java test code
    for student in students:
        # Create the directory if the directory downloads doesn't exist
        if not path.exists(downloads_directory): 
            makedirs(downloads_directory)

        filename = '_'.join(student['nome'].split())+'.zip'
        filepath = path.join(downloads_directory, filename)

        response = get(student['arquivo_teste_java_zip'], cookies=cookies)

        if response.status_code == 200:
            with open(filepath, 'wb+') as file:
                file.write(response.content)
                print(filename, 'downloaded!')
                file.flush()
        else:
            print('Failed to download resource for the student:',student['nome'])

    return downloads_directory
    

def extractAllZipFiles(download_folder):
    # Walk into every downloaded zip and unzip
    for _, _, files in walk(download_folder):
        for file in files:
            if('.zip' in file):
                directory = path.join(download_folder, file)
                new_directory = directory[:-4]

                if not path.isdir(new_directory):
                    mkdir(new_directory)

                subprocess.run(['unzip', '-q', file, '-d', file[:-4]], cwd=download_folder, input=b'A\n')

                # delete the .zip archive
                remove(directory)
        break
    

def treatStudentsFilesAndRunTests(student, download_folder):
    student_folder = '_'.join(student['nome'].split())
    print(path.exists(path.join(download_folder, student_folder)))
    ## Try to find a test class .java and move it to CalTest path
    try:
        # Copy the Test.java file from the student to our project CalTest.java
        subprocess.run(GET_STUTEND_TEST_CLASS_AND_SEND_TO_TEST_JAVA_PACKAGE, shell=True, cwd=path.join(download_folder, student_folder))
        # delete the package of the .java test file if it exists
        subprocess.run(IMPROVE_TEST_CLASS_FORMAT, shell=True)

        # executa os comandos que rodam os testes
        try:
            subprocess.run(INSTALL_TEST_ARTIFACTS_AND_EXECUTE, cwd=JAVA_PROGRAM_DIRECTORY_ROOT_PATH)
        except subprocess.CalledProcessError:
            print(COULD_NOT_RUN_TESTS_MESSAGE)
            return None
    except subprocess.CalledProcessError:
        print(TEST_CLASS_NOT_FOUND_MESSAGE)
        return None        
    return True

def main():

    downloads_directory = downloadAllTheTestArchives()
    extractAllZipFiles(downloads_directory)

    for student in students:
        print('Running tests of:', student["nome"])
        if(treatStudentsFilesAndRunTests(student, downloads_directory)):
            if not rateStudent(student):
                print(COULD_NOT_RUN_TESTS_MESSAGE)
        else:
            print('Não foi possível corrigir o exercício do aluno:', student["nome"] + '\n\n\n=-=-=-=-=-=-=-=-=-=-=--=-=-=\n\n\n')
        # deleta a pasta target
        subprocess.run(DELETE_TARGET_FOLDER, shell=True)

if __name__ == "__main__":
    main()