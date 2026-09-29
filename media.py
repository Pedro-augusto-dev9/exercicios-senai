# programa em Python que solicite a matricula do aluno e três notas obtidas em avaliação.

print("---Programa de matricula--")
matricula = input("Digite a matrícula do aluno: ")
soma_nota = 0
banco = []
validar_nota = True

for i in range(1, 4):
    notas = float(input(f"Digite a nota {i}: "))
    if notas < 0 or notas > 10:
           print("Nota inválida. Digite uma nota entre 0 e 10.")
           validar_nota = False
           break
           
    banco.append(notas)
    soma_nota += notas

media = soma_nota / 3
print("Média calculada com sucesso.")
print("resultado: ")
if media <= 4:
        print("Reprovado")
elif media > 4 and media <= 5.9:
        print("Recuperação")
elif media > 5.9 and media <= 7.9:
        print("Aprovado")
elif media > 7.9 and media <= 10:
        print("Aprovado com excelente desempenho")
else:
        print("Nota inválida")

ultimo_digito = int(matricula[-1])
if ultimo_digito % 2 == 0:
    print("Perfil A")
else:
    print("Perfil B")

print(f"Notas inseridas: {banco}")
print(f"Aluno: {matricula}")
print(f"Média: {media:.2f}")