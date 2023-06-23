import subprocess
from os import path, makedirs, mkdir, remove, walk
from constants import *
from webscrappingEDisciplinas import StudentsFromWebscrapping
from requests import get
from getAuthCookies import AuthCookies
from extractCoverageFromJaCoCoHTML import rateStudent
from json import load

students = None

def downloadAllTheTestArchives():
    downloads_directory = 'Downloads'
    flag_before_download_all_archives = '0'
    while flag_before_download_all_archives != '' and flag_before_download_all_archives.upper() != "N":
        flag_before_download_all_archives = input('\nVocê deseja baixar os arquivos de teste do edisciplinas ou já os tem?\nCaso deseja baixar aperte enter.\nSe já tem baixado, digite "N"\n')    
    
    if(flag_before_download_all_archives.upper() != ''):
        if(path.exists(downloads_directory)):
            return downloads_directory, True
        else:
            print(LINE_MARKER, COULD_NOT_FIND_STUDENTS_FILE)

    #For each student, download the zip file containing the java test code
    students = StudentsFromWebscrapping.getStudents()
    for student in students:
        # Create the directory if the directory downloads doesn't exist
        if not path.exists(downloads_directory): 
            makedirs(downloads_directory)

        filename = '_'.join(student['nome'].split())+'.zip'
        filepath = path.join(downloads_directory, filename)

        print(LINE_MARKER, 'Downloading the zip files')
        response = get(student['arquivo_teste_java_zip'], 
                       cookies = AuthCookies.getAuthDataFromEdisciplinas())

        if response.status_code == 200:
            with open(filepath, 'wb+') as file:
                file.write(response.content)
                print(LINE_MARKER, filename, 'downloaded!')
                file.flush()
        else:
            print(LINE_MARKER, 'Failed to download resource for the student:',student['nome'])

    return downloads_directory, False
    

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
    if not path.exists(path.join(download_folder, student_folder)):
        return False, ZIP_FILE_NOT_FOUND
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
            return False, COULD_NOT_RUN_TESTS_MESSAGE
    except subprocess.CalledProcessError:
        return False, TEST_CLASS_NOT_FOUND_MESSAGE
    return True, student['nome'] + "'s tests sucessfull executed!"

def main():

    downloads_directory, alreadyHasTheFilesDownloaded = downloadAllTheTestArchives()
    extractAllZipFiles(downloads_directory)


    if(alreadyHasTheFilesDownloaded):
        if(path.exists('students.json')):
            print(LINE_MARKER, 'I found the students directory, recovering the data...')
            with open('students.json', 'r+') as students_file:
                students = load(students_file)

    if(not students):
        print(LINE_MARKER, COULD_NOT_FIND_STUDENTS_FILE)
        students = StudentsFromWebscrapping.getStudents()
    else:
        print(LINE_MARKER, 'Students recovered!')

    for student in students:
        print(LINE_MARKER, 'Running tests of:', student["nome"])
        testsSuccessful, errorMessage = treatStudentsFilesAndRunTests(student, downloads_directory)
        if(testsSuccessful):
            if not rateStudent(student):
                print(LINE_MARKER, 'Could not correct the exercise of:', student["nome"] + LINE_MARKER)
        else:
            print(LINE_MARKER, errorMessage)
        
        # deleta a pasta target
        if(path.exists(TARGET_PATH)):
            subprocess.run(DELETE_TARGET_FOLDER, shell=True)

if __name__ == "__main__":
    main()