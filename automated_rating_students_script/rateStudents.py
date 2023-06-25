from bs4 import BeautifulSoup
from json import dump
from os import path, makedirs
from constants import JACOCO_RESULTS_PATH
import datetime
from shutil import rmtree
from webscrappingEDisciplinas import StudentsFromWebscrapping

class RateStudent():

    executionFolderName = ''

    def __init__(self):
        timestamp_now = datetime.datetime.now()
        formatted_timestamp = timestamp_now.strftime("%d-%b-%Y_%H:%M")
        self.executionFolderName = "FinalResults/"+ \
            StudentsFromWebscrapping.disciplina_avaliada_code + '_' + formatted_timestamp + ".csv"
        

    def calculateStudentPoints(self, resultados):
        instructionsCoverage = resultados.get('coberturaInstrucoes')
        branchesCoverage = resultados.get('coberturaRamificacoes')
        ciclomaticCoverage = str(100*(
            (
                float(resultados.get('complexidadeCiclomaticaTotal')) 
                - 
                float(resultados.get('complexidadeCiclomaticaNaoCoberta'))
            )
            /
            float(resultados.get('complexidadeCiclomaticaTotal'))) 
            ) + '%'
        linesCoverage = str(100*(
            (
                float(resultados.get('totalDeLinhas')) 
                - 
                float(resultados.get('linhasNaoExecutadas'))
            )
            /
            float(resultados.get('totalDeLinhas'))) 
            ) + '%'
        methodsCoverage = str(100*(
            (
                float(resultados.get('totalDeMetodosExecutaveis')) 
                - 
                float(resultados.get('metodosNaoExecutados'))
            )
            /
            float(resultados.get('totalDeMetodosExecutaveis'))) 
            ) + '%'
        
        finalPointsStr = (instructionsCoverage + branchesCoverage + ciclomaticCoverage + linesCoverage + methodsCoverage)[:-1]
        
        finalPointsList = [float(i) for i in finalPointsStr.split('%')]
        
        finalPoints = sum(finalPointsList) / len(finalPointsList) / 10

        return finalPoints


    def getResultsTableFromHTML(self):

        if not path.exists(JACOCO_RESULTS_PATH): return None
        # Carregar o arquivo HTML
        with open(JACOCO_RESULTS_PATH, 'r') as file:
            content = file.read()

        # Criar o objeto BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        # Fechar o arquivo html
        file.close()

        # Encontrar todos os elementos <td>
        return soup.find_all('tr')

    def rateStudent(self, student):

        resultado = {
            "particaoAnalisadaDoCodigoDeTeste": "",
            "instrucoesNaoExecutadas": "",
            "coberturaInstrucoes": "",
            "ramificacoesNaoExecutadas": "",
            "coberturaRamificacoes": "",
            "complexidadeCiclomaticaNaoCoberta": "",
            "complexidadeCiclomaticaTotal": "",
            "linhasNaoExecutadas": "",
            "totalDeLinhas": "",
            "metodosNaoExecutados": "",
            "totalDeMetodosExecutaveis": "",
            "classesNaoExecutadas": "",
            "totalDeClassesExecutaveis": "",
            "notaFinal": ""
        }

        table_rows = self.getResultsTableFromHTML()

        if(table_rows):    
            # Iterar sobre os elementos encontrados
            for table_row in table_rows:
                if('Total' in table_row.get_text()):
                    # O PYTHON É LINDO !!!!! / PYTHON IS AMAZING!!!!!
                    resultado = {
                        key: value
                        for key, value in zip(resultado.keys(), [data.get_text() for data in table_row])
                    }

        # Adicionando a nota ao dicionário de informações
        resultado["nota"] = f"{self.calculateStudentPoints(resultado):.2f}"\
                            if table_rows \
                            else 'Não foi possível avaliar de forma automática'
        resultado["nome"] = student["nome"]
        resultado["nusp"] = student["nusp"]


        # Verificar se o diretório existe e criar, se necessário
        if not path.exists("IndividualResults"):
            makedirs("IndividualResults")

        with open("IndividualResults/" + '_'.join(student['nome'].split()) +".json", "w+") as outfile:
            dump(resultado, outfile)

        if not path.exists("FinalResults"):
            makedirs("FinalResults")

        with open(self.executionFolderName, "a+") as final_results_file:
            final_results_file.write(student["nome"] + ';' + str(resultado['nota']) + '\n')


        return table_rows != None

