def validar_senha(tamanho_minimo):
    while True:
        senha = input(f'Digite uma senha de pelo menos {tamanho_minimo} caracteres: ')
        if len(senha) >= tamanho_minimo:
            print('Cadastro realizado com sucesso!\n')
            return senha
        else:
            print(f'Erro. A senha deve ter ao menos {tamanho_minimo} caracteres.')