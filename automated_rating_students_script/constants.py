from os import path 

## DIRECTORY PATHS
DOWNLOADS_DIRECTORY_PATH = '/home/draude/Downloads'

JAVA_PROGRAM_DIRECTORY_PATH = '../Cal'

CAL_TEST_RELATIVE_PATH = './Cal/src/test/java/CalTest.java'

CAL_TEST_ABS_PATH = path.abspath(CAL_TEST_RELATIVE_PATH)



## SHELL COMMANDS
GET_CURRENT_TEST_CLASS_FROM_DOWNLOADS = f'find . -name "*[tT]est*.java" -exec grep -v \'^package\' {{}} \\; -exec cp {{}} {CAL_TEST_ABS_PATH} \\; -quit'

IMPROVE_TEST_CLASS_FORMAT = f'sed -i \'/^package .*;/d\' {CAL_TEST_RELATIVE_PATH}'

INSTALL_TEST_ARTIFACTS_AND_EXECUTE = ['mvn', 'clean', 'install']

DELETE_TARGET_FOLDER = 'rm -r ../Cal/target'



## MESSAGES
TEST_CLASS_NOT_FOUND_MESSAGE = f" I couldn't found no java class with 'Test' in the name in the folder {DOWNLOADS_DIRECTORY_PATH} :("

COULD_NOT_RUN_TESTS_MESSAGE = f" I couldn't run the java tests from {CAL_TEST_RELATIVE_PATH} :("
