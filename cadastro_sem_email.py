#imports
from selenium.webdriver import Firefox
from time import sleep

#abrir navegador Firefox
navegador = Firefox()

#variável definida com o site, para nao ter a necessidade de ficar colando o link pelo código.
url = 'http://automationpractice.com/index.php?controller=authentication&;back=my-account'
#abrir sítio que será testado
navegador.get(url)
#aguardar 3 segundos para buscar o elemento, visto que a página demorar parar abrir
sleep(3)

clicar_em_botao_criar = navegador.find_element_by_tag_name('button#SubmitCreate')
clicar_em_botao_criar.click()

#pausa para verificação de mensagem de erro
sleep(3)
#leitura da mensagem de erro
mensagem_de_erro = navegador.find_element_by_tag_name('div#create_account_error')
lis = mensagem_de_erro.find_element_by_tag_name('ol')
print(lis.text)

#Fechar navegador ao finalizar teste
navegador.quit()
