# ==============================
# CATEGORIAS PADRÃO
# ==============================

CATEGORIAS_PADRAO = [
    "Moradia",
    "Alimentação",
    "Transporte",
    "Saúde",
    "Educação",
    "Lazer",
    "Compras",
    "Contas Fixas",
    "Investimentos",
    "Outros"
]

# ==============================
# MOSTRAR CATEGORIAS
# ==============================

def mostrar_categorias():
    print("\nEscolha uma categoria:")
    for i, categoria in enumerate(CATEGORIAS_PADRAO, start=1):
        print(f"{i} - {categoria}")

# ==============================
# ESCOLHER CATEGORIA
# ==============================

def escolher_categoria():
    while True:
        mostrar_categorias()
        try:
            opcao = int(input("Digite o número da categoria: "))
            if 1 <= opcao <= len(CATEGORIAS_PADRAO):
                return CATEGORIAS_PADRAO[opcao - 1]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

# ==============================
# COLETA DE DADOS FINANCEIROS
# ==============================

def coletar_dados_financeiros():
    mes = input("Mês: ")
    entrada = float(input('Total de entradas: R$ '))
    n = int(input('Quantos gastos deseja registrar: '))

    categorias = []
    economias = set()  # 👈 conjunto para evitar repetição
    saidas = 0

    for i in range(n):
        print(f"\nGasto {i+1}:")
        nome = escolher_categoria()

        valor = float(input('Valor gasto: R$ '))
        saidas += valor

        # Validação robusta da resposta
        while True:
            economia = input('Poderia economizar? (sim/não): ').strip().lower()
            if economia in ['sim', 's']:
                economias.add(nome)
                break
            elif economia in ['não', 'nao', 'n']:
                break
            else:
                print("Resposta inválida. Digite 'sim' ou 'não'.")

        categorias.append({
            "nome": nome,
            "valor": valor
        })

    return mes, entrada, saidas, categorias, list(economias)

# ==============================
# CÁLCULO DO SALDO
# ==============================

def calcular_saldo(entrada, saidas):
    return entrada - saidas

# ==============================
# ORDENAR GASTOS
# ==============================

def ordenar_gastos(categorias):
    return sorted(categorias, key=lambda x: x["valor"], reverse=True)

# ==============================
# EXIBIR RESUMO
# ==============================

def exibir_resumo(mes, entrada, saidas, saldo, categorias, economias):
    print(f"\nResumo de {mes}:")
    print(f"Entrada: R${entrada}")
    print(f"Saída: R${saidas}")
    print(f"Saldo: R${saldo}")

    print("\nGastos (maior → menor):")
    for item in categorias:
        print(f"{item['nome']}: R${item['valor']}")

    print("\nPossíveis economias:")
    if economias:
        for item in economias:
            print(item)
    else:
        print("Nenhuma economia identificada.")

# ==============================
# ALERTA FINANCEIRO
# ==============================

def gerar_alerta(saldo):
    if saldo == 0:
        print("Atenção! Você gastou tudo que ganhou.")
    elif saldo < 0:
        print("Cuidado! Você gastou mais do que ganhou.")

        