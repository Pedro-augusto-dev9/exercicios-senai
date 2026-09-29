nome = input("Nome: ")
matricula = input("Matrícula: ")

notas = [float(input(f"Nota {i}: ")) for i in range(1, 6)]
media_orig = sum(notas) / 5

ultimo = int(matricula[-1])
bonus = 0.5 if ultimo <= 3 else 1.0 if ultimo <= 6 else 1.5

nota_final = min(media_orig + bonus, 10.0)

if nota_final < 5: sit = "Reprovado"
elif nota_final < 7: sit = "Recuperação"
elif nota_final <= 9: sit = "Aprovado"
else: sit = "Excelente"

acima = sum(1 for n in notas if n > media_orig)
abaixo = sum(1 for n in notas if n < media_orig)

print(f"\nMédia Original: {media_orig:.2f} | Bônus: {bonus} | Final: {nota_final:.2f}")
print(f"Situação: {sit}")
print(f"Maior nota: {max(notas)} | Menor nota: {min(notas)}")
print(f"Notas acima da média: {acima} | Abaixo: {abaixo}")
