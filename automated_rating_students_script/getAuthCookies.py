from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from functools import reduce
from constants import LINE_MARKER, AUTH_EDISCIPLINAS_URL


class AuthCookies:

    cookies = None

    def getLoginData():
        # Capturar dados do login
        try:
            userInput = next(open('loginUsp.txt', 'r'))
        except FileNotFoundError:
            while ';' not in userInput:
                userInput = input(LINE_MARKER + 'Não foi possível recuperar os dados do arquivo loginUsp.txt ou o formato é incorreto. Insira-os manualmente no formato\nNUSP;SENHA\n\n')

        return userInput.split(';')

    @classmethod
    def getAuthDataFromEdisciplinas(cls):

        if(cls.cookies): return cls.cookies

        print(LINE_MARKER, 'Authenticating in', AUTH_EDISCIPLINAS_URL)
        userInput = input(LINE_MARKER + 'Caso deseja inserir os dados da autenticação por aqui, insira no seguinte formato: NUSP;SENHA\
        \nCaso já tenha inserido os dados nesse formato no arquivo loginUsp.txt, apenas pressione enter para iniciar a autenticação.\n\n')
        print(LINE_MARKER, 'Loading...')


        chrome_options = Options()
        # Configurar as opções do ChromeDriver para o modo headless
        chrome_options.add_argument('--headless')  # Executar em modo headless
        chrome_options.add_argument('--disable-gpu')  # Desabilitar aceleração de hardware

        
        userInput = cls.getLoginData()

        # Configurar o driver do Chrome com as opções
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

        # Acessar a URL e realizar a autenticação
        driver.get(AUTH_EDISCIPLINAS_URL)


        ## caso o usuário queira autenticar na pagina do google
        username = driver.find_element(By.ID, 'username').send_keys(userInput[0])
        password = driver.find_element(By.ID, 'password').send_keys(userInput[1])

        loginButton = driver.find_element(By.XPATH, "//div[@id='login-main-content']//button").click()

        # Recuperar os cookies - convertendo [{cookie1:lorem}, {cookie1:lorem}, ...] para {cookie:lorem, cookie2, lorem}
        cls.cookies = reduce(lambda x, y: {**x, **y}, map(lambda x: {x['name']: x['value']}, driver.get_cookies()))

        if(cls.cookies):
            print(LINE_MARKER, 'Cookies sucessfully returned')
        driver.quit()

        return cls.cookies
