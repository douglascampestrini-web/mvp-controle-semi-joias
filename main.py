
# Sistema de Controle de Estoque
# Projeto acadêmico em Python

produtos = []


def cadastrar_produto():
    nome = input("Nome do produto: ").strip()

    if not nome:
        print("Erro: o nome não pode ficar vazio.")
        return

    try:
        quantidade = int(input("Quantidade em estoque: "))

        if quantidade < 0:
            print("Erro: a quantidade não pode ser negativa.")
            return

    except ValueError:
        print("Erro: informe uma quantidade inteira válida.")
        return

    produto = {
        "nome": nome,
        "quantidade": quantidade
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- Estoque de Produtos ---")

    for produto in produtos:
        print(
            f"Produto: {produto['nome']} | "
            f"Quantidade: {produto['quantidade']}"
        )


def menu():
    while True:
        print("\n=== CONTROLE DE ESTOQUE ===")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
