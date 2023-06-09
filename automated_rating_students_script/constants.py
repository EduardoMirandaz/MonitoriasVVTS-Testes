from os import path 

## DIRECTORY PATHS
DOWNLOADS_DIRECTORY_PATH = '/Downloads'

JAVA_PROGRAM_DIRECTORY_ROOT_PATH = '../Cal'

CAL_TEST_RELATIVE_PATH = '../Cal/src/test/java/CalTest.java'

CAL_TEST_ABS_PATH = path.abspath(CAL_TEST_RELATIVE_PATH)

JACOCO_RESULTS_PATH = '../Cal/target/site/jacoco/index.html'

TARGET_PATH = '../Cal/target'

## SHELL COMMANDS
GET_STUDEND_TEST_CLASS_AND_SEND_TO_TEST_JAVA_PACKAGE = f'find . -name "*[tT]est*.java" -exec grep -v \'^package\' {{}} \\; -exec cp {{}} {CAL_TEST_ABS_PATH} \\; -quit'

IMPROVE_TEST_CLASS_FORMAT = f"sed -i -e '/^package .*;/d' -e 's/class .*{{/class CalTest{{\\n/g' {CAL_TEST_RELATIVE_PATH}"

INSTALL_TEST_ARTIFACTS_AND_EXECUTE = ['mvn', 'clean', 'install']

DELETE_TARGET_FOLDER = 'rm -r ' + TARGET_PATH

## URLS

AUTH_EDISCIPLINAS_URL = 'https://edisciplinas.usp.br/auth/shibboleth'


CODIGO_DISCIPLINA_SCC0569 = 'SCC0569'
CODIGO_DISCIPLINA_SSC0524 = 'SSC0524'

DISCIPLINA_SSC0569_TESTE_E_INSPECAO_DE_SOFTWARE = 'https://edisciplinas.usp.br/mod/assign/view.php?id=4757121&action=grading'
DISCIPLINA_SSC0524_VERIFICACAO_VALIDACAO_E_TESTE_DE_SOFTWARE = 'https://edisciplinas.usp.br/mod/assign/view.php?id=4757395&action=grading'



## MESSAGES
TEST_CLASS_NOT_FOUND_MESSAGE = f" I couldn't found no java class with 'Test' in the name in the folder {DOWNLOADS_DIRECTORY_PATH} :("

COULD_NOT_RUN_TESTS_MESSAGE = f" I couldn't run the java tests from {CAL_TEST_RELATIVE_PATH} :("

COULT_NOT_RATE_THE_EXERCISE_MESSAGE = f"I couldn't rate the exercise"

LINE_MARKER = '\n=-=-=-=-=-=-=-=-=-=-=--=-=-=\n'

ZIP_FILE_NOT_FOUND = '.zip file not found'

COULD_NOT_FIND_STUDENTS_FILE = "I couldn't find the students directory, lets download it again!"