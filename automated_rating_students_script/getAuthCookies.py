from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from functools import reduce

userInput = input('\n\nCaso deseja inserir os dados da autenticação por aqui, insira no seguinte formato: NUSP;SENHA\n\nCaso já tenha inserido os dados nesse formato no arquivo loginUsp.txt, apenas pressione enter para iniciar a autenticação.\n\n')
print('Carregando...')
chrome_options = Options()
# Configurar as opções do ChromeDriver para o modo headless
chrome_options.add_argument('--headless')  # Executar em modo headless
chrome_options.add_argument('--disable-gpu')  # Desabilitar aceleração de hardware

# Capturar dados do login
try:
    userInput = next(open('loginUsp.txt', 'r'))
except FileNotFoundError:
    userInput = None
    while ';' not in userInput:
        userInput = input('\n=-=-=-=-=-=-=-=-=-=\n\nNão foi possível recuperar os dados do arquivo loginUsp.txt ou o formato é incorreto. Insira-os manualmente no formato\nNUSP;SENHA\n\n')

userInput = userInput.split(';')

# Configurar o driver do Chrome com as opções
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Acessar a URL e realizar a autenticação
driver.get('https://edisciplinas.usp.br/auth/shibboleth')


## caso o usuário queira autenticar na pagina do google
username = driver.find_element(By.ID, 'username').send_keys(userInput[0])
password = driver.find_element(By.ID, 'password').send_keys(userInput[1])

loginButton = driver.find_element(By.XPATH, "//div[@id='login-main-content']//button").click()

# Recuperar os cookies - convertendo [{cookie1:lorem}, {cookie1:lorem}, ...] para {cookie:lorem, cookie2, lorem}
cookies = reduce(lambda x, y: {**x, **y}, map(lambda x: {x['name']: x['value']}, driver.get_cookies()))

driver.quit()
