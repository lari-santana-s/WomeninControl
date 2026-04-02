from utils import validar_senha

def realizar_cadastro():
    print("Precisaremos de algumas informações para começar.")

    nome = input("Nome completo: ")
    idade = int(input('Idade: '))
    genero = input('Gênero: ')
    estado = input('Estado: ')
    cidade = input('Cidade: ')
    email = input('E-mail: ')
    senha = validar_senha(8)

    return {
        "nome": nome,
        "idade": idade,
        "genero": genero,
        "estado": estado,
        "cidade": cidade,
        "email": email,
        "senha": senha
    }