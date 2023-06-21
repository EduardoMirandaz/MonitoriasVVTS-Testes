from requests import get 
from getAuthCookies import cookies
from bs4 import BeautifulSoup

response = get('https://edisciplinas.usp.br/mod/assign/view.php?id=4757395&action=grading', 
               cookies=cookies).text

students = []

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
        students.append(student_data)
