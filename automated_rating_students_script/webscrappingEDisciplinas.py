from requests import get 
from getAuthCookies import AuthCookies
from bs4 import BeautifulSoup
from json import dump

class StudentsFromWebscrapping:
    

    students = None

    @classmethod
    def getStudents(cls):
        
        if(cls.students): return cls.students
        
        # Aqui deve ser indicado o url a página que contém as tarefas de todos os alunos
        response = get('https://edisciplinas.usp.br/mod/assign/view.php?id=4757395&action=grading', 
                    cookies= AuthCookies.getAuthDataFromEdisciplinas()).text

        # Criar o objeto BeautifulSoup
        soup = BeautifulSoup(response, 'html.parser')

        table_rows = soup.find_all('tr')

        name_ref_index = 2
        for row in table_rows:
            if('@usp.br' in row.get_text()):
                student_data = {}
                for index, data in enumerate(row):
                    if(index == name_ref_index):
                        student_data['nome'] = data.get_text()
                    if(index == name_ref_index+1):
                        student_data['email'] = data.get_text()
                    if(index == name_ref_index+2):
                        student_data['nusp'] = data.get_text()
                    if('.zip' in data.get_text()):
                        student_data['data_envio_arquivo'] = ' '.join((data.get_text().split())[1:])
                        a_tag = data.find('a')
                        student_data['arquivo_teste_java_zip'] = a_tag['href'] if a_tag else 'File not found'
                cls.students.append(student_data)
        
        with open('students.json', 'w+') as out_students_file:
            dump(cls.students, out_students_file)
        return cls.students
