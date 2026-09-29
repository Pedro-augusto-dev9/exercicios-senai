matriculas = []
acertos = []

while True:
    mat = int(input("Matrícula (0 para sair): "))
    if mat == 0:
        break
    v_acertos = int(input("Acertos (0 a 10): "))
    matriculas.append(mat)
    acertos.append(v_acertos)

if acertos:
    aprov, rec, reprov = 0, 0, 0
    for a in acertos:
        if a >= 8: aprov += 1
        elif a >= 6: rec += 1
        else: reprov += 1

    maior = max(acertos)
    print(f"\nMédia da turma: {sum(acertos)/len(acertos):.2f}")
    print(f"Maior acerto: {maior} | Menor acerto: {min(acertos)}")
    print(f"Aprovados: {aprov} | Recuperação: {rec} | Reprovados: {reprov}")
    
    # Desafio: Alunos com maior acerto
    melhores = [matriculas[i] for i in range(len(acertos)) if acertos[i] == maior]
    print(f"Matrículas com maior nota: {melhores}")
