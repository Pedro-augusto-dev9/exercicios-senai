matricula = input("digite a matrícula do aluno: ")
primeiro_digito = int(str(matricula)[0])
ultimo_digito = int(str(matricula)[-1])

if not matricula.isdigit():
    print("Matrícula inválida. Digite uma matrícula numérica.")

elif len(str(matricula)) != 8:
    print("Matrícula inválida. Digite uma matrícula com 8 dígitos.")

elif primeiro_digito == 0:
    print("Matrícula inválida. O primeiro dígito não pode ser zero.")

else:
    print("Matrícula válida.")
    
soma_digitos = sum(int(d) for d in matricula)
if soma_digitos < 20:
    categoria = "Categoria 1"
elif soma_digitos <= 39:    
    categoria = "Categoria 2"
else:
    categoria = "Categoria 3"

print(f"Primeiro dígito: {primeiro_digito}")
print(f"Último dígito: {ultimo_digito}")
print(f"Matrícula: {matricula}")
print(f"soma dos dígitos: {soma_digitos}")
print(f"Categoria: {categoria}")