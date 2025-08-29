from LoginsUtils import Login


#login System

def mostrarMenu():
    print("""
    Oque deseja fazer?
        1. Cadastrar usuario
        2. Efetuar login
        3. Finalizar
""")
    
mostrarMenu()

while True:

    #Evitar quebra de codigo
    try:
        menuAsk = int(input(">"))
    except ValueError:
        print("digite um numero valido")
        continue

    #Cadastrar Login
    if menuAsk == 1:
        email = input("Digite seu E-mail: >")
        senha = input("Digite sua senha: >")
        Login.cadastrarLogin(email, senha)

    #Validar Login
    elif menuAsk == 2:
        email = input("Digite um E-mail: >")
        senha = input("Digite uma senha: >")
        Login.validarLogin(email, senha)

    #Finalizar ação
    elif menuAsk == 3:
        print("Tenha um otimo dia!")
        break
    
    else:
        print("Numero não reconhecido")

    #Menu interativo
    mostrarMenu()
    