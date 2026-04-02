from cadastro import realizar_cadastro
from financeiro import (
    coletar_dados_financeiros,
    calcular_saldo,
    ordenar_gastos,
    exibir_resumo,
    gerar_alerta
)

print("Seja bem-vinda ao WomeninControl!")

opcao = input("Deseja se cadastrar? (sim/não): ")

if opcao.lower() != 'não':
    usuario = realizar_cadastro()

    mes, entrada, saidas, categorias, economias = coletar_dados_financeiros()
    saldo = calcular_saldo(entrada, saidas)

    categorias_ordenadas = ordenar_gastos(categorias)

    exibir_resumo(mes, entrada, saidas, saldo, categorias_ordenadas, economias)
    gerar_alerta(saldo)
else:
    print("Até a próxima!")
    