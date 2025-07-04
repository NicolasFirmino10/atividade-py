# 1 - Calculadora com tratamento de erros

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao not in ['+', '-', '*', '/']:
            print("Operação inválida. Tente novamente.")
            continue

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            resultado = num1 / num2

        print(f"Resultado: {resultado}")
        break

    except ValueError:
        print("Entrada inválida. Digite apenas números.")
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
        
        
# 2 - Par ou Ímpar com contagem

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")


# 3 - Verificador de senha forte

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        continue

    if not any(char.isdigit() for char in senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    print("Senha forte cadastrada com sucesso!")
    break


# 4 - Registro de notas com média da turma

notas = []

while True:
    entrada = input("Digite uma nota (0 a 10) ou 'fim' para encerrar: ")

    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")