from behave import given, when, then
from selenium.webdriver import Firefox

#cenário1: cadastro de usuário sem e-mail informado
@given('acesso a pagina de login_cadastro de usuário')
def go_to_page(context):
    context.navegador = Firefox()
    context.navegador.get('http://automationpractice.com/index.php?controller=authentication&;back=my-account')

@when('seleciono botão de novo cadastro')
def select_button(context):
    context.navegador
    context.navegador.find_element_by_id('SubmitCreate')

@when('não informo e-mail')
def step_impl(context):
    context.navegador.find_element_by_id('SubmitCreate').click()

@then('recebo uma mensagem de erro contento a informação')
def check_error_message(context):
    context.navegador.find_element_by_id('create_account_error')

#cenário2: cadastro de usuário com e-mail informado
@given('acesso a pagina de login_cadastro de usuario')
def go_to_page(context):
    context.navegador = Firefox()
    context.navegador.get('http://automationpractice.com/index.php?controller=authentication&;back=my-account')

@when('informo um e-mail válido')
def step_impl(context):
    context.navegador.find_element_by_id('email_create').click()
    context.navegador.find_element_by_id('email_create').send_keys(['leticiatxt@test.com'])

@when('seleciono o botão de envio de login_cadastro')
def step_impl(context):
        context.navegador.find_element_by_id('SubmitCreate').click()

@then('site é direcionado para uma nova página de continuação de cadastro')
def check_error_message(context):
    ...

#cenário3:login com usuário sem cadastro
@when('realizo o insert de e-mail e senha invalido')
def step_impl(context):
    context.navegador.find_element_by_id('email').click()
    context.navegador.find_element_by_id('email').send_keys(['test@teste.com'])
    context.navegador.find_element_by_id('passwd').send_keys(['123456'])

@when('não possuo cadastro')
def step_impl(context):
    ...

@when('envio os dados selecionando botão de envio')
def step_impl(context):
    context.navegador.find_element_by_id('SubmitLogin').click()

@then('mensagem de erro é exibida')
def step_impl(context):
    context.navegador.find_element_by_class_name('alert.alert-danger')

#cenário4: login com senha incorreta
@when('realizo o insert de e-mail e senha')
def step_impl(context):
    context.navegador.find_element_by_id('email').click()
    context.navegador.find_element_by_id('email').send_keys(['sedarob208@questza.com'])
    context.navegador.find_element_by_id('passwd').send_keys(['teste'])

@when('senha está incorreta')
def step_impl(context):
    ...

@then('mensagem de erro é exibida no topo')
def step_impl(context):
    context.navegador.find_element_by_class_name('alert.alert-danger')

#cenário5: login com sucesso
@when('realizo o insert de e-mail e senha cadastrado')
def step_impl(context):
    context.navegador.find_element_by_id('email').click()
    context.navegador.find_element_by_id('email').send_keys(['sedarob208@questza.com'])
    context.navegador.find_element_by_id('passwd').send_keys(['123456'])

@when('realizo o envio de dados corretos')
def step_impl(context):
    context.navegador.find_element_by_id('SubmitLogin').click()

@then('site é redirecionado para home page de usuário')
def step_impl(context):
    ...
