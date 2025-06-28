# 1. Classificador de Idade

idade = int(input("Informe sua idade: "))

if idade >= 0 and idade <= 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

# Saída
print(f"Classificação: {classificacao}")



# 2. Calculadora de IMC


peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))

imc = peso / (altura ** 2)


if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"


print(f"IMC: {imc:.2f} - {classificacao}")



# 3. Conversor de Temperatura


temperatura = float(input("Informe a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()


resultado = None

if origem == "C":
    if destino == "F":
        resultado = (temperatura * 9/5) + 32
    elif destino == "K":
        resultado = temperatura + 273.15
    elif destino == "C":
        resultado = temperatura

elif origem == "F":
    if destino == "C":
        resultado = (temperatura - 32) * 5/9
    elif destino == "K":
        resultado = (temperatura - 32) * 5/9 + 273.15
    elif destino == "F":
        resultado = temperatura

elif origem == "K":
    if destino == "C":
        resultado = temperatura - 273.15
    elif destino == "F":
        resultado = (temperatura - 273.15) * 9/5 + 32
    elif destino == "K":
        resultado = temperatura


if resultado is not None:
    print(f"Resultado: {resultado:.2f}°{destino}")
else:
    print("Unidades inválidas.")
    
    
# 4. Verificador de Ano Bissexto


ano = int(input("Informe o ano: "))


if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")