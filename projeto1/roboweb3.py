# instalação das bibliotecas
from selenium import webdriver # módulo principal
from selenium.webdriver.common.keys import Keys # módulo para simular o pressionar de teclas (ENTER, TAB, SHIFT, etc)
from selenium.webdriver.common.by import By # identificar o método de localização do elemento (ID, XPath, Classe, etc.)
import time

# abertuda do navegador e do site (driver é apenas o nome de uma variável)
driver = webdriver.Chrome() # ira abrir o navegador do Google Chrome
driver.get('https://registro.br/') # o .get irá pesquisar o site escolhido

# pesquisando no site
dominios = ['roboscompython.com.br', 'hotmart', 'pycode', 'uol', 'pythoncurso'] # variavel transformada em Lista com os dominios que serão pesquisados
for dominio in dominios: # um laço de repetição para consultar a lista toda
    pesquisa = driver.find_element(By.ID, 'is-avail-field') # By.ID indica onde será localizado + o id da barra de pesquisa no site
    # para achar o ID, basta clicar na barra com o botão direito e ir em inspecionar
    pesquisa.clear() # ira limpar a barra caso tenha algo escrito
    pesquisa.send_keys(dominio) # ira pesquisar essa chave
    pesquisa.send_keys(Keys.RETURN) # referente ao clique do enter
    time.sleep(2) # tempo para poder renderizar a pagina
    driver.find_element(By.XPATH, '//*[@id="conteudo"]/div/section/div[2]/div/p/span/strong') # pegar o caminho do negrito que aparece DISPONIVEL e NÃO DISPONIVEL
    print(f'Domínio -{dominio}- {driver.find_element(By.XPATH, '//*[@id="conteudo"]/div/section/div[2]/div/p/span/strong').text}') # ira aparecer uma mensagem com o dominio pesquisado e o resultado em formato texto

driver.quit() # depois do tempo ele fecha sozinho