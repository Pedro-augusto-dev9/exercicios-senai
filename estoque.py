produtos = ["Arroz", "Feijao", "Macarrao", "Cafe", "Acucar"]
quantidades = [15, 8, 20, 5, 12]

while True:
    print("\n1-Listar | 2-Consultar | 3-Entrada | 4-Saída | 5-Baixo Estoque | 0-Sair")
    opcao = input("Opção: ")

    if opcao == "0":
        break

    elif opcao == "1":
        for p, q in zip(produtos, quantidades):
            print(f"{p}: {q} unidades")

    elif opcao == "2":
        p = input("Produto: ").capitalize()
        if p in produtos:
            print(f"Estoque de {p}: {quantidades[produtos.index(p)]}")
        else:
            print("Inexistente.")

    elif opcao == "3":
        p = input("Produto: ").capitalize()
        if p in produtos:
            qtd = int(input("Qtd recebida: "))
            if qtd < 0: print("Proibido valor negativo.")
            else: quantidades[produtos.index(p)] += qtd
        else:
            print("Inexistente.")

    elif opcao == "4":
        p = input("Produto: ").capitalize()
        if p in produtos:
            qtd = int(input("Qtd retirada: "))
            idx = produtos.index(p)
            if qtd < 0: print("Proibido valor negativo.")
            elif qtd > quantidades[idx]: print("Estoque insuficiente.")
            else: quantidades[idx] -= qtd
        else:
            print("Inexistente.")

    elif opcao == "5":
        for p, q in zip(produtos, quantidades):
            if q < 10: print(f"Baixo estoque -> {p}: {q}")
