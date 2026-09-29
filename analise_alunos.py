matriculas = []
nomes = []
medias = []

while True:
    print("\n1-Cadastrar | 2-Listar | 3-Consultar | 4-Estatísticas | 5-Aprovados | 6-Reprovados | 7-Maior Média | 0-Sair")
    op = input("Opção: ")

    if op == "0":
        break

    elif op == "1":
        mat = input("Matrícula: ")
        if mat in matriculas:
            print("Matrícula duplicada!")
        else:
            nome = input("Nome: ")
            n1 = float(input("Nota 1: "))
            n2 = float(input("Nota 2: "))
            n3 = float(input("Nota 3: "))
            
            matriculas.append(mat)
            nomes.append(nome)
            medias.append((n1 + n2 + n3) / 3)

    elif op == "2":
        for i in range(len(matriculas)):
            sit = "Aprovado" if medias[i] >= 7 else "Recuperação" if medias[i] >= 5 else "Reprovado"
            print(f"{nomes[i]} ({matriculas[i]}) - Média: {medias[i]:.2f} - {sit}")

    elif op == "3":
        mat = input("Matrícula: ")
        if mat in matriculas:
            idx = matriculas.index(mat)
            print(f"Nome: {nomes[idx]} | Média: {medias[idx]:.2f}")
        else:
            print("Não encontrado.")

    elif op == "4" and medias:
        aprov = sum(1 for m in medias if m >= 7)
        rec = sum(1 for m in medias if 5 <= m < 7)
        print(f"Alunos: {len(medias)} | Média Geral: {sum(medias)/len(medias):.2f}")
        print(f"Maior: {max(medias):.2f} | Menor: {min(medias):.2f}")
        print(f"Aprovados: {aprov} | Rec: {rec} | Reprovados: {len(medias)-aprov-rec}")

    elif op == "5":
        for i in range(len(matriculas)):
            if medias[i] >= 7: print(f"{nomes[i]} ({matriculas[i]}) - Média: {medias[i]:.2f}")

    elif op == "6":
        for i in range(len(matriculas)):
            if medias[i] < 5: print(f"{nomes[i]} ({matriculas[i]}) - Média: {medias[i]:.2f}")

    elif op == "7" and medias:
        maior_m = max(medias)
        for i in range(len(matriculas)):
            if medias[i] == maior_m: print(f"Maior Média -> {nomes[i]} ({matriculas[i]}): {medias[i]:.2f}")
