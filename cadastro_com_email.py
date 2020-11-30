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


#Buscar elemento de teste
selecionar_campo_email = navegador.find_element_by_tag_name('input#email_create')
selecionar_campo_email.click()
selecionar_campo_email.send_keys('leticiatest@gmail.com')
sleep(3)

clicar_em_botao_criar = navegador.find_element_by_tag_name('button#SubmitCreate')
clicar_em_botao_criar.click()
#após esse comando, a tela para inscrição de dados é aberta para finalização de cadastro.

sleep(3)
#Fechar navegador ao finalizar teste
navegador.quit()
