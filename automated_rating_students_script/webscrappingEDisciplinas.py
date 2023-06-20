from requests import get 
from cookies import cookies
from bs4 import BeautifulSoup


response = get('https://edisciplinas.usp.br/mod/assign/view.php?id=4757395&action=grading', 
               cookies=cookies)

# Criar o objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

table_rows = soup.find_all('tr')

for row in table_rows:
    for data in row:
        if('@usp.br' in data.get_text()):
            print('Email:', data.get_text())
        if('.zip' in data.get_text()):
            print('Link:', data.get_text())


