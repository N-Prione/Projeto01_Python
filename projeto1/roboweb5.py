# instalação das bibliotecas
from selenium import webdriver # módulo principal
from selenium.webdriver.common.keys import Keys # módulo para simular o pressionar de teclas (ENTER, TAB, SHIFT, etc)
from selenium.webdriver.common.by import By # identificar o método de localização do elemento (ID, XPath, Classe, etc.)
import time
import xlrd # biblioteca para ler a planilha

# variavel para criar o arquivo de texto
arquivo = open('Resultado.txt', 'w') # ela ira abrir um arquivo .txt, o W (write), ele que ira escrever no arquivo

# usar a planilha
workbook = xlrd.open_workbook('/home/nprione/Documentos/PYTHON/OficinaPython/ProjetoRobo/excel.xls') # variavel que ira abrir a planilha com os dominios
planilha = workbook.sheet_by_name('Plan1') # especificar a planilha que ira trabalhar
linhas = planilha.nrows # contagem de número de linhas
colunas = planilha.ncols # contagem de número de colunas

# abertuda do navegador e do site (driver é apenas o nome de uma variável)
driver = webdriver.Chrome() # ira abrir o navegador do Google Chrome
driver.get('https://registro.br/') # o .get irá pesquisar o site escolhido

# pesquisando no site
for linha_planilha in range(0, linhas): # fazer uma contagem de linhas dentro da planilha
    x = planilha.cell_value(linha_planilha, 0) # ira começar a ler cada linha do excel e dar seu valor
    pesquisa = driver.find_element(By.ID, 'is-avail-field') # By.ID indica onde será localizado + o id da barra de pesquisa no site
    # para achar o ID, basta clicar na barra com o botão direito e ir em inspecionar
    time.sleep(1) # so para dar tempo do robo processar
    pesquisa.clear() # ira limpar a barra caso tenha algo escrito
    pesquisa.send_keys(x) # ira pesquisar essa chave
    time.sleep(1)# so para dar tempo do robo processar
    pesquisa.send_keys(Keys.RETURN) # referente ao clique do enter
    time.sleep(1) # so para dar tempo do robo processar
    resultado = driver.find_element(By.XPATH, '//*[@id="conteudo"]/div/section/div[2]/div/p/span/strong') # pegar o caminho do negrito que aparece DISPONIVEL e NÃO DISPONIVEL
    texto = f'Domínio ({x}) = {resultado.text.upper()}! \n' # o texto escolhido e as variáveis
    arquivo.write(texto)

arquivo.close()
# fechar o navegador
driver.quit() # depois do tempo ele fecha sozinho