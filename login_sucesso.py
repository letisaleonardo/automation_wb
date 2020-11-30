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

#fazer login
seleciona_email = navegador.find_element_by_tag_name('input#email')
seleciona_email.click()
seleciona_email.send_keys('sedarob208@questza.com')
sleep(3)

seleciona_senha = navegador.find_element_by_tag_name('input#passwd')
seleciona_senha.click()
seleciona_senha.send_keys('123456')
sleep(3)

#envio de preenchimento de form
clicar_em_botao_criar = navegador.find_element_by_tag_name('button#SubmitLogin')
clicar_em_botao_criar.click()


sleep(3)
#Fechar navegador ao finalizar teste
#navegador.quit()
