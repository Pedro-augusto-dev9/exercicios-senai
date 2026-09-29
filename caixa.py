saldo = float(input("Digite o saldo inicial: "))
extrato = []

while True:
    print("\n1-Saldo | 2-Depositar | 3-Sacar | 4-Extrato | 0-Sair")
    op = input("Opção: ")

    if op == "0":
        break
    elif op == "1":
        print(f"Saldo: R$ {saldo:.2f}")
    elif op == "2":
        v = float(input("Valor do depósito: "))
        if v > 0:
            saldo += v
            extrato.append(f"Deposito: R$ {v:.2f}")
        else: print("Valor inválido.")
    elif op == "3":
        v = float(input("Valor do saque: "))
        if 0 < v <= saldo:
            saldo -= v
            extrato.append(f"Saque: R$ {v:.2f}")
        else: print("Saldo insuficiente ou valor inválido.")
    elif op == "4":
        dep, saq, t_dep, t_saq = 0, 0, 0, 0
        for op_txt in extrato:
            print(op_txt)
            val = float(op_txt.split("R$ ")[1])
            if "Deposito" in op_txt:
                dep += 1; t_dep += val
            else:
                saq += 1; t_saq += val
        print(f"\nDepósitos: {dep} (Total: R$ {t_dep:.2f})")
        print(f"Saques: {saq} (Total: R$ {t_saq:.2f})")
        print(f"Saldo atual: R$ {saldo:.2f}")
