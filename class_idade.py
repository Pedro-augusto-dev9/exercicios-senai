idades = []

while True:
    idade = int(input("Digite a idade do aluno (0 para encerrar): "))
    
    if idade == 0:
        break
    elif idade < 0:
        print("Idade inválida! Não são permitidas idades negativas.")
        continue
        
    idades.append(idade)

    # Classificação imediata de cada idade digitada
    if idade <= 12:
        print("Classificação: Criança")
    elif idade <= 17:
        print("Classificação: Adolescente")
    elif idade <= 59:
        print("Classificação: Adulto")
    else:
        print("Classificação: Idoso")

if idades:
    total_alunos = len(idades)
    menores = sum(1 for id in idades if id < 18)
    maiores_18 = sum(1 for id in idades if id >= 18)
    maiores_50 = sum(1 for id in idades if id > 50)
    media = sum(idades) / total_alunos

    print(f"\nQuantidade total de alunos: {total_alunos}")
    print(f"Maior idade: {max(idades)} | Menor idade: {min(idades)}")
    print(f"Média das idades: {media:.2f}")
    print(f"Menores de idade: {menores}")
    print(f"Alunos com 18 anos ou mais: {maiores_18}")
    print(f"Alunos com mais de 50 anos: {maiores_50}")
