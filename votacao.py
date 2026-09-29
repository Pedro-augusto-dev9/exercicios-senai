votos = []

while True:
    voto = int(input("Digite o seu voto (1, 2, 3 ou 9 para encerrar): "))
    if voto == 9:
        break
    votos.append(voto)

total_votos = len(votos)
cand_a = 0
cand_b = 0
cand_c = 0
invalidos = 0

for v in votos:
    if v == 1:
        cand_a += 1
    elif v == 2:
        cand_b += 1
    elif v == 3:
        cand_c += 1
    else:
        invalidos += 1

perc_a = (cand_a / total_votos * 100) if total_votos > 0 else 0
perc_b = (cand_b / total_votos * 100) if total_votos > 0 else 0
perc_c = (cand_c / total_votos * 100) if total_votos > 0 else 0

maior_voto = max(cand_a, cand_b, cand_c)
if cand_a == cand_b == cand_c == 0:
    mais_votado = "Nenhum candidato recebeu votos"
elif cand_a > cand_b and cand_a > cand_c:
    mais_votado = "Candidato A"
elif cand_b > cand_a and cand_b > cand_c:
    mais_votado = "Candidato B"
elif cand_c > cand_a and cand_c > cand_b:
    mais_votado = "Candidato C"
else:
    mais_votado = "Empate"

print(f"\nQuantidade total de votos: {total_votos}")
print(f"Quantidade de votos do Candidato A: {cand_a}")
print(f"Quantidade de votos do Candidato B: {cand_b}")
print(f"Quantidade de votos do Candidato C: {cand_c}")
print(f"Quantidade de votos inválidos: {invalidos}")
print(f"Percentual do Candidato A: {perc_a:.2f}%")
print(f"Percentual do Candidato B: {perc_b:.2f}%")
print(f"Percentual do Candidato C: {perc_c:.2f}%")
print(f"Candidato mais votado: {mais_votado}")