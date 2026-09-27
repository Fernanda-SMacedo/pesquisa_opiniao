contador = 1
total_excelente = 0
total_ruim = 0

while contador <= 50:
    print(f"\nEntrevistado {contador}:")
    nome_usuario = input("Digite o seu nome: ")
    idade_usuario = input("Digite a sua idade: ")
    opiniao_usuario = input("Digite sua opinião sobre o atendimento (1: EXCELENTE, 2: BOM E 3: RUIM): ").lower()

    if opiniao_usuario == "1":
        total_excelente += 1
    elif opiniao_usuario == "3":
        total_ruim += 1

    print("Obrigada por participar da pesquisa!")
    contador += 1

print("\n--- Resultado da pesquisa ---")
print(f"Quantidade de respostas EXCELENTE: {total_excelente}")
print(f"Quantidade de respostas RUIM: {total_ruim}")




