#language: pt

Funcionalidade: Acessar funcionalidades do site para automação de testes

    """
    Validação de criação de usuário e login.
    """

    Cenario: cadastro de usuário sem e-mail informado
    Dado acesso a pagina de login_cadastro de usuário
    Quando seleciono botão de novo cadastro
    E não informo e-mail
    Entao recebo uma mensagem de erro contento a informação

    Cenario: cadastro de usuário com e-mail informado
    Dado acesso a pagina de login_cadastro de usuario
    Quando seleciono botão de novo cadastro
    E informo um e-mail válido
    E seleciono o botão de envio de login_cadastro
    Entao site é direcionado para uma nova página de continuação de cadastro

    Cenario: login com usuário sem cadastro
    Dado acesso a pagina de login_cadastro de usuario
    Quando realizo o insert de e-mail e senha invalido
    E não possuo cadastro
    E envio os dados selecionando botão de envio
    Entao mensagem de erro é exibida

    Cenario: login com senha incorreta
    Dado acesso a pagina de login_cadastro de usuario
    Quando realizo o insert de e-mail e senha
    E senha está incorreta
    E envio os dados selecionando botão de envio
    Entao mensagem de erro é exibida no topo

    Cenario: login com sucesso
    Dado acesso a pagina de login_cadastro de usuario
    Quando realizo o insert de e-mail e senha cadastrado
    E realizo o envio de dados corretos
    Entao site é redirecionado para home page de usuário
