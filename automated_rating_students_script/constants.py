from os import path 

## DIRECTORY PATHS
DOWNLOADS_DIRECTORY_PATH = '/Downloads'

JAVA_PROGRAM_DIRECTORY_ROOT_PATH = '../Cal'

CAL_TEST_RELATIVE_PATH = '../Cal/src/test/java/CalTest.java'

CAL_TEST_ABS_PATH = path.abspath(CAL_TEST_RELATIVE_PATH)

JACOCO_RESULTS_PATH = '../Cal/target/site/jacoco/index.html'

TARGET_PATH = '../Cal/target'

## SHELL COMMANDS
GET_STUTEND_TEST_CLASS_AND_SEND_TO_TEST_JAVA_PACKAGE = f'find . -name "*[tT]est*.java" -exec grep -v \'^package\' {{}} \\; -exec cp {{}} {CAL_TEST_ABS_PATH} \\; -quit'

IMPROVE_TEST_CLASS_FORMAT = f'sed -i \'/^package .*;/d\' {CAL_TEST_RELATIVE_PATH}'

INSTALL_TEST_ARTIFACTS_AND_EXECUTE = ['mvn', 'clean', 'install']

DELETE_TARGET_FOLDER = 'rm -r ' + TARGET_PATH

## URLS

AUTH_EDISCIPLINAS_URL = 'https://edisciplinas.usp.br/auth/shibboleth'


## MESSAGES
TEST_CLASS_NOT_FOUND_MESSAGE = f" I couldn't found no java class with 'Test' in the name in the folder {DOWNLOADS_DIRECTORY_PATH} :("

COULD_NOT_RUN_TESTS_MESSAGE = f" I couldn't run the java tests from {CAL_TEST_RELATIVE_PATH} :("

COULT_NOT_RATE_THE_EXERCISE_MESSAGE = f"I couldn't rate the exercise"

LINE_MARKER = '\n=-=-=-=-=-=-=-=-=-=-=--=-=-=\n'

ZIP_FILE_NOT_FOUND = '.zip file not found'

COULD_NOT_FIND_STUDENTS_FILE = "I couldn't find the students directory, lets download it again!"