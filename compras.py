produtos = []

while True:
    print("\n1-Add | 2-Remover | 3-Consultar | 4-Alterar | 5-Listar | 0-Sair")
    opcao = input("Opção: ")

    if opcao == "0":
        print(f"\nCadastrados: {len(produtos)} | Máximo: 12 | Disponível: {12 - len(produtos)}")
        break

    elif opcao == "1":
        if len(produtos) >= 12:
            print("Lista cheia!")
        else:
            p = input("Produto: ").strip().lower()
            if not p:
                print("Não pode ser vazio.")
            elif p in produtos:
                print("Já cadastrado.")
            else:
                produtos.append(p)

    elif opcao == "2":
        p = input("Remover produto: ").strip().lower()
        if p in produtos:
            produtos.remove(p)
        else:
            print("Não encontrado.")

    elif opcao == "3":
        p = input("Consultar produto: ").strip().lower()
        print("Cadastrado" if p in produtos else "Não cadastrado")

    elif opcao == "4":
        atual = input("Produto atual: ").strip().lower()
        if atual in produtos:
            novo = input("Novo nome: ").strip().lower()
            if novo in produtos:
                print("Novo nome já existe na lista.")
            else:
                idx = produtos.index(atual)
                produtos[idx] = novo
        else:
            print("Não encontrado.")

    elif opcao == "5":
        for i, p in enumerate(produtos, 1):
            print(f"{i}. {p}")
